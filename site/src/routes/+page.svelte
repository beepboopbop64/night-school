<script lang="ts">
	import { catalog } from '$lib/catalog';

	let query = $state('');
	const hits = $derived(
		catalog.filter((entry) => {
			const q = query.trim().toLowerCase();
			if (q.length === 0) return true;
			return [entry.title, entry.question, entry.aha, entry.slug]
				.join(' ')
				.toLowerCase()
				.includes(q);
		})
	);
</script>

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

	<div class="index">
		<input
			class="search"
			type="search"
			placeholder="Search the sessions…"
			aria-label="Search the sessions"
			bind:value={query}
		/>

		<ul class="cards">
			{#each hits as entry (entry.slug)}
				<li>
					{#if entry.status === 'live'}
						<a class="card" href={`/sessions/${entry.slug}`}>
							<span class="card-q">{entry.question}</span>
							<span class="card-aha">“{entry.aha}”</span>
							<span class="card-meta mono">{entry.title} · ~{entry.minutes} min</span>
						</a>
					{:else}
						<div class="card coming" aria-label={`${entry.title}, in production`}>
							<span class="card-q">{entry.question}</span>
							<span class="card-aha">“{entry.aha}”</span>
							<span class="card-meta mono">{entry.title} · in the oven</span>
						</div>
					{/if}
				</li>
			{/each}
			{#if hits.length === 0}
				<li class="none">Nothing matches. The kettle’s still on, though.</li>
			{/if}
		</ul>
	</div>
</main>

<style>
	main {
		min-height: 100svh;
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 2.4rem;
		padding: 4rem 2rem 3rem;
		text-align: center;
	}

	.wordmark {
		margin: 0 0 1rem;
		font-family: var(--font-mono), monospace;
		font-size: 0.85rem;
		letter-spacing: 0.45em;
		text-indent: 0.45em;
		color: var(--color-brand-periwinkle);
	}

	.rule {
		width: 3.5rem;
		height: 2px;
		margin: 0 auto;
		border-radius: 1px;
		background: var(--color-brand-mint);
	}

	.tagline { margin: 0; max-width: 26ch; }
	.tagline-lead {
		display: block;
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: clamp(1.9rem, 5vw, 3.1rem);
		line-height: 1.15;
	}
	.tagline-creed {
		display: block;
		margin-top: 1.1rem;
		font-style: italic;
		font-size: clamp(1rem, 2.2vw, 1.25rem);
		opacity: 0.85;
	}

	.index { width: min(44rem, 100%); display: flex; flex-direction: column; gap: 1.4rem; }

	.search {
		width: 100%;
		box-sizing: border-box;
		padding: 0.7rem 1rem;
		font-family: var(--font-body), Georgia, serif;
		font-size: 1rem;
		color: var(--color-text);
		background: var(--color-surface);
		border: 1px solid color-mix(in oklab, var(--color-text) 12%, transparent);
		border-radius: 10px;
	}
	.search:focus { outline: 2px solid var(--color-brand-mint); outline-offset: 1px; }
	.search::placeholder { color: color-mix(in oklab, var(--color-text) 45%, transparent); }

	.cards { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 0.9rem; }

	.card {
		display: flex;
		flex-direction: column;
		gap: 0.45rem;
		padding: 1.1rem 1.3rem;
		text-align: left;
		background: var(--color-surface);
		border: 1px solid color-mix(in oklab, var(--color-text) 8%, transparent);
		border-radius: 12px;
		text-decoration: none;
		color: var(--color-text);
		transition: border-color var(--motion-min-ms) var(--ease-out-quint);
	}
	a.card:hover { border-color: var(--color-brand-mint); }
	.card.coming { opacity: 0.55; }

	.card-q {
		font-family: var(--font-heading), sans-serif;
		font-weight: 600;
		font-size: 1.15rem;
		line-height: 1.3;
	}
	.card-aha { font-style: italic; opacity: 0.8; font-size: 0.95rem; }
	.card-meta { font-size: 0.75rem; opacity: 0.55; letter-spacing: 0.04em; }
	.mono { font-family: var(--font-mono), monospace; }

	.none { font-style: italic; opacity: 0.6; padding: 1rem; }
</style>
