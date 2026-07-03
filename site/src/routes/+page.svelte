<svelte:head>
	<title>Night School</title>
	<meta name="description" content="Advanced machine learning, after hours." />
</svelte:head>

<main>
	<header>
		<p class="wordmark">NIGHT SCHOOL</p>
		<div class="rule" aria-hidden="true"></div>
	</header>

	<h1 class="tagline">
		<span class="tagline-lead">Advanced machine learning, after hours.</span>
		<span class="tagline-creed">Stories first. Rigor always. Kettle’s on.</span>
	</h1>

	<p class="quiet">No sessions published yet. The kettle’s on.</p>
</main>

<style>
	main {
		min-height: 100svh;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		gap: 2.75rem;
		padding: 2rem;
		text-align: center;
	}

	.wordmark {
		margin: 0 0 1rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.85rem;
		letter-spacing: 0.45em;
		text-indent: 0.45em; /* recenters tracked caps */
		color: var(--color-brand-periwinkle);
	}

	.rule {
		width: 3.5rem;
		height: 2px;
		margin: 0 auto;
		border-radius: 1px;
		background: var(--color-brand-mint);
	}

	.tagline {
		margin: 0;
		max-width: 24ch;
	}

	.tagline-lead {
		display: block;
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: clamp(1.9rem, 5vw, 3.1rem);
		line-height: 1.15;
		color: var(--color-text);
	}

	.tagline-creed {
		display: block;
		margin-top: 1.1rem;
		font-family: var(--font-body), Georgia, serif;
		font-style: italic;
		font-weight: 400;
		font-size: clamp(1rem, 2.2vw, 1.25rem);
		color: var(--color-text);
		opacity: 0.85;
	}

	.quiet {
		margin: 0;
		font-family: var(--font-body), Georgia, serif;
		font-style: italic;
		font-size: 0.95rem;
		color: var(--color-text);
		opacity: 0.6;
	}
</style>
