<script>
	// Turn the probe until the meter agrees.
	// probeAngle: primary slider value, degrees, 0..360, step 5.
	// lengthC1: named auxiliary control, relative length of candidate c1, 0.5..2, step 0.1.
	let probeAngle = $state(40);
	let lengthC1 = $state(1);

	let diagramEl = $state(null);

	// viewBox is deliberately wider than tall: candidates only ever fan through
	// the upper half of the circle, so the canvas is cropped to that content
	// instead of wasting a full square of empty space above the score bars.
	const VIEW_W = 320;
	const VIEW_H = 230;
	const CENTER_X = 160;
	const CENTER_Y = 150;
	const R = 50;
	const MAX_SCORE = 2;

	const baseCandidates = [
		{ name: 'c1', angle: 20 },
		{ name: 'c2', angle: 70 },
		{ name: 'c3', angle: 110 },
		{ name: 'c4', angle: 160 }
	];

	function computeHead(tipX, tipY, dirX, dirY, shaftLen) {
		const headLen = shaftLen * 0.18;
		const halfW = shaftLen * 0.09;
		const backX = tipX - dirX * headLen;
		const backY = tipY - dirY * headLen;
		const perpX = -dirY;
		const perpY = dirX;
		const lx = backX + perpX * halfW;
		const ly = backY + perpY * halfW;
		const rx = backX - perpX * halfW;
		const ry = backY - perpY * halfW;
		return { backX, backY, poly: `${tipX},${tipY} ${lx},${ly} ${rx},${ry}` };
	}

	let candidateData = $derived.by(() => {
		return baseCandidates.map((c) => {
			const len = c.name === 'c1' ? lengthC1 : 1;
			const rad = (c.angle * Math.PI) / 180;
			const dirX = Math.cos(rad);
			const dirY = -Math.sin(rad);
			const shaft = R * len;
			const tipX = CENTER_X + dirX * shaft;
			const tipY = CENTER_Y + dirY * shaft;
			const head = computeHead(tipX, tipY, dirX, dirY, shaft);
			// label offset is measured from the TIP, not from the center, so it
			// stays a fixed safe distance from the length handle no matter how
			// long or short c1 gets.
			const labelR = shaft + 36;
			const labelX = CENTER_X + dirX * labelR;
			const labelY = CENTER_Y + dirY * labelR;
			const diff = ((probeAngle - c.angle) * Math.PI) / 180;
			const score = Math.cos(diff) * len;
			return { ...c, len, tipX, tipY, ...head, labelX, labelY, score };
		});
	});

	let probeGeom = $derived.by(() => {
		const rad = (probeAngle * Math.PI) / 180;
		const dirX = Math.cos(rad);
		const dirY = -Math.sin(rad);
		const shaft = R;
		const tipX = CENTER_X + dirX * shaft;
		const tipY = CENTER_Y + dirY * shaft;
		const head = computeHead(tipX, tipY, dirX, dirY, shaft);
		const perpX = -dirY;
		const perpY = dirX;
		// Pushed well clear of the 44px handle hit box (radial + tangential
		// combined) so the label never sits under the probe dot or its focus
		// ring at any angle. The radial reach is deliberately well beyond any
		// candidate label's radius (even c1 stretched to its own labels'
		// range) and the tangential kick is large enough that even when the
		// probe sits exactly on top of a candidate's line (e.g. 70 degrees on
		// c2), the two label centers land 40+ px apart, never abutting.
		const labelX = CENTER_X + dirX * (R + 56) + perpX * 38;
		const labelY = CENTER_Y + dirY * (R + 56) + perpY * 38;
		return { tipX, tipY, ...head, labelX, labelY };
	});

	let probeHandlePos = $derived.by(() => ({
		x: (probeGeom.tipX / VIEW_W) * 100,
		y: (probeGeom.tipY / VIEW_H) * 100
	}));

	let c1HandlePos = $derived.by(() => {
		const c1 = candidateData.find((c) => c.name === 'c1');
		return { x: (c1.tipX / VIEW_W) * 100, y: (c1.tipY / VIEW_H) * 100 };
	});

	function roundScore(s) {
		let v = Math.round(s * 10) / 10;
		if (Object.is(v, -0)) v = 0;
		return v;
	}

	// A leader is only crowned when its rounded, displayed score strictly
	// beats every other rounded score. If two or more candidates share the
	// top rounded value the emphasis is suppressed entirely (no false bold).
	let leaderName = $derived.by(() => {
		const rounded = candidateData.map((c) => roundScore(c.score));
		const max = Math.max(...rounded);
		const tiedCount = rounded.filter((r) => r === max).length;
		if (tiedCount > 1) return null;
		const idx = rounded.indexOf(max);
		return candidateData[idx].name;
	});

	function updateProbeFromEvent(e) {
		if (!diagramEl) return;
		const rect = diagramEl.getBoundingClientRect();
		const scaleX = VIEW_W / rect.width;
		const scaleY = VIEW_H / rect.height;
		const lx = (e.clientX - rect.left) * scaleX;
		const ly = (e.clientY - rect.top) * scaleY;
		const dx = lx - CENTER_X;
		const dy = ly - CENTER_Y;
		let deg = (Math.atan2(-dy, dx) * 180) / Math.PI;
		if (deg < 0) deg += 360;
		if (deg > 360) deg = 360;
		probeAngle = deg;
	}

	function onProbePointerDown(e) {
		e.preventDefault();
		e.currentTarget.setPointerCapture(e.pointerId);
		updateProbeFromEvent(e);
		const move = (ev) => updateProbeFromEvent(ev);
		const up = () => {
			window.removeEventListener('pointermove', move);
			window.removeEventListener('pointerup', up);
		};
		window.addEventListener('pointermove', move);
		window.addEventListener('pointerup', up);
	}

	function onProbeKeydown(e) {
		let handled = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp') probeAngle = Math.min(360, probeAngle + 5);
		else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') probeAngle = Math.max(0, probeAngle - 5);
		else if (e.key === 'Home') probeAngle = 0;
		else if (e.key === 'End') probeAngle = 360;
		else handled = false;
		if (handled) e.preventDefault();
	}

	function updateLengthFromEvent(e) {
		if (!diagramEl) return;
		const rect = diagramEl.getBoundingClientRect();
		const scaleX = VIEW_W / rect.width;
		const scaleY = VIEW_H / rect.height;
		const lx = (e.clientX - rect.left) * scaleX;
		const ly = (e.clientY - rect.top) * scaleY;
		const dx = lx - CENTER_X;
		const dy = ly - CENTER_Y;
		const dist = Math.sqrt(dx * dx + dy * dy);
		let len = dist / R;
		len = Math.min(2, Math.max(0.5, len));
		lengthC1 = Math.round(len * 10) / 10;
	}

	function onLengthPointerDown(e) {
		e.preventDefault();
		e.currentTarget.setPointerCapture(e.pointerId);
		updateLengthFromEvent(e);
		const move = (ev) => updateLengthFromEvent(ev);
		const up = () => {
			window.removeEventListener('pointermove', move);
			window.removeEventListener('pointerup', up);
		};
		window.addEventListener('pointermove', move);
		window.addEventListener('pointerup', up);
	}

	function onLengthKeydown(e) {
		let handled = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp')
			lengthC1 = Math.min(2, Math.round((lengthC1 + 0.1) * 10) / 10);
		else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown')
			lengthC1 = Math.max(0.5, Math.round((lengthC1 - 0.1) * 10) / 10);
		else if (e.key === 'Home') lengthC1 = 0.5;
		else if (e.key === 'End') lengthC1 = 2;
		else handled = false;
		if (handled) e.preventDefault();
	}
