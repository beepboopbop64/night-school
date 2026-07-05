<script>
	let angle = $state(90);
	let dragging = false;
	let svgEl;

	const candidates = [
		{ id: 'c1', deg: 20 },
		{ id: 'c2', deg: 70 },
		{ id: 'c3', deg: 110 },
		{ id: 'c4', deg: 160 }
	];

	function toPoint(deg, r, cx = 200, cy = 200) {
		const rad = (deg * Math.PI) / 180;
		return { x: cx + r * Math.cos(rad), y: cy - r * Math.sin(rad) };
	}

	// Offsets a point tangentially (sideways along the circle) so a label
	// placed near an arrow's tip never sits directly on the arrow's line,
	// even if another arrow later points at that same angle.
	function toTangentPoint(deg, r, sideOffset, cx = 200, cy = 200) {
		const rad = (deg * Math.PI) / 180;
		return {
			x: cx + r * Math.cos(rad) - sideOffset * Math.sin(rad),
			y: cy - r * Math.sin(rad) - sideOffset * Math.cos(rad)
		};
	}

	const scores = $derived(
		candidates.map((c) => {
			const diff = ((angle - c.deg) * Math.PI) / 180;
			return Math.round(100 * Math.cos(diff));
		})
	);

	const bestIndex = $derived(
		scores.reduce((best, s, i) => (s > scores[best] ? i : best), 0)
	);

	function angleFromClient(clientX, clientY) {
		const rect = svgEl.getBoundingClientRect();
		const cx = rect.left + rect.width / 2;
		const cy = rect.top + rect.height / 2;
		const dx = clientX - cx;
		const dy = clientY - cy;
		let a = (Math.atan2(-dy, dx) * 180) / Math.PI;
		if (a < 0) a += 360;
		return Math.round(a);
	}

	function handlePointerDown(e) {
		dragging = true;
		svgEl.setPointerCapture(e.pointerId);
		angle = angleFromClient(e.clientX, e.clientY);
	}

	function handlePointerMove(e) {
		if (!dragging) return;
		angle = angleFromClient(e.clientX, e.clientY);
	}

	function handlePointerUp(e) {
		dragging = false;
		try {
			svgEl.releasePointerCapture(e.pointerId);
		} catch (err) {
			// already released, ignore
		}
	}

	function handleKeydown(e) {
		let handled = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp') {
			angle = Math.min(360, angle + 5);
		} else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') {
			angle = Math.max(0, angle - 5);
		} else if (e.key === 'Home') {
			angle = 0;
		} else if (e.key === 'End') {
			angle = 360;
		} else {
			handled = false;
		}
		if (handled) e.preventDefault();
	}

	function fmt(n) {
		return n > 0 ? `+${n}` : `${n}`;
	}

	const probeTip = $derived(toPoint(angle, 148));
	const probeLabel = $derived.by(() => {
		const rad = (angle * Math.PI) / 180;
		const shaftR = 80;
		const sideOffset = 22;
		return {
			x: 200 + shaftR * Math.cos(rad) - sideOffset * Math.sin(rad),
			y: 200 - shaftR * Math.sin(rad) - sideOffset * Math.cos(rad)
		};
	});
</script>

