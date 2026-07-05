<script lang="ts">
	import '../styles/tokens.css';
	import '@fontsource/bricolage-grotesque/600.css';
	import '@fontsource/literata/400.css';
	import '@fontsource/literata/400-italic.css';
	import '@fontsource/ibm-plex-mono/400.css';
	import { page } from '$app/state';

	let { children } = $props();
	const onHome = $derived(page.url.pathname === '/');
</script>

{#if !onHome}
	<header class="shell-bar">
		<a class="shell-wordmark" href="/">NIGHT SCHOOL</a>
		<nav class="shell-nav">
			<a href="/">Lessons</a>
		</nav>
	</header>
{/if}

{@render children()}

<style>
	:global(body) {
		margin: 0;
		background: var(--color-bg);
		color: var(--color-text);
		font-family: var(--font-body), Georgia, serif;
		-webkit-font-smoothing: antialiased;
	}

	.shell-bar {
		position: sticky;
		top: 0;
		z-index: 20;
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding: 0.7rem 1.4rem;
		background: color-mix(in oklab, var(--color-bg) 88%, transparent);
		backdrop-filter: blur(8px);
		border-bottom: 1px solid color-mix(in oklab, var(--color-text) 7%, transparent);
	}

	.shell-wordmark {
		font-family: var(--font-mono), monospace;
		font-size: 0.75rem;
		letter-spacing: 0.4em;
		color: var(--color-brand-periwinkle);
		text-decoration: none;
	}
	.shell-wordmark:hover { color: var(--color-brand-mint); }

	.shell-nav a {
		font-family: var(--font-heading), sans-serif;
		font-size: 0.85rem;
		color: var(--color-text);
		opacity: 0.8;
		text-decoration: none;
	}
	.shell-nav a:hover { opacity: 1; color: var(--color-brand-mint); }
</style>
