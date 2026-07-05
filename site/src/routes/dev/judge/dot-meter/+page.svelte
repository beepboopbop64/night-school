<script lang="ts">
	// DotMeter v2 — the judge's hand-built take, for direct iteration with Jake.
	// The design thesis: multiply-and-add should be VISIBLE, not narrated.
	// Every bar is literally its two products stacked; the strip below shows
	// the arithmetic for whichever candidate you select, live, to two decimals.

	const CANDIDATES = [
		{ id: 'c1', angle: 20 },
		{ id: 'c2', angle: 70 },
		{ id: 'c3', angle: 110 },
		{ id: 'c4', angle: 160 }
	];

	let probeAngle = $state(40);
	let lengthC1 = $state(1.0);
	let selected = $state('c1');
	let dragging = $state<'probe' | 'length' | null>(null);

	const rad = (d: number) => (d * Math.PI) / 180;

	const probe = $derived({ x: Math.cos(rad(probeAngle)), y: Math.sin(rad(probeAngle)) });

	const rows = $derived(
		CANDIDATES.map((c) => {
			const len = c.id === 'c1' ? lengthC1 : 1;
			const x = len * Math.cos(rad(c.angle));
			const y = len * Math.sin(rad(c.angle));
			const px = probe.x * x; // the x-term product
			const py = probe.y * y; // the y-term product
			return { ...c, len, x, y, px, py, score: px + py };
		})
	);

	const maxScore = $derived(Math.max(...rows.map((r) => r.score)));
	const leaders = $derived(rows.filter((r) => Math.abs(r.score - maxScore) < 0.005).map((r) => r.id));
	const tied = $derived(leaders.length > 1);
	const sel = $derived(rows.find((r) => r.id === selected) ?? rows[0]);

	// The overtake: c1 stretched AND leading over a candidate that out-aligns it.
	const cheatActive = $derived.by(() => {
		const c1 = rows[0];
		if (lengthC1 <= 1.05) return false;
		return rows.some(
			(r) =>
				r.id !== 'c1' &&
				Math.abs(((r.angle - probeAngle + 540) % 360) - 180) <
					Math.abs(((c1.angle - probeAngle + 540) % 360) - 180) &&
				c1.score > r.score + 0.005
		);
	});

	// --- Arena geometry (SVG units) ---
	const S = 340; // viewBox square
	const CX = S / 2;
	const CY = S / 2;
	const R = 118; // unit arrow length in px
	const pt = (x: number, y: number) => ({ px: CX + x * R, py: CY - y * R });

	function arrow(x: number, y: number) {
		const tip = pt(x, y);
		const ang = Math.atan2(CY - tip.py, tip.px - CX);
		const L = Math.hypot(tip.px - CX, tip.py - CY);
		const head = Math.max(7, Math.min(11, L * 0.09));
		const back = { px: tip.px - head * Math.cos(ang), py: tip.py + head * Math.sin(ang) };
		const left = {
			px: back.px - head * 0.55 * Math.sin(ang),
			py: back.py - head * 0.55 * Math.cos(ang)
		};
		const right = {
			px: back.px + head * 0.55 * Math.sin(ang),
			py: back.py + head * 0.55 * Math.cos(ang)
		};
		return {
			shaft: { x1: CX, y1: CY, x2: back.px, y2: back.py },
			head: `${tip.px},${tip.py} ${left.px},${left.py} ${right.px},${right.py}`
		};
	}

	function labelPos(angle: number, len: number, pad = 20) {
		const d = len * R + pad;
		return { px: CX + d * Math.cos(rad(angle)), py: CY - d * Math.sin(rad(angle)) };
	}

	let arenaEl = $state<SVGSVGElement | null>(null);

	function anglesFromEvent(e: PointerEvent) {
		if (!arenaEl) return null;
		const r = arenaEl.getBoundingClientRect();
		const x = ((e.clientX - r.left) / r.width) * S - CX;
		const y = CY - ((e.clientY - r.top) / r.height) * S;
		return { angle: ((Math.atan2(y, x) * 180) / Math.PI + 360) % 360, dist: Math.hypot(x, y) / R };
	}

	function onArenaPointer(e: PointerEvent) {
		const a = anglesFromEvent(e);
		if (!a || !dragging) return;
		if (dragging === 'probe') probeAngle = Math.round(a.angle / 5) * 5 % 360;
		else lengthC1 = Math.max(0.5, Math.min(2, Math.round(a.dist * 10) / 10));
	}

	function startDrag(kind: 'probe' | 'length', e: PointerEvent) {
		dragging = kind;
		(e.currentTarget as Element).setPointerCapture(e.pointerId);
	}

	function probeKeys(e: KeyboardEvent) {
		let h = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp') probeAngle = (probeAngle + 5) % 360;
		else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') probeAngle = (probeAngle + 355) % 360;
		else h = false;
		if (h) e.preventDefault();
	}

	function lengthKeys(e: KeyboardEvent) {
		let h = true;
		if (e.key === 'ArrowRight' || e.key === 'ArrowUp') lengthC1 = Math.min(2, Math.round((lengthC1 + 0.1) * 10) / 10);
		else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') lengthC1 = Math.max(0.5, Math.round((lengthC1 - 0.1) * 10) / 10);
		else h = false;
		if (h) e.preventDefault();
	}

	const f = (n: number) => (Object.is(n, -0) ? 0 : n).toFixed(2);
	const f1 = (n: number) => (Object.is(n, -0) ? 0 : n).toFixed(1);

	// Bar scale: scores live in [-2, 2] once c1 can stretch.
	const BARMAX = 2.05;
	const barH = 92;
	const segH = (v: number) => (Math.abs(v) / BARMAX) * (barH / 2);

	const probeTip = $derived(pt(probe.x, probe.y));
	const c1row = $derived(rows[0]);
	const c1HandlePos = $derived(pt(c1row.x, c1row.y));
