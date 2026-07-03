<script lang="ts">
	import '../styles/tokens.css';
	import '@fontsource/bricolage-grotesque/600.css';
	import '@fontsource/literata/400.css';
	import '@fontsource/literata/400-italic.css';
	import '@fontsource/ibm-plex-mono/400.css';

	let { children } = $props();
</script>

{@render children()}

<style>
	:global(body) {
		margin: 0;
		background: var(--color-bg);
		color: var(--color-text);
		font-family: var(--font-body), Georgia, serif;
		-webkit-font-smoothing: antialiased;
	}
</style>
