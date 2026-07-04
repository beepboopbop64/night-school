<script lang="ts">
	// ToySlider (M1 walking skeleton) — written by the web-section node; do not
	// edit by hand. Proves a session-owned interactive builds into the site
	// using design-token CSS variables only.
	let trueness = $state(35);
</script>

<div class="toy-slider">
	<label class="row">
		<span class="label">trueness</span>
		<input type="range" min="0" max="100" bind:value={trueness} />
	</label>
	<div class="track" aria-hidden="true">
		<div class="fill" style="width: {trueness}%"></div>
	</div>
	<p class="readout">
		{trueness < 100 ? `sketched (${trueness}% trued)` : "trued"}
	</p>
</div>

<style>
	.toy-slider {
		background: var(--color-surface);
		border-radius: 8px;
		padding: 1.25rem 1.5rem;
		max-width: 28rem;
	}

	.row {
		display: flex;
		align-items: center;
		gap: 1rem;
	}

	.label {
		font-family: var(--font-mono), monospace;
		font-size: 0.85rem;
		color: var(--color-brand-periwinkle);
	}

	input[type="range"] {
		flex: 1;
		min-height: 44px; /* a11y touch target */
		accent-color: var(--color-brand-mint);
	}

	.track {
		height: 4px;
		border-radius: 2px;
		background: var(--color-bg);
		overflow: hidden;
	}

	.fill {
		height: 100%;
		background: var(--data-fit);
		transition: width var(--motion-min-ms) var(--ease-out-quint);
	}

	@media (prefers-reduced-motion: reduce) {
		.fill {
			transition: none;
		}
	}

	.readout {
		margin: 0.75rem 0 0;
		font-family: var(--font-mono), monospace;
		font-size: 0.85rem;
		color: var(--color-text);
	}
</style>
