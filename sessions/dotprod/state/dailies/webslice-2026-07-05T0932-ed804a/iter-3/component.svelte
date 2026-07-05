<script>
	// Turn the probe until the meter agrees.
	// Primary control: probeAngle, degrees, 0..360, step 5.
	// Auxiliary control: lengthC1, relative length of candidate c1, 0.5..2, step 0.1.
	let probeAngle = $state(40);
	let lengthC1 = $state(1);

	let svgEl = $state(null);

	// Square canvas, centered, sized with margin for the worst case (c1
	// stretched to 2x plus its label) at ANY angle, not just the driven
	// states, so nothing clips or crowds regardless of where the probe or
	// c1's length land.
	const VIEW = 400;
	const CENTER = 200;
	const R = 70;
	const MAX_SCORE = 2;
	const HEAD_LEN_RATIO = 0.2;
	const HEAD_WIDTH_RATIO = 0.11;
	const LABEL_RADIAL_OFFSET = 30;
	const PROBE_LABEL_TANGENT = 26;

	const baseCandidates = [
		{ name: 'c1', angle: 20 },
		{ name: 'c2', angle: 70 },
		{ name: 'c3', angle: 110 },
		{ name: 'c4', angle: 160 }
	];

	function toRad(deg) {
		return (deg * Math.PI) / 180;
	}

	function clamp(v, min, max) {
		return Math.min(max, Math.max(min, v));
	}

	// Shared geometry for every arrow (probe and candidates alike) so the
	// arrowhead-to-shaft proportion is identical everywhere: nothing is ever
	// bloated relative to its own length.
	function arrow(angleDeg, length) {
		const rad = toRad(angleDeg);
		const dirX = Math.cos(rad);
		const dirY = -Math.sin(rad);
		const shaft = R * length;
		const tipX = CENTER + dirX * shaft;
		const tipY = CENTER + dirY * shaft;
		const headLen = shaft * HEAD_LEN_RATIO;
		const halfWidth = shaft * HEAD_WIDTH_RATIO;
		const backX = tipX - dirX * headLen;
		const backY = tipY - dirY * headLen;
		const perpX = -dirY;
		const perpY = dirX;
		const leftX = backX + perpX * halfWidth;
		const leftY = backY + perpY * halfWidth;
		const rightX = backX - perpX * halfWidth;
		const rightY = backY - perpY * halfWidth;
		return {
			dirX,
			dirY,
			perpX,
			perpY,
			shaft,
			tipX,
			tipY,
			backX,
			backY,
			poly: `${tipX},${tipY} ${leftX},${leftY} ${rightX},${rightY}`
		};
	}

	let candidates = $derived(
		baseCandidates.map((c) => {
			const length = c.name === 'c1' ? lengthC1 : 1;
			const geo = arrow(c.angle, length);
			const labelDist = geo.shaft + LABEL_RADIAL_OFFSET;
			const labelX = CENTER + geo.dirX * labelDist;
			const labelY = CENTER + geo.dirY * labelDist;
			const diff = toRad(probeAngle - c.angle);
			const score = Math.cos(diff) * length;
			return { ...c, length, ...geo, labelX, labelY, score };
		})
	);

	let probeGeo = $derived.by(() => {
		const geo = arrow(probeAngle, 1);
		const labelDist = geo.shaft + LABEL_RADIAL_OFFSET;
		// Radial reach plus a fixed tangential kick: even when the probe
		// sits exactly on a candidate's line, the two label centers stay a
		// fixed distance apart, independent of angle.
		const labelX = CENTER + geo.dirX * labelDist + geo.perpX * PROBE_LABEL_TANGENT;
		const labelY = CENTER + geo.dirY * labelDist + geo.perpY * PROBE_LABEL_TANGENT;
		return { ...geo, labelX, labelY };
	});

	let probeHandlePos = $derived({
		x: (probeGeo.tipX / VIEW) * 100,
		y: (probeGeo.tipY / VIEW) * 100
	});

	let c1HandlePos = $derived.by(() => {
		const c1 = candidates.find((c) => c.name === 'c1');
		return { x: (c1.tipX / VIEW) * 100, y: (c1.tipY / VIEW) * 100 };
	});

	function roundScore(s) {
		let v = Math.round(s * 10) / 10;
		if (Object.is(v, -0)) v = 0;
		return v;
	}

	// A leader is crowned only when its rounded score strictly beats every
	// other rounded score. A tie for the top value suppresses the boost
	// everywhere, so no bar is ever falsely bolded as the leader.
	let leaderName = $derived.by(() => {
		const rounded = candidates.map((c) => roundScore(c.score));
		const max = Math.max(...rounded);
		const tiedCount = rounded.filter((r) => r === max).length;
		if (tiedCount > 1) return null;
		return candidates[rounded.indexOf(max)].name;
	});

	function screenToUser(e) {
		const rect = svgEl.getBoundingClientRect();
		const scaleX = VIEW / rect.width;
		const scaleY = VIEW / rect.height;
		return {
			x: (e.clientX - rect.left) * scaleX,
			y: (e.clientY - rect.top) * scaleY
		};
	}

	function angleFromPointer(e) {
		const p = screenToUser(e);
		const dx = p.x - CENTER;
		const dy = p.y - CENTER;
		let deg = (Math.atan2(-dy, dx) * 180) / Math.PI;
		if (deg < 0) deg += 360;
		return clamp(Math.round(deg), 0, 360);
	}

	function lengthFromPointer(e) {
		const p = screenToUser(e);
		const dx = p.x - CENTER;
		const dy = p.y - CENTER;
		const c1Rad = toRad(20);
		const dirX = Math.cos(c1Rad);
		const dirY = -Math.sin(c1Rad);
		const proj = dx * dirX + dy * dirY;
		const len = proj / R;
		return clamp(Math.round(len * 10) / 10, 0.5, 2);
	}

	function onProbePointerDown(e) {
		e.preventDefault();
		e.currentTarget.setPointerCapture(e.pointerId);
		probeAngle = angleFromPointer(e);
	}

	function onProbePointerMove(e) {
		if (e.buttons === 0) return;
		probeAngle = angleFromPointer(e);
	}

	function onProbePointerUp(e) {
		try {
			e.currentTarget.releasePointerCapture(e.pointerId);
		} catch (err) {
			/* no-op: capture may already be released */
		}
	}

	function onProbeKeydown(e) {
		let handled = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp') probeAngle = clamp(probeAngle + 5, 0, 360);
		else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') probeAngle = clamp(probeAngle - 5, 0, 360);
		else if (e.key === 'Home') probeAngle = 0;
		else if (e.key === 'End') probeAngle = 360;
		else handled = false;
		if (handled) e.preventDefault();
	}

	function onLengthPointerDown(e) {
		e.preventDefault();
		e.currentTarget.setPointerCapture(e.pointerId);
		lengthC1 = lengthFromPointer(e);
	}

	function onLengthPointerMove(e) {
		if (e.buttons === 0) return;
		lengthC1 = lengthFromPointer(e);
	}

	function onLengthPointerUp(e) {
		try {
			e.currentTarget.releasePointerCapture(e.pointerId);
		} catch (err) {
			/* no-op: capture may already be released */
		}
	}

	function onLengthKeydown(e) {
		let handled = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp')
			lengthC1 = clamp(Math.round((lengthC1 + 0.1) * 10) / 10, 0.5, 2);
		else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown')
			lengthC1 = clamp(Math.round((lengthC1 - 0.1) * 10) / 10, 0.5, 2);
		else if (e.key === 'Home') lengthC1 = 0.5;
		else if (e.key === 'End') lengthC1 = 2;
		else handled = false;
		if (handled) e.preventDefault();
	}
