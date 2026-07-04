<script lang="ts">
	import '@fontsource/bricolage-grotesque/700.css';
	import '@fontsource/ibm-plex-mono/400-italic.css';
	import TrueUp from '../../../../shared/components/TrueUp.svelte';

	interface Swatch {
		token: string;
		name: string;
		job: string;
	}

	const core: Swatch[] = [
		{ token: '--color-bg', name: '10pm Sky', job: 'Page & video background' },
		{ token: '--color-surface', name: 'Lamplit Room', job: 'Cards, callouts, code wells' },
		{
			token: '--color-text',
			name: 'Paper Under Lamplight',
			job: 'Body text — warm cream, never clinical white'
		},
		{
			token: '--color-brand-mint',
			name: 'Trued Mint',
			job: 'THE signature: trued lines, settle-glow, correctness'
		},
		{
			token: '--color-brand-rose',
			name: 'Open-Sign Rose',
			job: 'Warmth, jokes, emphasis — rationed 1–2× per lesson'
		},
		{
			token: '--color-brand-periwinkle',
			name: 'Streetlamp Periwinkle',
			job: 'Structure: links, UI chrome, wayfinding'
		}
	];

	const data: Swatch[] = [
		{ token: '--data-observed', name: 'observed', job: 'Raw data / observations' },
		{ token: '--data-params', name: 'params', job: 'Weights / learned things' },
		{ token: '--data-truth', name: 'truth', job: 'Ground truth / reference' },
		{ token: '--data-heat', name: 'heat', job: 'Attention / intensity (sparing)' },
		{ token: '--data-fit', name: 'fit', job: 'Converged / TRUE — rhymes with mint' },
		{ token: '--data-error', name: 'error', job: 'Residual / tension — rhymes with rose' }
	];

	// Resolved swatch values are read from the stylesheet at runtime so the
	// page can DISPLAY them without a single hex literal in source (lint rule).
	let resolved = $state<Record<string, string>>({});
	$effect(() => {
		const style = getComputedStyle(document.documentElement);
		const out: Record<string, string> = {};
		for (const s of [...core, ...data]) {
			out[s.token] = style.getPropertyValue(s.token).trim().toUpperCase();
		}
		resolved = out;
	});

	// Motion demo: dramatic durations are user-triggered only, so the arrival
	// replays on a button, not a loop.
	let arrivals = $state(0);
</script>

<svelte:head>
	<title>Night School — brand</title>
	<meta name="description" content="Brand ratification sample: palette, type, motion, True-Up." />
</svelte:head>

