<script lang="ts">
	const stills = [
		{ file: 'A_Totals_ManimCE_v0.20.1.png', moment: 'Snapshot A', line: 'Attempt one, compare totals: Night Drive and Glass Rain tie at 1 away, and (3,1) vs (1,3) exposes the flaw.' },
		{ file: 'B_Differences_ManimCE_v0.20.1.png', moment: 'Snapshot B', line: 'Attempt two, entry-by-entry differences: keeps the mix, ignores how much you care.' },
		{ file: 'C_Votes_ManimCE_v0.20.1.png', moment: 'Snapshot C', line: 'The repair: your numbers are votes; multiply your vote by their amount.' },
		{ file: 'D_Score_ManimCE_v0.20.1.png', moment: 'Snapshot D', line: 'Add the votes: match 5, with its lineage still on screen.' },
		{ file: 'E_Chip_ManimCE_v0.20.1.png', moment: 'Snapshot E', line: 'The recipe compacts into the corner chip the notation lands beside.' }
	];
</script>

<svelte:head><title>dev · section 2 stills</title></svelte:head>

<main>
	<h1>Section 2 mock stills, take 2</h1>
	<p class="sub">One persistent stage: the four columns never leave; every attempt happens on them.</p>
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