</script>

<div class="wrap" data-interactive="dot-alignment">
	<p class="instruction">Turn the probe until the meter agrees. Stretch c1's handle to see length cheat direction.</p>

	<div class="stage">
		<svg
			bind:this={svgEl}
			viewBox="0 0 {VIEW} {VIEW}"
			class="diagram"
			aria-label="An amber probe arrow rotates among four periwinkle candidate arrows named c1 through c4"
		>
			<circle cx={CENTER} cy={CENTER} r="3" fill="var(--color-text)" opacity="0.25" aria-hidden="true" />

			{#each candidates as c (c.name)}
				<line
					x1={CENTER}
					y1={CENTER}
					x2={c.backX}
					y2={c.backY}
					stroke="var(--data-observed)"
					stroke-width="2"
					stroke-linecap="round"
					opacity="0.85"
				/>
				<polygon points={c.poly} fill="var(--data-observed)" opacity="0.85" />
				<text
					x={c.labelX}
					y={c.labelY}
					class="arrow-label"
					text-anchor="middle"
					dominant-baseline="middle"
					aria-hidden="true">{c.name}</text
				>
			{/each}

			<line
				x1={CENTER}
				y1={CENTER}
				x2={probeGeo.backX}
				y2={probeGeo.backY}
				stroke="var(--data-heat)"
				stroke-width="3"
				stroke-linecap="round"
			/>
			<polygon points={probeGeo.poly} fill="var(--data-heat)" />
			<text
				x={probeGeo.labelX}
				y={probeGeo.labelY}
				class="arrow-label probe-label"
				text-anchor="middle"
				dominant-baseline="middle"
				aria-hidden="true">probe</text
			>
		</svg>

		<div
			class="handle probe-handle"
			style="left: {probeHandlePos.x}%; top: {probeHandlePos.y}%;"
			role="slider"
			tabindex="0"
			aria-label="probe angle in degrees"
			aria-valuemin="0"
			aria-valuemax="360"
			aria-valuenow={Math.round(probeAngle)}
			onpointerdown={onProbePointerDown}
			onpointermove={onProbePointerMove}
			onpointerup={onProbePointerUp}
			onkeydown={onProbeKeydown}
		></div>

		<div
			class="handle length-handle"
			style="left: {c1HandlePos.x}%; top: {c1HandlePos.y}%;"
			data-control="length-c1"
			role="spinbutton"
			tabindex="0"
			aria-label="c1 length"
			aria-valuemin="0.5"
			aria-valuemax="2"
			aria-valuenow={lengthC1.toFixed(1)}
			onpointerdown={onLengthPointerDown}
			onpointermove={onLengthPointerMove}
			onpointerup={onLengthPointerUp}
			onkeydown={onLengthKeydown}
		></div>
	</div>

	<div class="scores">
		{#each candidates as c (c.name)}
			{@const displayScore = roundScore(c.score).toFixed(1)}
			{@const isLeading = c.name === leaderName}
			<div class="score-col">
				<div class="bar-track">
					<div class="bar-zero" aria-hidden="true"></div>
					<div
						class="bar-fill"
						class:leading={isLeading}
						style="height: {Math.min(Math.abs(c.score), MAX_SCORE) / MAX_SCORE * 44}px; {c.score >= 0
							? 'bottom: 50%;'
							: 'top: 50%;'}"
					></div>
				</div>
				<span class="readout" class:leading={isLeading} aria-label="{c.name} score {displayScore}"
					>{displayScore}</span
				>
				<span class="cand-label" aria-hidden="true">{c.name}</span>
			</div>
		{/each}
	</div>
</div>

<style>
	.wrap {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1rem;
		width: 100%;
		max-width: 520px;
		margin: 0 auto;
		padding: 1.25rem 1rem;
		box-sizing: border-box;
		background: var(--color-bg);
	}

	.instruction {
		font-family: var(--font-body);
		color: var(--color-text);
		font-size: 0.9rem;
		opacity: 0.85;
		text-align: center;
		margin: 0;
	}

	.stage {
		position: relative;
		width: 100%;
		max-width: 360px;
		aspect-ratio: 1 / 1;
	}

	.diagram {
		width: 100%;
		height: 100%;
		display: block;
	}

	.arrow-label {
		font-family: var(--font-mono);
		fill: var(--color-text);
		font-size: 15px;
		pointer-events: none;
		user-select: none;
	}

	.handle {
		position: absolute;
		width: 48px;
		height: 48px;
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

	.probe-handle::before {
		content: '';
		width: 14px;
		height: 14px;
		border-radius: 50%;
		background: var(--data-heat);
		box-shadow: 0 0 0 3px var(--color-bg);
	}

	.length-handle::before {
		content: '';
		width: 12px;
		height: 12px;
		border-radius: 50%;
		background: var(--data-observed);
		box-shadow: 0 0 0 3px var(--color-bg);
	}

	.handle:focus-visible::before {
		box-shadow: 0 0 0 3px var(--color-bg), 0 0 0 5px currentColor;
	}

	.probe-handle:focus-visible::before {
		color: var(--data-heat);
	}

	.length-handle:focus-visible::before {
		color: var(--data-observed);
	}

	.scores {
		display: flex;
		justify-content: center;
		gap: 1.5rem;
		width: 100%;
		flex-wrap: wrap;
	}

	.score-col {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.3rem;
		min-width: 56px;
	}

	.bar-track {
		position: relative;
		width: 24px;
		height: 88px;
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
		border-radius: 2px;
		transition: height 150ms ease-out, top 150ms ease-out, bottom 150ms ease-out, opacity 150ms ease-out;
	}

	.bar-fill.leading {
		opacity: 1;
	}

	.readout {
		font-family: var(--font-mono);
		color: var(--data-params);
		font-size: 0.8rem;
		opacity: 0.65;
	}

	.readout.leading {
		opacity: 1;
		font-weight: 700;
	}

	.cand-label {
		font-family: var(--font-mono);
		color: var(--color-text);
		font-size: 0.75rem;
		opacity: 0.7;
	}

	@media (prefers-reduced-motion: reduce) {
		.bar-fill {
			transition: none;
		}
	}
</style>