<main>
	<!-- (a) The session-page header treatment -->
	<header class="session-header">
		<p class="wordmark">NIGHT SCHOOL · SESSION 01</p>
		<h1 class="title">Why does a lookup table need&nbsp;calculus?</h1>
		<div class="underline">
			<TrueUp d="M2 10 C 110 3, 290 15, 478 6" width={480} height={18} strokeWidth={3} />
		</div>
		<p class="subtitle">
			A filing cabinet that leans toward your question. Drawers that open by degrees. Somewhere in
			the stacks, a derivative clears its throat.
		</p>
	</header>

	<!-- (b) Palette -->
	<section aria-labelledby="palette">
		<p class="section-label" id="palette">01 · PALETTE</p>
		<h2>Math drawn in light, because it&rsquo;s dark out</h2>
		<ul class="swatches core">
			{#each core as s (s.token)}
				<li class="swatch-card">
					<div class="chip" style="background: var({s.token})"></div>
					<p class="swatch-name">{s.name}</p>
					<p class="swatch-token">var({s.token}) <span class="value">{resolved[s.token] ?? ''}</span></p>
					<p class="swatch-job">{s.job}</p>
				</li>
			{/each}
		</ul>
		<p class="rule-note">
			Semantic data series — one color, one job, across every session. The two rhymes are the
			point: brand colors accrue mathematical meaning.
		</p>
		<ul class="swatches data">
			{#each data as s (s.token)}
				<li class="swatch-card">
					<div class="chip small" style="background: var({s.token})"></div>
					<p class="swatch-token">data.{s.name} <span class="value">{resolved[s.token] ?? ''}</span></p>
					<p class="swatch-job">{s.job}</p>
				</li>
			{/each}
		</ul>
	</section>

	<!-- (c) Type specimens -->
	<section aria-labelledby="type">
		<p class="section-label" id="type">02 · TYPE</p>
		<h2>Three voices, no costumes</h2>

		<div class="specimen">
			<p class="specimen-meta">Headings / UI — Bricolage Grotesque</p>
			<p class="spec-display">Still up?</p>
			<p class="spec-heading">Class dismissed.</p>
			<p class="spec-weights">
				<span class="w400">Grotesque 400</span> · <span class="w600">600</span> ·
				<span class="w700">700</span>
			</p>
		</div>

		<div class="specimen">
			<p class="specimen-meta">Body — Literata</p>
			<p class="spec-body">
				Class dismissed. Every trick we pulled up there is disclosed in the notes — go check our
				work. Then take the long way home; ideas true up better in motion.
			</p>
			<p class="spec-body-italic">
				Advanced machine learning, after hours. Stories first. Rigor always. Kettle&rsquo;s on.
			</p>
		</div>

		<div class="specimen well">
			<p class="specimen-meta">Mono — IBM Plex Mono</p>
			<p class="spec-mono">NIGHT SCHOOL · SESSION 01 <span class="dim">23:47</span></p>
			<p class="spec-mono">shapes: Q (B, T, d) · K (B, T, d) · V (B, T, d)</p>
			<p class="spec-mono annotation"># pre-formal: a lookup table, but the keys negotiate</p>
			<p class="spec-mono glow-line">assert torch.allclose(ours, theirs) <span class="mint">· trued</span></p>
		</div>
	</section>

	<!-- (d) Motion personality -->
	<section aria-labelledby="motion">
		<p class="section-label" id="motion">03 · MOTION</p>
		<h2>Deliberate · warm · settling · exact-at-the-end</h2>
		<p class="prose">
			Elements arrive on easeOutQuint with a small decaying wobble, so the final 150ms of every
			key animation is the rough becoming exact. Never instant; dramatic durations are
			user-triggered only — like this one.
		</p>
		<div class="motion-stage">
			<button class="bell" onclick={() => (arrivals += 1)}>
				{arrivals === 0 ? 'Ring the bell' : 'Ring it again'}
			</button>
			{#key arrivals}
				<div class="arriving-card" class:waiting={arrivals === 0}>
					<p class="arrive-title">The aha arrives, then trues.</p>
					<TrueUp
						d="M2 7 C 60 3, 150 11, 238 5"
						width={240}
						height={14}
						strokeWidth={2.5}
						trigger={arrivals > 0}
					/>
				</div>
			{/key}
		</div>
		<p class="motion-tokens">
			easeOutQuint&nbsp;&nbsp;cubic-bezier(0.22, 1, 0.36, 1)<br />
			wobble&nbsp;&nbsp;≤ 2px, decaying → 0<br />
			true-up&nbsp;&nbsp;800ms · min&nbsp;&nbsp;150ms · dramatic&nbsp;&nbsp;≥ 1500ms, user-triggered only<br />
			prefers-reduced-motion&nbsp;&nbsp;crossfade, no wobble
		</p>
	</section>

	<footer>
		<p class="walk-home-label">FOR THE WALK HOME</p>
		<p class="walk-home">
			If every answer is a weighted average, what — exactly — chooses the weights?
		</p>
	</footer>
</main>

<style>
	main {
		max-width: 64rem;
		margin: 0 auto;
		padding: 0 1.5rem 6rem;
	}

	/* ————— header ————— */

	.session-header {
		position: relative;
		padding: clamp(5rem, 16vh, 9rem) 0 5rem;
	}

	.session-header::before {
		/* one streetlamp's worth of periwinkle, high and faint */
		content: '';
		position: absolute;
		inset: -6rem -10rem 0;
		background: radial-gradient(
			42rem 26rem at 30% 0%,
			color-mix(in oklab, var(--color-brand-periwinkle) 9%, transparent),
			transparent 70%
		);
		pointer-events: none;
	}

	.wordmark {
		margin: 0 0 2.25rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.8rem;
		letter-spacing: 0.45em;
		color: var(--color-brand-periwinkle);
	}

	.title {
		margin: 0;
		max-width: 16ch;
		font-family: var(--font-heading), sans-serif;
		font-weight: 700;
		font-size: clamp(2.5rem, 6.5vw, 4.4rem);
		line-height: 1.06;
		letter-spacing: -0.01em;
		color: var(--color-text);
	}

	.underline {
		max-width: min(30rem, 82%);
		margin-top: 1.4rem;
	}

	.underline :global(svg) {
		width: 100%;
		height: auto;
	}

	.subtitle {
		margin: 2rem 0 0;
		max-width: 44ch;
		font-family: var(--font-body), Georgia, serif;
		font-style: italic;
		font-size: clamp(1.05rem, 1.9vw, 1.25rem);
		line-height: 1.6;
		color: color-mix(in oklab, var(--color-text) 82%, transparent);
	}

	/* ————— sections ————— */

	section {
		padding: 4.5rem 0 0;
	}

	.section-label {
		margin: 0 0 0.9rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.75rem;
		letter-spacing: 0.35em;
		color: var(--color-brand-periwinkle);
	}

	h2 {
		margin: 0 0 2rem;
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: clamp(1.4rem, 2.6vw, 1.9rem);
		color: var(--color-text);
	}

	.prose {
		max-width: 56ch;
		margin: 0 0 1.75rem;
		font-family: var(--font-body), Georgia, serif;
		line-height: 1.7;
	}

	/* ————— palette ————— */

	.swatches {
		list-style: none;
		margin: 0;
		padding: 0;
		display: grid;
		gap: 1rem;
	}

	.swatches.core {
		grid-template-columns: repeat(auto-fit, minmax(17.5rem, 1fr));
	}

	.swatches.data {
		grid-template-columns: repeat(auto-fit, minmax(9rem, 1fr));
	}

	.swatch-card {
		background: var(--color-surface);
		border: 1px solid color-mix(in oklab, var(--color-text) 7%, transparent);
		border-radius: 12px;
		padding: 0.9rem;
	}

	.chip {
		height: 4.25rem;
		border-radius: 8px;
		border: 1px solid color-mix(in oklab, var(--color-text) 12%, transparent);
		margin-bottom: 0.85rem;
	}

	.chip.small {
		height: 2.75rem;
	}

	.swatch-name {
		margin: 0 0 0.2rem;
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: 1rem;
	}

	.swatch-token {
		margin: 0 0 0.45rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.72rem;
		color: var(--color-brand-periwinkle);
		overflow-wrap: anywhere;
	}

	.swatch-token .value {
		color: color-mix(in oklab, var(--color-text) 55%, transparent);
	}

	.swatch-job {
		margin: 0;
		font-family: var(--font-body), Georgia, serif;
		font-style: italic;
		font-size: 0.85rem;
		line-height: 1.45;
		color: color-mix(in oklab, var(--color-text) 72%, transparent);
	}

	.rule-note {
		max-width: 56ch;
		margin: 2.25rem 0 1rem;
		font-family: var(--font-body), Georgia, serif;
		font-style: italic;
		font-size: 0.95rem;
		color: color-mix(in oklab, var(--color-text) 75%, transparent);
	}

	/* ————— type ————— */

	.specimen {
		background: var(--color-surface);
		border: 1px solid color-mix(in oklab, var(--color-text) 7%, transparent);
		border-radius: 12px;
		padding: 1.75rem 2rem;
		margin-bottom: 1.25rem;
	}

	.specimen-meta {
		margin: 0 0 1.4rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.72rem;
		letter-spacing: 0.22em;
		text-transform: uppercase;
		color: var(--color-brand-periwinkle);
	}

	.spec-display {
		margin: 0 0 0.5rem;
		font-family: var(--font-heading), sans-serif;
		font-weight: 700;
		font-size: clamp(2.6rem, 5.5vw, 4rem);
		line-height: 1.05;
	}

	.spec-heading {
		margin: 0 0 1.2rem;
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: 1.6rem;
	}

	.spec-weights {
		margin: 0;
		font-family: var(--font-heading), sans-serif;
		font-size: 1.05rem;
		color: color-mix(in oklab, var(--color-text) 78%, transparent);
	}

	.spec-weights .w400 {
		font-weight: 400;
	}

	.spec-weights .w600 {
		font-weight: 600;
	}

	.spec-weights .w700 {
		font-weight: 700;
	}

	.spec-body {
		margin: 0 0 1.1rem;
		max-width: 58ch;
		font-family: var(--font-body), Georgia, serif;
		font-size: 1.08rem;
		line-height: 1.75;
	}

	.spec-body-italic {
		margin: 0;
		font-family: var(--font-body), Georgia, serif;
		font-style: italic;
		font-size: 1.02rem;
		color: color-mix(in oklab, var(--color-text) 80%, transparent);
	}

	.specimen.well {
		background: color-mix(in oklab, var(--color-surface) 72%, var(--color-bg));
	}

	.spec-mono {
		margin: 0 0 0.55rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.92rem;
		line-height: 1.55;
	}

	.spec-mono .dim {
		color: color-mix(in oklab, var(--color-text) 45%, transparent);
	}

	.spec-mono.annotation {
		font-style: italic;
		color: var(--color-brand-periwinkle);
	}

	.spec-mono .mint {
		color: var(--color-brand-mint);
	}

	/* ————— motion ————— */

	.motion-stage {
		display: flex;
		align-items: center;
		gap: 2.5rem;
		flex-wrap: wrap;
		background: var(--color-surface);
		border: 1px solid color-mix(in oklab, var(--color-text) 7%, transparent);
		border-radius: 12px;
		padding: 2rem;
		min-height: 9.5rem;
	}

	.bell {
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: 0.95rem;
		color: var(--color-bg);
		background: var(--color-brand-mint);
		border: none;
		border-radius: 999px;
		padding: 0.8rem 1.5rem;
		min-height: 44px;
		min-width: 44px;
		cursor: pointer;
		transition: transform 150ms var(--ease-out-quint);
	}

	.bell:hover {
		transform: translateY(-1px);
	}

	.arriving-card {
		background: var(--color-bg);
		border: 1px solid color-mix(in oklab, var(--color-brand-mint) 22%, transparent);
		border-radius: 10px;
		padding: 1.2rem 1.5rem 1rem;
		animation: arrive 800ms var(--ease-out-quint) both;
	}

	.arriving-card.waiting {
		animation: none;
		opacity: 0.35;
	}

	.arrive-title {
		margin: 0 0 0.6rem;
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: 1.05rem;
	}

	@keyframes arrive {
		0% {
			opacity: 0;
			transform: translateY(18px);
		}
		60% {
			opacity: 1;
			transform: translateY(-1.8px);
		}
		78% {
			transform: translateY(0.9px);
		}
		90% {
			transform: translateY(-0.4px);
		}
		100% {
			opacity: 1;
			transform: translateY(0);
		}
	}

	@media (prefers-reduced-motion: reduce) {
		.arriving-card {
			animation: arrive-fade 800ms ease both;
		}

		@keyframes arrive-fade {
			from {
				opacity: 0;
			}
			to {
				opacity: 1;
			}
		}
	}

	.motion-tokens {
		margin: 1.75rem 0 0;
		font-family: var(--font-mono), monospace;
		font-size: 0.82rem;
		line-height: 1.9;
		color: color-mix(in oklab, var(--color-text) 65%, transparent);
	}

	/* ————— footer ————— */

	footer {
		margin-top: 6rem;
		padding-top: 2.5rem;
		border-top: 1px solid color-mix(in oklab, var(--color-text) 10%, transparent);
	}

	.walk-home-label {
		margin: 0 0 0.75rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.72rem;
		letter-spacing: 0.35em;
		color: var(--color-brand-periwinkle);
	}

	.walk-home {
		margin: 0;
		max-width: 44ch;
		font-family: var(--font-body), Georgia, serif;
		font-style: italic;
		font-size: 1.15rem;
		line-height: 1.6;
		color: color-mix(in oklab, var(--color-text) 85%, transparent);
	}
</style>
