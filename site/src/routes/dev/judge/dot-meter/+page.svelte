<script lang="ts">
	// DotMeter v2 — the judge's hand-built take, for direct iteration with Jake.
	// The design thesis: multiply-and-add should be VISIBLE, not narrated.
	// Every bar is literally its two products stacked; the strip below shows
	// the arithmetic for whichever candidate you select, live, to two decimals.

	// The two entries mean something: x is how loud, y is how fast.
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
		// one click always re-arms: a solved card resets on first click,
		// whether or not another challenge was active in between
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
			const px = probe.x * x; // the x-term product
			const py = probe.y * y; // the y-term product
			return { ...c, len, x, y, px, py, score: px + py };
		})
	);

	const maxScore = $derived(Math.max(...rows.map((r) => r.score)));
	const leaders = $derived(rows.filter((r) => Math.abs(r.score - maxScore) < 0.005).map((r) => r.id));
	const tied = $derived(leaders.length > 1);
	const sel = $derived(rows.find((r) => r.id === selected) ?? rows[0]);

	// The mirror lesson: c1 aims truest but is too short to win.
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

	// The overtake: c1 stretched AND outscoring a candidate that out-aligns it.
	// Returns the most deserving victim (best-aligned beaten song) so the flag
	// can name the exact pair instead of making a vague claim about the board.
	const cheatVictim = $derived.by(() => {
		const c1 = rows[0];
		if (lengthC1 <= 1.05) return null;
		const dist = (angle: number) => Math.abs(((angle - probeAngle + 540) % 360) - 180);
		const beaten = rows.filter(
			(r) => r.id !== 'c1' && dist(r.angle) < dist(c1.angle) && c1.score > r.score + 0.005
		);
		if (beaten.length === 0) return null;
		return beaten.reduce((a, b) => (dist(a.angle) < dist(b.angle) ? a : b));
	});
	const cheatActive = $derived(cheatVictim !== null);
	const leaderName = $derived(rows.find((r) => r.id === leaders[0])?.name ?? '');

	// --- Arena geometry (SVG units) ---
	const S = 400; // viewBox square
	const CX = S / 2;
	const CY = S / 2;
	const R = 92; // unit arrow length in px; 2.0 x R stays inside the frame
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
	const cl = (v: number) => Math.min(Math.max(v, 24), S - 24);
	const f1 = (n: number) => (Object.is(n, -0) ? 0 : n).toFixed(1);

	// Bar scale: scores live in [-2, 2] once c1 can stretch.
	const BARMAX = 2.05;
	const barH = 96;
	const segH = (v: number) => (Math.abs(v) / BARMAX) * (barH / 2);

	const probeTip = $derived(pt(probe.x, probe.y));
	const c1row = $derived(rows[0]);
	const c1HandlePos = $derived(pt(c1row.x, c1row.y));
</script>

<svelte:window onpointerup={() => (dragging = null)} />