</script>

<div class="wrap" data-interactive="dot-alignment">
	<p class="instruction">Drag the probe to score each candidate. Drag c1's handle to change its length.</p>

	<div class="diagram-wrap" bind:this={diagramEl}>
		<svg
			viewBox="0 0 {VIEW_W} {VIEW_H}"
			class="diagram-svg"
			role="img"
			aria-label="Diagram: an amber probe arrow rotates among four periwinkle candidate arrows, c1 through c4"
		>
			{#each candidateData as c (c.name)}
				<line
					x1={CENTER_X}
					y1={CENTER_Y}
					x2={c.backX}
					y2={c.backY}
					stroke="var(--data-observed)"
					stroke-width="2.2"
					stroke-linecap="round"
				/>
				<polygon points={c.poly} fill="var(--data-observed)" />
				<text
					x={c.labelX}
					y={c.labelY}
					class="arrow-label"
					text-anchor="middle"
					dominant-baseline="middle"
					aria-hidden="true"
				>
					{c.name}
				</text>
			{/each}

			<line
				x1={CENTER_X}
				y1={CENTER_Y}
				x2={probeGeom.backX}
				y2={probeGeom.backY}
				stroke="var(--data-heat)"
				stroke-width="2.2"
				stroke-linecap="round"
				class="probe-line"
			/>
			<polygon points={probeGeom.poly} fill="var(--data-heat)" />
			<text
				x={probeGeom.labelX}
				y={probeGeom.labelY}
				class="arrow-label probe-label"
				text-anchor="middle"
				dominant-baseline="middle"
				aria-hidden="true"
			>
				probe
			</text>
		</svg>

		<div
			class="handle probe-handle"
			style="left: {probeHandlePos.x}%; top: {probeHandlePos.y}%; --handle-color: var(--data-heat);"
			role="slider"
			tabindex="0"
			aria-label="probe angle in degrees"
			aria-valuemin="0"
			aria-valuemax="360"
			aria-valuenow={Math.round(probeAngle)}
			onpointerdown={onProbePointerDown}
			onkeydown={onProbeKeydown}
		></div>

		<div
			class="handle length-handle"
			style="left: {c1HandlePos.x}%; top: {c1HandlePos.y}%; --handle-color: var(--data-observed);"
			data-control="length-c1"
			role="spinbutton"
			tabindex="0"
			aria-label="c1 length"
			aria-valuemin="0.5"
			aria-valuemax="2"
			aria-valuenow={lengthC1.toFixed(1)}
			onpointerdown={onLengthPointerDown}
			onkeydown={onLengthKeydown}
		></div>
	</div>

	<div class="bars">
		{#each candidateData as c (c.name)}
			{@const displayScore = roundScore(c.score).toFixed(1)}
			<div class="bar-col">
				<div class="bar-track">
					<div class="bar-zero"></div>
					<div
						class="bar-fill"
						class:leading={c.name === leaderName}
						style="height: {Math.min(Math.abs(c.score) / MAX_SCORE, 1) * 40}px; {c.score >= 0
							? 'bottom: 50%;'
							: 'top: 50%;'}"
					></div>
				</div>
				<span class="readout" class:leading={c.name === leaderName} aria-label="{c.name} score {displayScore}"
					>{displayScore}</span
				>
				<span class="cand-label">{c.name}</span>
			</div>
		{/each}
	</div>
</div>

<style>
	.wrap {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.65rem;
		width: 100%;
		max-width: 520px;
		margin: 0 auto;
		padding: 1rem;
		box-sizing: border-box;
	}

	.instruction {
		font-family: var(--font-body);
		color: var(--color-text);
		font-size: 0.9rem;
		opacity: 0.85;
		text-align: center;
		margin: 0;
	}

	.diagram-wrap {
		position: relative;
		width: 100%;
		max-width: 400px;
		aspect-ratio: 320 / 230;
	}

	.diagram-svg {
		width: 100%;
		height: 100%;
		display: block;
	}

	.arrow-label {
		font-family: var(--font-mono);
		fill: var(--color-text);
		font-size: 13px;
		pointer-events: none;
		user-select: none;
	}

	.probe-label {
		font-size: 13px;
	}

	.handle {
		position: absolute;
		width: 46px;
		height: 46px;
		transform: translate(-50%, -50%);
		display: flex;
		align-items: center;
		justify-content: center;
		touch-action: none;
		cursor: grab;
		background: transparent;
		border: none;
		padding: 0;
	}

	.handle::before {
		content: '';
		width: 14px;
		height: 14px;
		border-radius: 50%;
		background: var(--handle-color);
		box-shadow: 0 0 0 3px var(--color-bg);
	}

	.handle:focus-visible::before {
		box-shadow: 0 0 0 3px var(--color-bg), 0 0 0 5px var(--handle-color);
	}

	.bars {
		display: flex;
		justify-content: center;
		gap: 1.25rem;
		width: 100%;
		flex-wrap: wrap;
		margin-top: -0.25rem;
	}

	.bar-col {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.25rem;
		min-width: 60px;
	}

	.bar-track {
		position: relative;
		width: 26px;
		height: 80px;
	}

	.bar-zero {
		position: absolute;
		left: 0;
		right: 0;
		top: 50%;
		height: 1px;
		background: var(--color-text);
		opacity: 0.3;
	}

	.bar-fill {
		position: absolute;
		left: 0;
		right: 0;
		background: var(--data-params);
		opacity: 0.55;
		transition: height 150ms ease-out, top 150ms ease-out, bottom 150ms ease-out;
	}

	.bar-fill.leading {
		opacity: 1;
	}

	.readout {
		font-family: var(--font-mono);
		color: var(--data-params);
		font-size: 0.8rem;
		opacity: 0.7;
	}

	.readout.leading {
		opacity: 1;
		font-weight: 700;
	}

	.cand-label {
		font-family: var(--font-mono);
		color: var(--color-text);
		font-size: 0.75rem;
		opacity: 0.75;
	}

	@media (prefers-reduced-motion: reduce) {
		.bar-fill {
			transition: none;
		}
	}
</style>