</script>

<svelte:window onpointerup={() => (dragging = null)} />

<div class="lab" data-interactive="dot-meter">
	<p class="invite">
		Turn the amber probe and watch each score get <em>built</em>: two products, stacked into a bar.
		Then stretch <span class="mono">c1</span> and watch size cheat a meter that direction earned.
	</p>

	<div class="stage">
		<div class="arena-wrap">
			<svg
				bind:this={arenaEl}
				viewBox="0 0 {S} {S}"
				class="arena"
				onpointermove={onArenaPointer}
				role="img"
				aria-label="An amber probe arrow among four periwinkle candidate arrows; drag the probe tip to turn it, drag c1's tip to stretch it"
			>
				<!-- angle ring + ticks -->
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
				<!-- axes, whisper-quiet -->
				<line x1={CX - R - 14} y1={CY} x2={CX + R + 14} y2={CY} class="axis" />
				<line x1={CX} y1={CY - R - 14} x2={CX} y2={CY + R + 14} class="axis" />

				<!-- candidates -->
				{#each rows as r (r.id)}
					{@const a = arrow(r.x, r.y)}
					{@const lp = labelPos(r.angle, r.len)}
					<g
						class="cand"
						class:sel={selected === r.id}
						onpointerdown={() => (selected = r.id)}
						role="button"
						tabindex="-1"
						aria-label={`select ${r.id}`}
					>
						<line {...{ x1: a.shaft.x1, y1: a.shaft.y1, x2: a.shaft.x2, y2: a.shaft.y2 }} class="shaft cand-stroke" />
						<polygon points={a.head} class="cand-fill" />
						<text x={lp.px} y={lp.py} class="lab mono">{r.id}</text>
					</g>
				{/each}

				<!-- c1 length handle -->
				<circle
					cx={c1HandlePos.px}
					cy={c1HandlePos.py}
					r="9"
					class="handle length-handle"
					class:active={dragging === 'length'}
					onpointerdown={(e) => startDrag('length', e)}
					onkeydown={lengthKeys}
					role="slider"
					tabindex="0"
					data-control="length-c1"
					aria-label="c1 length"
					aria-valuemin="0.5"
					aria-valuemax="2"
					aria-valuenow={f1(lengthC1)}
				/>

				<!-- probe on top -->
				{#if true}
					{@const a = arrow(probe.x, probe.y)}
					{@const mid = pt(probe.x * 0.55, probe.y * 0.55)}
					<line {...{ x1: a.shaft.x1, y1: a.shaft.y1, x2: a.shaft.x2, y2: a.shaft.y2 }} class="shaft probe-stroke" />
					<polygon points={a.head} class="probe-fill" />
					<text
						x={mid.px + 14 * Math.cos(rad(probeAngle + 90))}
						y={mid.py - 14 * Math.sin(rad(probeAngle + 90))}
						class="lab probe-lab mono">probe</text>
				{/if}
				<circle
					cx={probeTip.px}
					cy={probeTip.py}
					r="11"
					class="handle probe-handle"
					class:active={dragging === 'probe'}
					onpointerdown={(e) => startDrag('probe', e)}
					onkeydown={probeKeys}
					role="slider"
					tabindex="0"
					aria-label="probe angle in degrees"
					aria-valuemin="0"
					aria-valuemax="360"
					aria-valuenow={Math.round(probeAngle)}
				/>
				<text x={CX + R + 8} y={CY + 26} class="angle mono">{Math.round(probeAngle)}°</text>
			</svg>
		</div>

		<div class="meter">
			{#each rows as r (r.id)}
				<button
					class="row"
					class:leading={leaders.includes(r.id) && !tied}
					class:sel={selected === r.id}
					onclick={() => (selected = r.id)}
					aria-label={`${r.id} score ${f1(r.score)}${leaders.includes(r.id) && !tied ? ', leading' : ''}`}
				>
					<span class="row-id mono">{r.id}</span>
					<span class="bar" style="--h: {barH}px">
						<span class="zero"></span>
						<!-- x-term segment then y-term segment, stacked from the baseline -->
						<span
							class="seg segx"
							class:neg={r.px < 0}
							style="height: {segH(r.px)}px; bottom: {r.px >= 0 ? barH / 2 : barH / 2 - segH(r.px)}px"
						></span>
						<span
							class="seg segy"
							class:neg={r.py < 0}
							style="height: {segH(r.py)}px; bottom: {r.py >= 0
								? barH / 2 + (r.px > 0 ? segH(r.px) : 0)
								: barH / 2 - segH(r.py) - (r.px < 0 ? segH(r.px) : 0)}px"
						></span>
					</span>
					<span class="row-score mono" class:neg={r.score < 0}>{f1(r.score)}</span>
				</button>
			{/each}
			{#if tied}<span class="tie mono">tied</span>{/if}
			{#if cheatActive}
				<span class="flag mono">⚑ size passed straight through</span>
			{/if}
		</div>
	</div>

	<div class="strip" aria-live="polite">
		<span class="strip-lead">the whole recipe, live for <b class="mono">{sel.id}</b>:</span>
		<span class="mono eq">
			<span class="probe-c">{f(probe.x)}</span>·<span class="cand-c">{f(sel.x)}</span>
			<span class="op">+</span>
			<span class="probe-c">{f(probe.y)}</span>·<span class="cand-c">{f(sel.y)}</span>
			<span class="op">=</span>
			<span class="segx-c">{f(sel.px)}</span>
			<span class="op">+</span>
			<span class="segy-c">{f(sel.py)}</span>
			<span class="op">=</span>
			<span class="score-c">{f(sel.score)}</span>
		</span>
		<span class="strip-note">multiply the matched entries, add the products. That sum is the bar.</span>
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
		font-size: 0.98rem;
		line-height: 1.5;
		color: color-mix(in oklab, var(--color-text) 88%, transparent);
	}
	.invite em { color: var(--color-brand-mint); font-style: normal; }
	.mono { font-family: var(--font-mono); }

	.stage { display: flex; gap: 1.4rem; align-items: stretch; }
	.arena-wrap { flex: 1 1 55%; min-width: 0; }
	.arena { width: 100%; height: auto; touch-action: none; display: block; }

	.ring { fill: none; stroke: color-mix(in oklab, var(--color-text) 10%, transparent); stroke-width: 1; }
	.tick { stroke: color-mix(in oklab, var(--color-text) 14%, transparent); stroke-width: 1; }
	.axis { stroke: color-mix(in oklab, var(--color-text) 7%, transparent); stroke-width: 1; }

	.shaft { stroke-width: 2.4; stroke-linecap: round; }
	.cand-stroke { stroke: var(--data-observed); }
	.cand-fill { fill: var(--data-observed); }
	.probe-stroke { stroke: var(--data-heat); }
	.probe-fill { fill: var(--data-heat); }
	.cand { opacity: 0.82; cursor: pointer; transition: opacity var(--motion-min-ms) var(--ease-out-quint); }
	.cand.sel { opacity: 1; }
	.cand.sel .shaft { stroke-width: 3; }

	.lab .arena text.lab { fill: var(--color-text); font-size: 13px; text-anchor: middle; dominant-baseline: middle; }
	.probe-lab { fill: var(--data-heat) !important; }
	.angle { fill: color-mix(in oklab, var(--color-text) 45%, transparent); font-size: 12px; }

	.handle { fill: transparent; stroke: transparent; cursor: grab; }
	.handle:focus-visible { outline: none; stroke: var(--color-brand-mint); stroke-width: 2; }
	.handle.active { cursor: grabbing; }
	.probe-handle { stroke: color-mix(in oklab, var(--data-heat) 55%, transparent); stroke-width: 1.5; stroke-dasharray: 3 3; }
	.length-handle { stroke: color-mix(in oklab, var(--data-observed) 65%, transparent); stroke-width: 1.5; }

	.meter { flex: 0 0 auto; display: flex; gap: 0.9rem; align-items: flex-end; align-self: center; padding: 1.6rem 0.2rem 0.4rem; position: relative; }
	.row {
		display: flex; flex-direction: column; align-items: center; gap: 0.3rem;
		background: none; border: none; padding: 0.3rem 0.35rem; border-radius: 8px; cursor: pointer;
		color: var(--color-text);
	}
	.row.sel { background: color-mix(in oklab, var(--color-text) 6%, transparent); }
	.row.leading .row-id { color: var(--color-brand-mint); }
	.row-id { font-size: 0.8rem; opacity: 0.85; }
	.row-score { font-size: 0.85rem; color: var(--data-params); }
	.row-score.neg { color: var(--data-error); }

	.bar { position: relative; width: 18px; height: var(--h); }
	.zero {
		position: absolute; left: -3px; right: -3px; top: 50%; height: 1px;
		background: color-mix(in oklab, var(--color-text) 25%, transparent);
	}
	.seg {
		position: absolute; left: 0; width: 100%; border-radius: 2px;
		transition: height var(--motion-min-ms) linear, bottom var(--motion-min-ms) linear;
	}
	.segx { background: var(--data-params); }
	.segy { background: color-mix(in oklab, var(--data-params) 55%, var(--color-surface)); }
	.seg.neg { opacity: 0.85; }

	.tie, .flag {
		position: absolute; top: -0.4rem; right: 0; font-size: 0.72rem;
	}
	.tie { color: color-mix(in oklab, var(--color-text) 55%, transparent); }
	.flag { color: var(--data-error); }

	.strip {
		margin-top: 1.1rem; padding-top: 0.9rem;
		border-top: 1px solid color-mix(in oklab, var(--color-text) 8%, transparent);
		display: flex; flex-wrap: wrap; gap: 0.35rem 1rem; align-items: baseline;
	}
	.strip-lead { font-size: 0.85rem; opacity: 0.75; }
	.eq { font-size: 1.02rem; letter-spacing: 0.01em; }
	.op { opacity: 0.6; padding: 0 0.1rem; }
	.probe-c { color: var(--data-heat); }
	.cand-c { color: var(--data-observed); }
	.segx-c { color: var(--data-params); }
	.segy-c { color: color-mix(in oklab, var(--data-params) 65%, var(--color-text)); }
	.score-c { color: var(--data-fit); font-weight: 600; }
	.strip-note { flex-basis: 100%; font-size: 0.8rem; opacity: 0.55; }

	@media (max-width: 700px) {
		.stage { flex-direction: column; }
		.meter { align-self: center; }
	}
</style>
