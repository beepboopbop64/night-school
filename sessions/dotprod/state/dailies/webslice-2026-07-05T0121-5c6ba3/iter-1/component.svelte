<script>
	// Probe angle in degrees, 0 = pointing right, increasing counterclockwise.
	let value = $state(90);
	let dragging = false;

	const candidatesDef = [
		{ id: 'c1', angle: 20 },
		{ id: 'c2', angle: 70 },
		{ id: 'c3', angle: 110 },
		{ id: 'c4', angle: 160 }
	];

	const cx = 130;
	const cy = 130;

	function point(angleDeg, radius) {
		const rad = (angleDeg * Math.PI) / 180;
		return { x: cx + radius * Math.cos(rad), y: cy - radius * Math.sin(rad) };
	}

	function clamp(v) {
		return Math.min(360, Math.max(0, v));
	}

	let probeTip = $derived(point(value, 100));
	let probeLabel = $derived(point(value, 122));

	let scores = $derived(
		candidatesDef.map((c) => {
			const raw = Math.cos(((value - c.angle) * Math.PI) / 180);
			const top = raw >= 0 ? 50 - raw * 50 : 50;
			const height = Math.abs(raw) * 50;
			return { id: c.id, angle: c.angle, score: raw, top, height };
		})
	);

	let bestId = $derived.by(() => {
		let best = scores[0];
		for (const s of scores) {
			if (s.score > best.score) best = s;
		}
		return best.id;
	});

	function angleFromPointer(e) {
		const rect = e.currentTarget.getBoundingClientRect();
		const centerX = rect.left + rect.width / 2;
		const centerY = rect.top + rect.height / 2;
		const dx = e.clientX - centerX;
		const dy = e.clientY - centerY;
		let deg = (Math.atan2(-dy, dx) * 180) / Math.PI;
		if (deg < 0) deg += 360;
		value = Math.round(deg);
	}

	function handlePointerDown(e) {
		e.currentTarget.setPointerCapture(e.pointerId);
		dragging = true;
		angleFromPointer(e);
	}

	function handlePointerMove(e) {
		if (!dragging) return;
		angleFromPointer(e);
	}

	function handlePointerUp(e) {
		dragging = false;
		try {
			e.currentTarget.releasePointerCapture(e.pointerId);
		} catch (err) {
			// pointer capture already released, ignore
		}
	}

	function handleKeydown(e) {
		const step = 5;
		let handled = true;
		switch (e.key) {
			case 'ArrowRight':
			case 'ArrowUp':
				value = clamp(value + step);
				break;
			case 'ArrowLeft':
			case 'ArrowDown':
				value = clamp(value - step);
				break;
			case 'Home':
				value = 0;
				break;
			case 'End':
				value = 360;
				break;
			default:
				handled = false;
		}
		if (handled) e.preventDefault();
	}
</script>