<div data-interactive="dot-alignment" class="wrap">
	<p class="instruction">Turn the probe (drag it or use arrow keys) until a bar peaks.</p>

	<div class="stage">
		<svg
			bind:this={svgEl}
			class="dial"
			viewBox="0 0 400 400"
			role="slider"
			tabindex="0"
			aria-label="Probe angle in degrees"
			aria-valuemin="0"
			aria-valuemax="360"
			aria-valuenow={angle}
			aria-valuetext={`${angle} degrees`}
			onpointerdown={handlePointerDown}
			onpointermove={handlePointerMove}
			onpointerup={handlePointerUp}
			onpointercancel={handlePointerUp}
			onkeydown={handleKeydown}
		>
			<defs>
				<marker id="head-probe" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto">
					<path d="M0,0 L10,5 L0,10 Z" style="fill: var(--data-heat)" />
				</marker>
				<marker id="head-candidate" markerWidth="9" markerHeight="9" refX="5" refY="4.5" orient="auto">
					<path d="M0,0 L9,4.5 L0,9 Z" style="fill: var(--data-observed)" />
				</marker>
			</defs>

			<circle cx="200" cy="200" r="160" fill="none" stroke="var(--color-text)" stroke-width="1" opacity="0.12" />
			<circle cx="200" cy="200" r="4" fill="var(--color-text)" opacity="0.3" />

			{#each candidates as c, i}
				{@const tip = toPoint(c.deg, 130)}
				{@const lbl = toTangentPoint(c.deg, 160, 26)}
				<line
					x1="200"
					y1="200"
					x2={tip.x}
					y2={tip.y}
					stroke="var(--data-observed)"
					stroke-width="3"
					opacity={i === bestIndex ? 0.85 : 0.4}
					marker-end="url(#head-candidate)"
				/>
				<text
					x={lbl.x}
					y={lbl.y}
					text-anchor="middle"
					dominant-baseline="middle"
					class="tip-label"
					style="fill: var(--color-text)"
				>{c.id}</text>
			{/each}

			<line
				x1="200"
				y1="200"
				x2={probeTip.x}
				y2={probeTip.y}
				stroke="var(--data-heat)"
				stroke-width="6"
				marker-end="url(#head-probe)"
			/>
			<text
				x={probeLabel.x}
				y={probeLabel.y}
				text-anchor="middle"
				dominant-baseline="middle"
				class="probe-label"
				style="fill: var(--color-text)"
			>probe {angle}°</text>
		</svg>
	</div>

	<div class="scores">
		{#each candidates as c, i}
			<div class="score-col" class:leading={i === bestIndex}>
				<div class="score-name" style="color: var(--color-text)">{c.id}</div>
				<div class="bar-track">
					<div class="zero-line"></div>
					{#if scores[i] >= 0}
						<div class="bar pos" style="height: {Math.abs(scores[i]) * 0.55}px; opacity: {i === bestIndex ? 1 : 0.45}"></div>
					{:else}
						<div class="bar neg" style="height: {Math.abs(scores[i]) * 0.55}px; opacity: {i === bestIndex ? 1 : 0.45}"></div>
					{/if}
				</div>
				<div class="score-num">{fmt(scores[i])}</div>
			</div>
		{/each}
	</div>
</div>

<style>
	.wrap {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: clamp(0.75rem, 2.5vw, 1.25rem);
		width: 100%;
		max-width: 640px;
		margin: 0 auto;
		padding: clamp(0.75rem, 3vw, 1.5rem);
		box-sizing: border-box;
		font-family: var(--font-body);
		color: var(--color-text);
		background: var(--color-bg);
	}

	.instruction {
		margin: 0;
		font-size: clamp(0.85rem, 1.6vw, 1rem);
		opacity: 0.85;
		text-align: center;
	}

	.stage {
		width: 100%;
		max-width: 420px;
	}

	.dial {
		width: 100%;
		height: auto;
		aspect-ratio: 1 / 1;
		display: block;
		touch-action: none;
		cursor: grab;
	}

	.dial:focus-visible {
		outline: 2px solid var(--data-heat);
		outline-offset: 4px;
	}

	.tip-label {
		font-family: var(--font-mono);
		font-size: 16px;
	}

	.probe-label {
		font-family: var(--font-mono);
		font-size: 17px;
		font-weight: 600;
	}

	.scores {
		display: flex;
		justify-content: space-between;
		gap: clamp(0.4rem, 2vw, 1rem);
		width: 100%;
		max-width: 460px;
	}

	.score-col {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.25rem;
		flex: 1 1 0;
		min-width: 0;
	}

	.score-name {
		font-family: var(--font-mono);
		font-size: clamp(0.7rem, 1.6vw, 0.85rem);
		opacity: 0.8;
	}

	.bar-track {
		position: relative;
		width: 100%;
		max-width: 44px;
		margin: 0 auto;
		height: 120px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.zero-line {
		position: absolute;
		left: 0;
		right: 0;
		top: 50%;
		height: 1px;
		background: var(--color-text);
		opacity: 0.2;
	}

	.bar {
		position: absolute;
		width: 60%;
		max-width: 26px;
		background: var(--data-params);
		border-radius: 2px;
	}

	.bar.pos {
		bottom: 50%;
	}

	.bar.neg {
		top: 50%;
	}

	.leading .bar {
		box-shadow: 0 0 0 1px var(--data-params);
	}

	.score-num {
		font-family: var(--font-mono);
		font-size: clamp(0.7rem, 1.6vw, 0.8rem);
		color: var(--data-params);
		opacity: 0.75;
	}

	.leading .score-num {
		opacity: 1;
		font-weight: 600;
	}

	@media (prefers-reduced-motion: reduce) {
		.dial,
		.bar,
		.score-num {
			transition: none !important;
			animation: none !important;
		}
	}
</style>