<div class="lab" data-interactive="dot-meter">
	<p class="invite">
		Every song here is two numbers: how <em class="qw-loud">loud</em>, how <em class="qw-fast">fast</em>. So is your taste. Turn
		the amber taste arrow and watch each song's match get <em>built</em>: the <span class="qw-loud">loud product</span> plus
		the <span class="qw-fast">fast product</span>, stacked into one bar. Then grab Night Drive's round handle and change its size.
	</p>
	<div class="challenges">
		<button class="chal" class:active={challenge === 'cheat' && !solvedCheat} class:done={solvedCheat} onclick={() => startChallenge('cheat')}>
			<span class="chal-t mono">challenge 01</span>
			<span class="chal-g">Make a worse match win</span>
			{#if solvedCheat}
				<span class="chal-s mono">✓ solved · click to retry</span>
				<span class="chal-why">{WHY.cheat}</span>
			{:else if challenge === 'cheat'}
				<span class="chal-s mono live">in play…</span>
			{/if}
		</button>
		<button class="chal" class:active={challenge === 'short' && !solvedShort} class:done={solvedShort} onclick={() => startChallenge('short')}>
			<span class="chal-t mono">challenge 02</span>
			<span class="chal-g">Make the truest song lose</span>
			{#if solvedShort}
				<span class="chal-s mono">✓ solved · click to retry</span>
				<span class="chal-why">{WHY.short}</span>
			{:else if challenge === 'short'}
				<span class="chal-s mono live">in play…</span>
			{/if}
		</button>
	</div>

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
				<!-- axes, whisper-quiet, but named: the two entries ARE qualities -->
				<line x1={CX - R - 14} y1={CY} x2={CX + R + 14} y2={CY} class="axis" />
				<line x1={CX} y1={CY - R - 14} x2={CX} y2={CY + R + 14} class="axis" />
				<text x={CX + R + 18} y={CY - 6} class="axisq q-loud mono">loud</text>
				<text x={CX - 10} y={CY - R - 8} text-anchor="end" class="axisq q-fast mono">fast</text>
				<g class="legend">
					<line x1="16" y1="20" x2="34" y2="20" class="lg probe-stroke" />
					<text x="40" y="24" class="lgt mono">your taste</text>
					<line x1="16" y1="38" x2="34" y2="38" class="lg cand-stroke" />
					<text x="40" y="42" class="lgt mono">songs</text>
				</g>

				<!-- coordinates made visible: dashed drops for probe and selected -->
				{#each [{ x: probe.x, y: probe.y, cls: 'p' }, { x: sel.x, y: sel.y, cls: 'c' }] as d (d.cls)}
					{@const tip = pt(d.x, d.y)}
					<line x1={tip.px} y1={tip.py} x2={tip.px} y2={CY} class="drop {d.cls}" />
					<line x1={tip.px} y1={tip.py} x2={CX} y2={tip.py} class="drop {d.cls}" />
					<text x={cl(tip.px)} y={CY + (d.cls === 'p' ? 13 : 25)} class="coord mono {d.cls}">{f(d.x)}</text>
					<text x={CX - (d.cls === 'p' ? 4 : 32)} y={cl(tip.py) - 3} class="coord mono {d.cls}" text-anchor="end">{f(d.y)}</text>
				{/each}

				<!-- candidates -->
				{#each rows as r (r.id)}
					{@const a = arrow(r.x, r.y)}
					<g
						class="cand"
						class:sel={selected === r.id}
						class:hov={hovered === r.id}
						onpointerdown={() => (selected = r.id)}
						role="button"
						tabindex="-1"
						aria-label={`select ${r.name}`}
					>
						<line {...{ x1: a.shaft.x1, y1: a.shaft.y1, x2: a.shaft.x2, y2: a.shaft.y2 }} class="shaft cand-stroke" />
						<polygon points={a.head} class="cand-fill" />
						{#if selected === r.id}
							{@const lp = labelPos(r.angle, r.len, 26)}
							<text
								x={Math.min(Math.max(lp.px, 44), S - 48)}
								y={Math.min(Math.max(lp.py, 16), S - 10)}
								class="lab song-lab halo">{r.name}</text>
						{/if}
					</g>
				{/each}

				<!-- c1 length handle -->
				<circle
					cx={c1HandlePos.px}
					cy={c1HandlePos.py}
					r="9"
					class="handle length-handle"
					class:active={dragging === 'length'}
					class:pulse={challenge !== null && !((challenge === 'cheat' && cheatActive) || (challenge === 'short' && shortChanged))}
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
					<line {...{ x1: a.shaft.x1, y1: a.shaft.y1, x2: a.shaft.x2, y2: a.shaft.y2 }} class="shaft probe-stroke" />
					<polygon points={a.head} class="probe-fill" />
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
				<text x="14" y={S - 14} class="angle mono">taste at {Math.round(probeAngle)}°</text>
			</svg>
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
					aria-label={`${r.name} score ${f(r.score)}${leaders.includes(r.id) && !tied ? ', leading' : ''}`}
				>
					<span class="row-id">{r.name}</span>
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
					<span class="row-score mono" class:neg={r.score < 0}>{f(r.score)}</span>
					{#if leaders.includes(r.id) && !tied}<span class="leads mono">leads</span>{/if}
				</button>
			{/each}
			{#if tied}<span class="tie mono">tied</span>{/if}
			{#if cheatVictim}
				<span class="flag mono">⚑ {cheatVictim.name} matches your taste better, but Night Drive outscores it on size</span>
			{:else if shortChanged}
				<span class="flag short mono">⚑ Night Drive matches best, but {leaderName} wins on size</span>
			{/if}
		</div>
	</div>
	{#if challenge === null && cheatActive}
		<p class="why">Why this matters: {WHY.cheat}</p>
	{:else if challenge === null && shortChanged}
		<p class="why">Why this matters: {WHY.short}</p>
	{/if}
	<p class="hint">
		Click any bar or arrow to inspect it. The dashed lines are that arrow's two
		entries (its loudness and its speed), the numbers the recipe multiplies.
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
			<span class="score-c">{f(sel.score)}</span>
		</span>
		<span class="strip-note">
			multiply the matched entries, add the products. The <span class="qw-loud">lilac slice</span>
			of each bar is its loud product, the <span class="qw-fast">mint slice</span> its fast
			product; stacked, they are the score.
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
		font-size: 0.98rem;
		line-height: 1.5;
		color: color-mix(in oklab, var(--color-text) 88%, transparent);
	}
	.invite em { color: var(--color-brand-mint); font-style: normal; }
	.invite .qw-loud, .lab .invite .qw-loud { color: var(--data-params); font-style: normal; }
	.invite .qw-fast, .lab .invite .qw-fast { color: color-mix(in oklab, var(--color-brand-mint) 85%, var(--color-text)); font-style: normal; }
	.mono { font-family: var(--font-mono); }

	.stage { display: flex; gap: 1.4rem; align-items: stretch; }
	.arena-wrap { flex: 1 1 62%; min-width: 0; }
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
		background: none; padding: 0.3rem 0.35rem; border-radius: 8px; cursor: pointer;
		color: var(--color-text);
		border: 1px solid color-mix(in oklab, var(--color-text) 10%, transparent);
		width: 5.6rem; box-sizing: border-box;
	}
	.row-id { min-height: 2.1em; display: flex; align-items: center; justify-content: center; text-align: center; }
	.row:hover { border-color: var(--color-brand-mint); }
	.row.sel { background: color-mix(in oklab, var(--color-text) 6%, transparent); border-color: var(--data-observed); }
	.leads { font-size: 0.6rem; color: var(--color-brand-mint); letter-spacing: 0.06em; }
	.drop { stroke-width: 1; stroke-dasharray: 3 4; opacity: 0.55; }
	.drop.p { stroke: var(--data-heat); }
	.drop.c { stroke: var(--data-observed); }
	.coord { font-size: 10px; }
	.coord.p { fill: var(--data-heat); }
	.coord.c { fill: var(--data-observed); }
	.flag.short { color: var(--data-heat); }
	.hint { margin: 0.7rem 0 0; font-size: 0.78rem; opacity: 0.55; }
	.why { margin: 0.7rem 0 0; font-size: 0.88rem; color: color-mix(in oklab, var(--color-text) 82%, transparent); }
	.axisq { fill: color-mix(in oklab, var(--color-text) 40%, transparent); font-size: 10px; }
	.song-lab { font-size: 11.5px; }
	.halo { paint-order: stroke; stroke: var(--color-bg); stroke-width: 4px; }
	.lg { stroke-width: 2.4; stroke-linecap: round; }
	.lgt { fill: color-mix(in oklab, var(--color-text) 55%, transparent); font-size: 10.5px; }
	.cand.hov { opacity: 1; }
	.cand.hov .shaft { stroke-width: 3.2; }
	.challenges { display: flex; gap: 0.6rem; align-items: stretch; flex-wrap: wrap; margin: 0 0 1rem; }
	.chal {
		flex: 1 1 0; min-width: 0;
		display: flex; flex-direction: column; align-items: flex-start; gap: 0.18rem;
		color: var(--color-text); text-align: left;
		background: color-mix(in oklab, var(--color-text) 3%, transparent);
		border: 1px solid color-mix(in oklab, var(--color-text) 16%, transparent);
		border-radius: 10px; padding: 0.55rem 0.85rem; cursor: pointer; opacity: 0.9;
	}
	.chal:hover { border-color: var(--color-brand-mint); opacity: 1; }
	.chal.active { border-color: var(--data-heat); opacity: 1; }
	.chal.done { border-color: var(--data-fit); }
	.chal-t { font-size: 0.6rem; letter-spacing: 0.1em; opacity: 0.55; }
	.chal-g { font-family: var(--font-heading), sans-serif; font-size: 0.88rem; }
	.chal-s { font-size: 0.7rem; color: var(--data-fit); }
	.chal-s.live { color: var(--data-heat); }
	.chal-why {
		max-width: 30rem; font-size: 0.78rem; line-height: 1.45;
		color: color-mix(in oklab, var(--color-text) 78%, transparent);
	}
	.handle.pulse { animation: hpulse 1.5s ease-in-out infinite; }
	@keyframes hpulse {
		0%, 100% { stroke-width: 1.5; }
		50% { stroke-width: 4.5; stroke-opacity: 1; }
	}
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
	.segy { background: color-mix(in oklab, var(--color-brand-mint) 72%, var(--color-surface)); }
	.seg.neg { opacity: 0.85; }

	.tie, .flag {
		position: absolute; top: -1.1rem; right: 0; font-size: 0.72rem;
		max-width: 24rem; text-align: right; line-height: 1.35;
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
	.segy-c { color: color-mix(in oklab, var(--color-brand-mint) 85%, var(--color-text)); }
	.qw-loud { color: var(--data-params); opacity: 0.9; }
	.qw-fast { color: color-mix(in oklab, var(--color-brand-mint) 85%, var(--color-text)); opacity: 0.9; }
	.q-loud { fill: color-mix(in oklab, var(--data-params) 80%, transparent); }
	.q-fast { fill: color-mix(in oklab, var(--color-brand-mint) 70%, transparent); }
	.score-c { color: var(--data-fit); font-weight: 600; }
	.strip-note { flex-basis: 100%; font-size: 0.8rem; opacity: 0.55; }

	@media (max-width: 700px) {
		.stage { flex-direction: column; }
		.meter { align-self: center; }
	}
</style>