<div class="wrapper" data-interactive="dot-alignment">
	<p class="instruction">Turn the probe. Each bar tracks how closely it points at that candidate.</p>

	<div class="stage">
		<div class="dial-wrap">
			<svg class="dial" viewBox="0 0 260 260" aria-hidden="true">
				<defs>
					<marker id="dot-alignment-arrow-heat" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
						<path d="M0,0 L8,4 L0,8 Z" style="fill: var(--data-heat)" />
					</marker>
					<marker id="dot-alignment-arrow-observed" markerWidth="7" markerHeight="7" refX="3.5" refY="3.5" orient="auto">
						<path d="M0,0 L7,3.5 L0,7 Z" style="fill: var(--data-observed)" />
					</marker>
				</defs>

				<circle cx={cx} cy={cy} r="98" fill="none" style="stroke: var(--color-text); stroke-opacity: 0.12; stroke-width: 1.5" />
				<circle cx={cx} cy={cy} r="3.5" style="fill: var(--color-text); fill-opacity: 0.4" />

				{#each candidatesDef as c (c.id)}
					{@const tip = point(c.angle, 76)}
					{@const label = point(c.angle, 98)}
					<line
						x1={cx}
						y1={cy}
						x2={tip.x}
						y2={tip.y}
						style="stroke: var(--data-observed); stroke-width: 2.5; stroke-opacity: 0.75"
						marker-end="url(#dot-alignment-arrow-observed)"
					/>
					<text
						x={label.x}
						y={label.y}
						text-anchor="middle"
						dominant-baseline="middle"
						style="fill: var(--color-text); font-family: var(--font-mono); font-size: 11px"
					>{c.id}</text>
				{/each}

				<line
					x1={cx}
					y1={cy}
					x2={probeTip.x}
					y2={probeTip.y}
					style="stroke: var(--data-heat); stroke-width: 4"
					marker-end="url(#dot-alignment-arrow-heat)"
				/>
				<text
					x={probeLabel.x}
					y={probeLabel.y}
					text-anchor="middle"
					dominant-baseline="middle"
					style="fill: var(--color-text); font-family: var(--font-mono); font-size: 12px; font-weight: 600"
				>probe {value}&deg;</text>
			</svg>

			<div
				class="slider"
				role="slider"
				tabindex="0"
				aria-label="Probe angle in degrees"
				aria-valuemin="0"
				aria-valuemax="360"
				aria-valuenow={value}
				onpointerdown={handlePointerDown}
				onpointermove={handlePointerMove}
				onpointerup={handlePointerUp}
				onpointercancel={handlePointerUp}
				onkeydown={handleKeydown}
			></div>
		</div>

		<div class="scores">
			{#each scores as s (s.id)}
				<div class="score-col" class:best={s.id === bestId}>
					<span class="score-label">{s.id}</span>
					<div class="track">
						<div class="zero-line"></div>
						<div class="fill" style={`top:${s.top}%; height:${s.height}%`}></div>
					</div>
					<span class="score-value">{s.score.toFixed(2)}</span>
				</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.wrapper {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: clamp(1rem, 3vw, 1.75rem);
		width: 100%;
		max-width: 640px;
		margin: 0 auto;
		box-sizing: border-box;
		padding: clamp(1rem, 4vw, 2rem);
		background: var(--color-bg);
		color: var(--color-text);
	}

	.instruction {
		margin: 0;
		text-align: center;
		font-family: var(--font-body);
		font-size: clamp(0.85rem, 1.6vw, 1rem);
		opacity: 0.85;
	}

	.stage {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: clamp(1.25rem, 4vw, 2rem);
		width: 100%;
	}

	.dial-wrap {
		position: relative;
		width: clamp(180px, 42vw, 300px);
		aspect-ratio: 1 / 1;
	}

	.dial {
		width: 100%;
		height: 100%;
		display: block;
	}

	.slider {
		position: absolute;
		inset: 0;
		border-radius: 50%;
		cursor: grab;
		touch-action: none;
	}

	.slider:focus-visible {
		outline: 2px solid var(--color-text);
		outline-offset: 3px;
	}

	.scores {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		gap: clamp(0.75rem, 3vw, 1.5rem);
		width: 100%;
	}

	.score-col {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.4rem;
		min-width: 4rem;
		opacity: 0.55;
		transition: opacity 150ms ease;
	}

	.score-col.best {
		opacity: 1;
	}

	.score-label {
		font-family: var(--font-mono);
		font-size: 0.85rem;
		color: var(--color-text);
	}

	.track {
		position: relative;
		width: clamp(1.5rem, 4vw, 2.25rem);
		height: 9rem;
		background: color-mix(in srgb, var(--color-text) 6%, transparent);
		border-radius: 0.2rem;
	}

	.zero-line {
		position: absolute;
		left: 0;
		right: 0;
		top: 50%;
		height: 1px;
		background: color-mix(in srgb, var(--color-text) 35%, transparent);
	}

	.fill {
		position: absolute;
		left: 0;
		right: 0;
		background: var(--data-params);
		border-radius: 0.15rem;
		transition: top 120ms ease, height 120ms ease;
	}

	.score-col.best .fill {
		background: var(--data-params);
	}

	.score-value {
		font-family: var(--font-mono);
		font-size: 0.85rem;
		font-weight: 600;
		color: var(--data-params);
	}

	@media (prefers-reduced-motion: reduce) {
		.fill,
		.score-col {
			transition: none;
		}
	}
</style>
