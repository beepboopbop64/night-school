<script lang="ts">
	import type { Component } from 'svelte';

	// Session artifacts are produced by the harness into sessions/toy/page/.
	// The route must build even before they exist (virgin state), so glob
	// imports with an empty-state fallback instead of hard imports.
	const sections = import.meta.glob('../../../../../sessions/toy/page/sections/*.md', {
		eager: true
	}) as Record<string, { default: Component }>;
	const interactives = import.meta.glob('../../../../../sessions/toy/page/interactives/*.svelte', {
		eager: true
	}) as Record<string, { default: Component }>;

	const sectionEntries = Object.entries(sections).sort(([a], [b]) => a.localeCompare(b));
	const interactiveEntries = Object.entries(interactives).sort(([a], [b]) => a.localeCompare(b));
</script>

<svelte:head>
	<title>Night School · toy session</title>
	<meta name="description" content="Walking-skeleton toy session. Rails, not teaching." />
</svelte:head>

<main>
	<header>
		<p class="wordmark">NIGHT SCHOOL</p>
		<div class="rule" aria-hidden="true"></div>
		<h1>Toy session</h1>
		<p class="quiet">Walking skeleton (M1). Rails, not teaching.</p>
	</header>

	<section aria-label="video">
		<h2>Video</h2>
		<div class="video-placeholder">
			<p class="mono">media/session.mp4</p>
			<p class="quiet">
				Rendered locally by the harness. Media hosting is open decision D-O1, so the file is not
				served here; play it from disk under sessions/toy/media/.
			</p>
		</div>
	</section>

	{#if sectionEntries.length === 0}
		<p class="quiet">No sections produced yet. Run <span class="mono">harness run toy</span>.</p>
	{:else}
		{#each sectionEntries as [file, mod] (file)}
			{@const Section = mod.default}
			<section class="prose" aria-label="section">
				<Section />
			</section>
		{/each}
	{/if}

	{#each interactiveEntries as [file, mod] (file)}
		{@const Interactive = mod.default}
		<section aria-label="interactive">
			<Interactive />
		</section>
	{/each}
</main>

<style>
	main {
		max-width: 46rem;
		margin: 0 auto;
		padding: 3rem 1.5rem 5rem;
		display: flex;
		flex-direction: column;
		gap: 2.5rem;
	}

	.wordmark {
		margin: 0 0 1rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.85rem;
		letter-spacing: 0.45em;
		color: var(--color-brand-periwinkle);
	}

	.rule {
		width: 3.5rem;
		height: 2px;
		margin-bottom: 1.5rem;
		border-radius: 1px;
		background: var(--color-brand-mint);
	}

	h1 {
		margin: 0;
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: clamp(1.8rem, 4vw, 2.6rem);
	}

	h2 {
		margin: 0 0 0.75rem;
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: 1.15rem;
	}

	.video-placeholder {
		aspect-ratio: 16 / 9;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 0.5rem;
		padding: 1rem;
		text-align: center;
		background: var(--color-surface);
		border-radius: 8px;
	}

	.mono {
		margin: 0;
		font-family: var(--font-mono), monospace;
		font-size: 0.9rem;
		color: var(--color-brand-mint);
	}

	.quiet {
		margin: 0;
		font-family: var(--font-body), Georgia, serif;
		font-style: italic;
		font-size: 0.95rem;
		color: var(--color-text);
		opacity: 0.65;
		max-width: 38ch;
	}

	.prose :global(h1) {
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: 1.5rem;
	}

	.prose :global(blockquote) {
		margin: 1rem 0;
		padding: 0.25rem 0 0.25rem 1rem;
		border-left: 3px solid var(--color-brand-mint);
		font-style: italic;
	}

	.prose :global(p) {
		line-height: 1.65;
	}
</style>
