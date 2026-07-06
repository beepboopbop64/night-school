<script lang="ts">
	const stills = [
		{ file: 'M3_IntensityContest_ManimCE_v0.20.1.png', moment: 'Moment 3', line: 'Idea one fails: the cranked column wins and your taste was never consulted.' },
		{ file: 'M6_ZeroMatches_ManimCE_v0.20.1.png', moment: 'Moment 6', line: 'Idea two fails: exact matching finds nothing, anywhere.' },
		{ file: 'M8_Multiply_ManimCE_v0.20.1.png', moment: 'Moment 8', line: 'The repair: your interest times their amount, one pair at a time.' },
		{ file: 'M9_Add_ManimCE_v0.20.1.png', moment: 'Moment 9', line: 'The products pool into 5 and answer the opening scorebox.' },
		{ file: 'M10_Chip_ManimCE_v0.20.1.png', moment: 'Moment 10', line: 'The recipe compacts into the chip the notation will land next to.' }
	];
</script>

<svelte:head><title>dev · section 2 stills</title></svelte:head>

<main>
	<h1>Section 2 mock stills</h1>
	<p class="sub">Hand-built compositions for the approved script. Mark up anything.</p>
	{#each stills as s (s.file)}
		<figure>
			<figcaption><span class="mono">{s.moment}</span> {s.line}</figcaption>
			<img src={'/dev/stills/' + s.file} alt={s.moment + ': ' + s.line} />
		</figure>
	{/each}
</main>

<style>
	main { max-width: 980px; margin: 2rem auto; padding: 0 1.2rem; }
	h1 { font-family: var(--font-heading), sans-serif; font-size: 1.5rem; }
	.sub { opacity: 0.7; margin-bottom: 1.6rem; }
	figure { margin: 0 0 2rem; }
	figcaption { margin-bottom: 0.5rem; font-size: 0.95rem; }
	.mono { font-family: var(--font-mono), monospace; color: var(--color-brand-mint); margin-right: 0.5rem; }
	img { width: 100%; border-radius: 10px; border: 1px solid color-mix(in oklab, var(--color-text) 10%, transparent); }
</style>
