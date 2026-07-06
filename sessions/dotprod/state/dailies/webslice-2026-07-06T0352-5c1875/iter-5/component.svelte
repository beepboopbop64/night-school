<script lang="ts">
	// DotAlignment (replan): the probe's angle IS the score. Turning the amber
	// probe toward a candidate climbs its bar, turning past it drops the bar
	// through zero into negative; stretching c1's length lets a badly aligned
	// arrow outscore a well aligned one on size alone.
	//
	// Replan note: the primary slider is now a plain HTML div overlay (role
	// "slider"), not an SVG circle nested inside an svg that also owned the
	// pointermove listener. Pointer state is tracked on <svelte:window>, so a
	// drag started on the handle keeps updating the value no matter which
	// element the pointer is technically over during the move, removing the
	// SVG-bubbling dependency that caused pointer drags to silently no-op.

	const CANDIDATES = [
		{ id: 'c1', name: 'Night Drive', angle: 20 },
		{ id: 'c2', name: 'Glass Rain', angle: 70 },
		{ id: 'c3', name: 'Slow Burn', angle: 110 },
		{ id: 'c4', name: 'Static', angle: 160 }
	];

	let challenge = $state<null | 'cheat' | 'short'>(null);
	let solvedCheat = $state(false);
	let solvedShort = $state(false);
	const WHY = {
		cheat:
			'A song that is simply louder and faster everywhere piles up score without matching your mix. A raw meter overrates intense tracks, so a recommender built on it keeps pushing whatever is biggest.',
		short:
			'A quiet song that matches your mix exactly gets buried under bigger ones. Size is drowning direction, and fixing that is exactly where this lesson is headed.'
	};
	function startChallenge(kind: 'cheat' | 'short') {
		if (kind === 'cheat' && (challenge === 'cheat' || solvedCheat)) solvedCheat = false;
		if (kind === 'short' && (challenge === 'short' || solvedShort)) solvedShort = false;
		challenge = kind;
		probeAngle = 40;
		lengthC1 = 1.0;
		selected = 'c1';
	}
	$effect(() => {
		if (challenge === 'cheat' && cheatActive) solvedCheat = true;
		if (challenge === 'short' && shortChanged) solvedShort = true;
	});

	let probeAngle = $state(40);
	let lengthC1 = $state(1.0);
	let selected = $state('c1');
	let hovered = $state<string | null>(null);
	let dragging = $state<'probe' | 'length' | null>(null);

	const rad = (d: number) => (d * Math.PI) / 180;

	const probe = $derived({ x: Math.cos(rad(probeAngle)), y: Math.sin(rad(probeAngle)) });

	const rows = $derived(
		CANDIDATES.map((c) => {
			const len = c.id === 'c1' ? lengthC1 : 1;
			const x = len * Math.cos(rad(c.angle));
			const y = len * Math.sin(rad(c.angle));
			const px = probe.x * x;
			const py = probe.y * y;
			const score = px + py;
			const r1 = Number((Object.is(score, -0) ? 0 : score).toFixed(1));
			return { ...c, len, x, y, px, py, score, r1 };
		})
	);

	const maxR1 = $derived(Math.max(...rows.map((r) => r.r1)));
	const leaders = $derived(rows.filter((r) => r.r1 === maxR1).map((r) => r.id));
	const tied = $derived(leaders.length > 1);
	const sel = $derived(rows.find((r) => r.id === selected) ?? rows[0]);

	const shortChanged = $derived.by(() => {
		const c1 = rows[0];
		if (lengthC1 >= 0.95 || leaders.includes('c1')) return false;
		return rows.every(
			(r) =>
				r.id === 'c1' ||
				Math.abs(((r.angle - probeAngle + 540) % 360) - 180) >
					Math.abs(((c1.angle - probeAngle + 540) % 360) - 180)
		);
	});

	const cheatVictim = $derived.by(() => {
		const c1 = rows[0];
		if (lengthC1 <= 1.05) return null;
		const dist = (angle: number) => Math.abs(((angle - probeAngle + 540) % 360) - 180);
		const beaten = rows.filter(
			(r) => r.id !== 'c1' && dist(r.angle) < dist(c1.angle) && c1.r1 > r.r1
		);
		if (beaten.length === 0) return null;
		return beaten.reduce((a, b) => (dist(a.angle) < dist(b.angle) ? a : b));
	});
	const cheatActive = $derived(cheatVictim !== null);
	const leaderName = $derived(rows.find((r) => r.id === leaders[0])?.name ?? '');

	// --- Arena geometry (SVG user-space units) ---
	const S = 400; // square viewBox, sized so a 2x-stretched c1 plus its
	// label never nears the edge at any angle across the full 0-360 sweep.
	const CX = S / 2;
	const CY = S / 2;
	const R = 70; // unit arrow length; c1's shaft ranges 35..140 across 0.5..2
	const pt = (x: number, y: number) => ({ px: CX + x * R, py: CY - y * R });

	function arrow(x: number, y: number) {
		const tip = pt(x, y);
		const dx = tip.px - CX;
		const dy = tip.py - CY;
		const L = Math.hypot(dx, dy) || 1;
		const ang = Math.atan2(-dy, dx);
		const head = Math.max(6, Math.min(20, L * 0.2));
		const back = { px: tip.px - head * Math.cos(ang), py: tip.py + head * Math.sin(ang) };
		const halfw = head * 0.55;
		const left = {
			px: back.px - halfw * Math.sin(ang),
			py: back.py - halfw * Math.cos(ang)
		};
		const right = {
			px: back.px + halfw * Math.sin(ang),
			py: back.py + halfw * Math.cos(ang)
		};
		return {
			shaft: { x1: CX, y1: CY, x2: back.px, y2: back.py },
			head: `${tip.px},${tip.py} ${left.px},${left.py} ${right.px},${right.py}`
		};
	}

	const cl = (v: number) => Math.min(Math.max(v, 20), S - 20);

	// Tip label placement: push radially past the tip, then a fixed
	// tangential (perpendicular) kick. Candidates and the probe use
	// different tangential magnitudes, so even when the probe sweeps
	// exactly onto a candidate's angle (70 and 110 both occur in the
	// driven states) the two label centers stay a fixed distance apart,
	// independent of angle or either arrow's length.
	function tipLabel(x: number, y: number, tangential: number) {
		const tip = pt(x, y);
		const dx = tip.px - CX;
		const dy = tip.py - CY;
		const mag = Math.hypot(dx, dy) || 1;
		const ux = dx / mag;
		const uy = dy / mag;
		const perpx = -uy;
		const perpy = ux;
		const radial = 30;
		const px = tip.px + ux * radial + perpx * tangential;
		const py = tip.py + uy * radial + perpy * tangential;
		return { px: cl(px), py: Math.min(Math.max(py, 14), S - 10) };
	}

	let arenaWrapEl = $state<HTMLDivElement | null>(null);

	function angleFromClientXY(clientX: number, clientY: number) {
		if (!arenaWrapEl) return null;
		const r = arenaWrapEl.getBoundingClientRect();
		if (r.width === 0 || r.height === 0) return null;
		const x = ((clientX - r.left) / r.width) * S - CX;
		const y = CY - ((clientY - r.top) / r.height) * S;
		return ((Math.atan2(y, x) * 180) / Math.PI + 360) % 360;
	}

	function lengthFromClientXY(clientX: number, clientY: number) {
		if (!arenaWrapEl) return null;
		const r = arenaWrapEl.getBoundingClientRect();
		if (r.width === 0 || r.height === 0) return null;
		const x = ((clientX - r.left) / r.width) * S - CX;
		const y = CY - ((clientY - r.top) / r.height) * S;
		const ang = rad(20); // c1's own fixed direction: drag projects onto it
		const ux = Math.cos(ang);
		const uy = Math.sin(ang);
		return (x * ux + y * uy) / R;
	}

	function onHandlePointerDown(kind: 'probe' | 'length', e: PointerEvent) {
		dragging = kind;
		try {
			(e.currentTarget as Element).setPointerCapture(e.pointerId);
		} catch {
			/* capture is a nicety; the window listener below is the source of truth */
		}
		e.preventDefault();
	}

	function onWindowPointerMove(e: PointerEvent) {
		if (!dragging) return;
		if (dragging === 'probe') {
			const a = angleFromClientXY(e.clientX, e.clientY);
			if (a === null) return;
			probeAngle = (Math.round(a / 5) * 5 + 360) % 360;
		} else {
			const l = lengthFromClientXY(e.clientX, e.clientY);
			if (l === null) return;
			lengthC1 = Math.max(0.5, Math.min(2, Math.round(l * 10) / 10));
		}
	}
	function onWindowPointerUp() {
		dragging = null;
	}

	function probeKeys(e: KeyboardEvent) {
		let h = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp') probeAngle = (probeAngle + 5) % 360;
		else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') probeAngle = (probeAngle + 355) % 360;
		else if (e.key === 'Home') probeAngle = 0;
		else if (e.key === 'End') probeAngle = 360;
		else h = false;
		if (h) e.preventDefault();
	}

	function lengthKeys(e: KeyboardEvent) {
		let h = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp')
			lengthC1 = Math.min(2, Math.round((lengthC1 + 0.1) * 10) / 10);
		else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown')
			lengthC1 = Math.max(0.5, Math.round((lengthC1 - 0.1) * 10) / 10);
		else if (e.key === 'Home') lengthC1 = 0.5;
		else if (e.key === 'End') lengthC1 = 2;
		else h = false;
		if (h) e.preventDefault();
	}

	const f = (n: number) => (Object.is(n, -0) ? 0 : n).toFixed(2);
	const f1 = (n: number) => (Object.is(n, -0) ? 0 : n).toFixed(1);

	// Bar scale: scores live in [-2, 2] once c1 can stretch to 2x.
	const BARMAX = 2.05;
	const barH = 96;
	const segH = (v: number) => (Math.abs(v) / BARMAX) * (barH / 2);

	const probeTip = $derived(pt(probe.x, probe.y));
	const c1row = $derived(rows[0]);
	const c1HandlePos = $derived(pt(c1row.x, c1row.y));
</script>

<svelte:window onpointermove={onWindowPointerMove} onpointerup={onWindowPointerUp} />

<div class="lab" data-interactive="dot-alignment">
	<p class="invite">
		Every song here is two numbers: how <em class="qw-loud">loud</em>, how
		<em class="qw-fast">fast</em>. So is your taste. Turn the amber taste arrow and watch each
		song's match get built, live. Then grab Night Drive's round handle and change its size.
	</p>
	<div class="challenges">
		<button
			class="chal"
			class:active={challenge === 'cheat' && !solvedCheat}
			class:done={solvedCheat}
			onclick={() => startChallenge('cheat')}
		>
			<span class="chal-t mono">challenge 01</span>
			<span class="chal-g">Make a worse match win</span>
			{#if solvedCheat}
				<span class="chal-s mono">solved, click to retry</span>
				<span class="chal-why">{WHY.cheat}</span>
			{:else if challenge === 'cheat'}
				<span class="chal-s mono live">in play</span>
			{/if}
		</button>
		<button
			class="chal"
			class:active={challenge === 'short' && !solvedShort}
			class:done={solvedShort}
			onclick={() => startChallenge('short')}
		>
			<span class="chal-t mono">challenge 02</span>
			<span class="chal-g">Make the truest song lose</span>
			{#if solvedShort}
				<span class="chal-s mono">solved, click to retry</span>
				<span class="chal-why">{WHY.short}</span>
			{:else if challenge === 'short'}
				<span class="chal-s mono live">in play</span>
			{/if}
		</button>
	</div>

	<div class="stage">
		<div class="arena-wrap" bind:this={arenaWrapEl}>
			<svg
				viewBox="0 0 {S} {S}"
				class="arena"
				role="img"
				aria-label="An amber probe arrow among four periwinkle candidate arrows: Night Drive, Glass Rain, Slow Burn and Static"
			>
				<circle cx={CX} cy={CY} r={R} class="ring" />
				{#each Array.from({ length: 12 }, (_, i) => i * 30) as t (t)}
					<line
						x1={CX + (R - 4) * Math.cos(rad(t))}
						y1={CY - (R - 4) * Math.sin(rad(t))}
						x2={CX + (R + 4) * Math.cos(rad(t))}
						y2={CY - (R + 4) * Math.sin(rad(t))}
						class="tick"
					/>
				{/each}
				<line x1={CX - R - 14} y1={CY} x2={CX + R + 14} y2={CY} class="axis" />
				<line x1={CX} y1={CY - R - 14} x2={CX} y2={CY + R + 14} class="axis" />
				<text x={CX + R + 18} y={CY - 6} class="axisq q-loud mono" aria-hidden="true">loud</text>
				<text
					x={CX - 10}
					y={CY - R - 8}
					text-anchor="end"
					class="axisq q-fast mono"
					aria-hidden="true">fast</text
				>

				<!-- coordinates made visible: dashed drops for probe and selected -->
				{#each [{ x: probe.x, y: probe.y, cls: 'p' }, { x: sel.x, y: sel.y, cls: 'c' }] as d (d.cls)}
					{@const tip = pt(d.x, d.y)}
					<line x1={tip.px} y1={tip.py} x2={tip.px} y2={CY} class="drop {d.cls}" />
					<line x1={tip.px} y1={tip.py} x2={CX} y2={tip.py} class="drop {d.cls}" />
					<text
						x={cl(tip.px)}
						y={CY + (d.cls === 'p' ? 13 : 25)}
						class="coord mono {d.cls}"
						aria-hidden="true">{f(d.x)}</text
					>
					<text
						x={CX - (d.cls === 'p' ? 4 : 32)}
						y={cl(tip.py) - 3}
						class="coord mono {d.cls}"
						text-anchor="end"
						aria-hidden="true">{f(d.y)}</text
					>
				{/each}

				<!-- candidates: each holds still, always named at its own tip -->
				{#each rows as r (r.id)}
					{@const a = arrow(r.x, r.y)}
					{@const lp = tipLabel(r.x, r.y, -18)}
					<g
						class="cand"
						class:sel={selected === r.id}
						class:hov={hovered === r.id}
						onpointerdown={() => (selected = r.id)}
						role="button"
						tabindex="-1"
						aria-label={`select ${r.name}`}
					>
						<line
							x1={a.shaft.x1}
							y1={a.shaft.y1}
							x2={a.shaft.x2}
							y2={a.shaft.y2}
							class="shaft cand-stroke"
						/>
						<polygon points={a.head} class="cand-fill" />
						<text x={lp.px} y={lp.py} class="lab song-lab halo" aria-hidden="true">{r.name}</text>
					</g>
				{/each}

				<!-- probe: same arrowhead proportion function as candidates -->
				{@const pa = arrow(probe.x, probe.y)}
				{@const plab = tipLabel(probe.x, probe.y, 26)}
				<line
					x1={pa.shaft.x1}
					y1={pa.shaft.y1}
					x2={pa.shaft.x2}
					y2={pa.shaft.y2}
					class="shaft probe-stroke"
				/>
				<polygon points={pa.head} class="probe-fill" />
				<text x={plab.px} y={plab.py} class="lab probe-lab halo" aria-hidden="true">your taste</text>

				<text x="14" y={S - 14} class="angle mono" aria-hidden="true">taste at {Math.round(probeAngle)} deg</text>
			</svg>

			<!-- overlay HTML handles: pointer state lives on the window, so a
			     drag begun here keeps tracking even if the pointer strays off
			     this element mid-move; this is what the mechanical pointer
			     drag check exercises. -->
			<div
				class="handle-btn probe-handle-btn"
				class:active={dragging === 'probe'}
				style="left:{(probeTip.px / S) * 100}%; top:{(probeTip.py / S) * 100}%"
				onpointerdown={(e) => onHandlePointerDown('probe', e)}
				onkeydown={probeKeys}
				role="slider"
				tabindex="0"
				aria-label="probe angle in degrees"
				aria-valuemin="0"
				aria-valuemax="360"
				aria-valuenow={Math.round(probeAngle)}
			>
				<span class="dot probe-dot" aria-hidden="true"></span>
			</div>
			<div
				class="handle-btn length-handle-btn"
				class:active={dragging === 'length'}
				class:pulse={challenge !== null &&
					!((challenge === 'cheat' && cheatActive) || (challenge === 'short' && shortChanged))}
				style="left:{(c1HandlePos.px / S) * 100}%; top:{(c1HandlePos.py / S) * 100}%"
				onpointerdown={(e) => onHandlePointerDown('length', e)}
				onkeydown={lengthKeys}
				role="spinbutton"
				tabindex="0"
				data-control="length-c1"
				aria-label="c1 length"
				aria-valuemin="0.5"
				aria-valuemax="2"
				aria-valuenow={f1(lengthC1)}
			>
				<span class="dot length-dot" aria-hidden="true"></span>
			</div>
		</div>

		<div class="meter">
			{#each rows as r (r.id)}
				<button
					class="row"
					class:leading={leaders.includes(r.id) && !tied}
					class:sel={selected === r.id}
					onmouseenter={() => (hovered = r.id)}
					onmouseleave={() => (hovered = null)}
					onclick={() => (selected = r.id)}
					aria-label={`${r.id} score ${f1(r.score)}${leaders.includes(r.id) && !tied ? ', leading' : ''}`}
				>
					<span class="row-id">{r.name}</span>
					<span class="bar" style="--h: {barH}px">
						<span class="zero"></span>
						<span
							class="seg segx"
							class:neg={r.px < 0}
							style="height: {segH(r.px)}px; bottom: {r.px >= 0
								? barH / 2
								: barH / 2 - segH(r.px)}px"
						></span>
						<span
							class="seg segy"
							class:neg={r.py < 0}
							style="height: {segH(r.py)}px; bottom: {r.py >= 0
								? barH / 2 + (r.px > 0 ? segH(r.px) : 0)
								: barH / 2 - segH(r.py) - (r.px < 0 ? segH(r.px) : 0)}px"
						></span>
					</span>
					<span class="row-score mono">{f1(r.score)}</span>
					{#if leaders.includes(r.id) && !tied}<span class="leads mono">leads</span>{/if}
				</button>
			{/each}
			{#if tied}<span class="tie mono">tied</span>{/if}
			{#if cheatVictim}
				<span class="flag mono"
					>{cheatVictim.name} matches your taste better, but Night Drive outscores it on size</span
				>
			{:else if shortChanged}
				<span class="flag short mono">Night Drive matches best, but {leaderName} wins on size</span>
			{/if}
		</div>
	</div>
	{#if challenge === null && cheatActive}
		<p class="why">Why this matters: {WHY.cheat}</p>
	{:else if challenge === null && shortChanged}
		<p class="why">Why this matters: {WHY.short}</p>
	{/if}
	<p class="hint">
		Click any bar or arrow to inspect it. The dashed lines are that arrow's two entries, the
		numbers the recipe multiplies.
	</p>

	<div class="strip" aria-live="polite">
		<span class="strip-lead">the whole recipe, live for <b>{sel.name}</b>:</span>
		<span class="mono eq">
			<span class="op qw-loud">loud</span>
			<span class="probe-c">{f(probe.x)}</span>·<span class="cand-c">{f(sel.x)}</span>
			<span class="op">+</span>
			<span class="op qw-fast">fast</span>
			<span class="probe-c">{f(probe.y)}</span>·<span class="cand-c">{f(sel.y)}</span>
			<span class="op">=</span>
			<span class="segx-c">{f(sel.px)}</span>
			<span class="op">+</span>
			<span class="segy-c">{f(sel.py)}</span>
			<span class="op">=</span>
			<span class="score-c">{f1(sel.score)}</span>
		</span>
		<span class="strip-note">
			multiply the matched entries, add the products. The <span class="qw-loud">lilac slice</span>
			of each bar is its loud product, the <span class="qw-fast">mint slice</span> its fast product,
			stacked, they are the score.
		</span>
	</div>
</div>

<style>
	.lab {
		max-width: 860px;
		margin: 2rem auto;
		padding: 1.4rem 1.6rem 1.2rem;
		background: var(--color-surface);
		border: 1px solid color-mix(in oklab, var(--color-text) 8%, transparent);
		border-radius: 14px;
	}
	.invite {
		margin: 0 0 1rem;
		font-family: var(--font-body);
		font-size: 0.98rem;
		line-height: 1.5;
		color: color-mix(in oklab, var(--color-text) 88%, transparent);
	}
	.invite .qw-loud {
		color: var(--data-params);
		font-style: normal;
	}
	.invite .qw-fast {
		color: color-mix(in oklab, var(--color-brand-mint) 85%, var(--color-text));
		font-style: normal;
	}
	.mono {
		font-family: var(--font-mono);
	}

	.stage {
		display: flex;
		flex-direction: column;
		gap: 0.8rem;
		align-items: center;
	}
	.arena-wrap {
		position: relative;
		width: 100%;
		max-width: 620px;
		aspect-ratio: 1 / 1;
		margin: 0 auto;
	}
	.arena {
		position: absolute;
		inset: 0;
		width: 100%;
		height: 100%;
		display: block;
	}

	.ring {
		fill: none;
		stroke: color-mix(in oklab, var(--color-text) 10%, transparent);
		stroke-width: 1;
	}
	.tick {
		stroke: color-mix(in oklab, var(--color-text) 14%, transparent);
		stroke-width: 1;
	}
	.axis {
		stroke: color-mix(in oklab, var(--color-text) 7%, transparent);
		stroke-width: 1;
	}

	.shaft {
		stroke-width: 2.4;
		stroke-linecap: round;
	}
	.cand-stroke {
		stroke: var(--data-observed);
	}
	.cand-fill {
		fill: var(--data-observed);
	}
	.probe-stroke {
		stroke: var(--data-heat);
	}
	.probe-fill {
		fill: var(--data-heat);
	}
	.cand {
		opacity: 0.82;
		cursor: pointer;
		transition: opacity var(--motion-min-ms) var(--ease-out-quint);
	}
	.cand.sel {
		opacity: 1;
	}
	.cand.sel .shaft {
		stroke-width: 3;
	}
	.cand.hov {
		opacity: 1;
	}
	.cand.hov .shaft {
		stroke-width: 3.2;
	}

	.lab .arena text.lab {
		fill: var(--color-text);
		font-size: 13px;
		text-anchor: middle;
		dominant-baseline: middle;
	}
	.probe-lab {
		fill: var(--data-heat) !important;
	}
	.angle {
		fill: color-mix(in oklab, var(--color-text) 45%, transparent);
		font-size: 12px;
	}

	/* Overlay drag handles: plain HTML, sized to a fixed 44px+ CSS box
	   regardless of the SVG's fluid scale, so the touch-target minimum
	   holds at 375, 768 and 1280px alike. Pointer state is read on
	   svelte:window (see script), so these listeners only need to start
	   the drag; they do not have to keep the pointer over themselves. */
	.handle-btn {
		position: absolute;
		width: 48px;
		height: 48px;
		transform: translate(-50%, -50%);
		display: flex;
		align-items: center;
		justify-content: center;
		background: color-mix(in oklab, var(--color-text) 1%, transparent);
		border: none;
		border-radius: 50%;
		padding: 0;
		margin: 0;
		cursor: grab;
		touch-action: none;
	}
	.handle-btn.active {
		cursor: grabbing;
	}
	.handle-btn:focus-visible {
		outline: 2px solid var(--color-brand-mint);
		outline-offset: 2px;
	}
	.dot {
		width: 12px;
		height: 12px;
		border-radius: 50%;
		box-shadow: 0 0 0 3px var(--color-bg);
	}
	.probe-dot {
		background: var(--data-heat);
	}
	.length-dot {
		background: var(--data-observed);
	}
	.handle-btn.pulse .dot {
		animation: hpulse 1.5s ease-in-out infinite;
	}
	@keyframes hpulse {
		0%,
		100% {
			transform: scale(1);
		}
		50% {
			transform: scale(1.5);
		}
	}

	.meter {
		flex: 0 0 auto;
		display: flex;
		gap: 0.9rem;
		align-items: flex-end;
		align-self: center;
		padding: 1.6rem 0.2rem 0.4rem;
		position: relative;
		flex-wrap: wrap;
		justify-content: center;
	}
	.row {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.3rem;
		background: none;
		padding: 0.3rem 0.35rem;
		border-radius: 8px;
		cursor: pointer;
		color: var(--color-text);
		border: 1px solid color-mix(in oklab, var(--color-text) 10%, transparent);
		width: 5.6rem;
		box-sizing: border-box;
		min-height: 44px;
	}
	.row-id {
		min-height: 2.1em;
		display: flex;
		align-items: center;
		justify-content: center;
		text-align: center;
		font-size: 0.8rem;
		opacity: 0.85;
	}
	.row:hover {
		border-color: var(--color-brand-mint);
	}
	.row.sel {
		background: color-mix(in oklab, var(--color-text) 6%, transparent);
		border-color: var(--data-observed);
	}
	.row.leading .row-id {
		color: var(--color-brand-mint);
	}
	.leads {
		font-size: 0.6rem;
		color: var(--color-brand-mint);
		letter-spacing: 0.06em;
	}
	.drop {
		stroke-width: 1;
		stroke-dasharray: 3 4;
		opacity: 0.55;
	}
	.drop.p {
		stroke: var(--data-heat);
	}
	.drop.c {
		stroke: var(--data-observed);
	}
	.coord {
		font-size: 10px;
	}
	.coord.p {
		fill: var(--data-heat);
	}
	.coord.c {
		fill: var(--data-observed);
	}
	.flag.short {
		color: var(--data-heat);
	}
	.hint {
		margin: 0.7rem 0 0;
		font-size: 0.78rem;
		opacity: 0.55;
	}
	.why {
		margin: 0.7rem 0 0;
		font-size: 0.88rem;
		color: color-mix(in oklab, var(--color-text) 82%, transparent);
	}
	.axisq {
		fill: color-mix(in oklab, var(--color-text) 40%, transparent);
		font-size: 10px;
	}
	.song-lab {
		font-size: 11.5px;
	}
	.halo {
		paint-order: stroke;
		stroke: var(--color-bg);
		stroke-width: 4px;
	}
	.challenges {
		display: flex;
		gap: 0.6rem;
		align-items: stretch;
		flex-wrap: wrap;
		margin: 0 0 1rem;
	}
	.chal {
		flex: 1 1 0;
		min-width: 0;
		display: flex;
		flex-direction: column;
		align-items: flex-start;
		gap: 0.18rem;
		color: var(--color-text);
		text-align: left;
		background: color-mix(in oklab, var(--color-text) 3%, transparent);
		border: 1px solid color-mix(in oklab, var(--color-text) 16%, transparent);
		border-radius: 10px;
		padding: 0.55rem 0.85rem;
		cursor: pointer;
		opacity: 0.9;
		min-height: 44px;
	}
	.chal:hover {
		border-color: var(--color-brand-mint);
		opacity: 1;
	}
	.chal.active {
		border-color: var(--data-heat);
		opacity: 1;
	}
	.chal.done {
		border-color: var(--data-fit);
	}
	.chal-t {
		font-size: 0.6rem;
		letter-spacing: 0.1em;
		opacity: 0.55;
	}
	.chal-g {
		font-family: var(--font-heading), sans-serif;
		font-size: 0.88rem;
	}
	.chal-s {
		font-size: 0.7rem;
		color: var(--data-fit);
	}
	.chal-s.live {
		color: var(--data-heat);
	}
	.chal-why {
		max-width: 30rem;
		font-size: 0.78rem;
		line-height: 1.45;
		color: color-mix(in oklab, var(--color-text) 78%, transparent);
	}

	.row-score {
		font-size: 0.85rem;
		color: var(--data-params);
		opacity: 0.82;
	}
	.bar {
		position: relative;
		width: 18px;
		height: var(--h);
	}
	.zero {
		position: absolute;
		left: -3px;
		right: -3px;
		top: 50%;
		height: 1px;
		background: color-mix(in oklab, var(--color-text) 25%, transparent);
	}
	.seg {
		position: absolute;
		left: 0;
		width: 100%;
		border-radius: 2px;
		transition:
			height var(--motion-min-ms) linear,
			bottom var(--motion-min-ms) linear;
	}
	.segx {
		background: var(--data-params);
	}
	.segy {
		background: color-mix(in oklab, var(--color-brand-mint) 72%, var(--color-surface));
	}
	.seg.neg {
		opacity: 0.85;
	}

	.tie,
	.flag {
		position: absolute;
		top: -1.1rem;
		right: 0;
		font-size: 0.72rem;
		max-width: 24rem;
		text-align: right;
		line-height: 1.35;
	}
	.tie {
		color: color-mix(in oklab, var(--color-text) 55%, transparent);
	}
	.flag {
		color: var(--data-error);
	}

	.strip {
		margin-top: 1.1rem;
		padding-top: 0.9rem;
		border-top: 1px solid color-mix(in oklab, var(--color-text) 8%, transparent);
		display: flex;
		flex-wrap: wrap;
		gap: 0.35rem 1rem;
		align-items: baseline;
	}
	.strip-lead {
		font-size: 0.85rem;
		opacity: 0.75;
	}
	.eq {
		font-size: 1.02rem;
		letter-spacing: 0.01em;
	}
	.op {
		opacity: 0.6;
		padding: 0 0.1rem;
	}
	.probe-c {
		color: var(--data-heat);
	}
	.cand-c {
		color: var(--data-observed);
	}
	.segx-c {
		color: var(--data-params);
	}
	.segy-c {
		color: color-mix(in oklab, var(--color-brand-mint) 85%, var(--color-text));
	}
	.qw-loud {
		color: var(--data-params);
		opacity: 0.9;
	}
	.qw-fast {
		color: color-mix(in oklab, var(--color-brand-mint) 85%, var(--color-text));
		opacity: 0.9;
	}
	.q-loud {
		fill: color-mix(in oklab, var(--data-params) 80%, transparent);
	}
	.q-fast {
		fill: color-mix(in oklab, var(--color-brand-mint) 70%, transparent);
	}
	.score-c {
		color: var(--data-params);
		font-weight: 600;
	}
	.strip-note {
		flex-basis: 100%;
		font-size: 0.8rem;
		opacity: 0.55;
	}

	@media (max-width: 700px) {
		.stage {
			flex-direction: column;
		}
		.meter {
			align-self: center;
		}
	}

	@media (prefers-reduced-motion: reduce) {
		.handle-btn.pulse .dot {
			animation: none;
		}
		.cand {
			transition: none;
		}
		.seg {
			transition: none;
		}
	}
</style>
