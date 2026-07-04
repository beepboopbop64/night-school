<script lang="ts">
	// RailsProbe (M4): a hand-written, known-good interactive that satisfies the
	// full S4b control contract. It exists to verify the webslice machinery
	// (build, preview server, Playwright drives, weba11y DOM checks) without
	// spending coder or Iris tokens. Not teaching content. Dash-free on purpose:
	// the weba11y source scan covers comments too.
	let value = $state(35);
	const MIN = 0;
	const MAX = 100;
</script>

<div class="rails-probe" data-interactive="rails-probe">
	<label class="row">
		<span class="label">probe value</span>
		<input
			type="range"
			min={MIN}
			max={MAX}
			step="5"
			bind:value
			aria-label="probe value"
		/>
	</label>
	<svg aria-hidden="true" class="gauge" viewBox="0 0 100 8" preserveAspectRatio="none">
		<rect x="0" y="2" width="100" height="4" rx="2" fill="var(--color-surface)" />
		<rect x="0" y="2" width={value} height="4" rx="2" fill="var(--data-fit)" />
	</svg>
	<p class="readout">value {value} of {MAX}</p>
</div>

<style>
	.rails-probe {
		background: var(--color-surface);
		border-radius: 8px;
		padding: 1.25rem 1.5rem;
		max-width: 28rem;
		width: 100%;
		box-sizing: border-box;
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

	input[type='range'] {
		flex: 1;
		min-height: 44px;
		accent-color: var(--color-brand-mint);
	}

	.gauge {
		display: block;
		width: 100%;
		height: 8px;
		margin-top: 0.5rem;
	}

	.readout {
		margin: 0.75rem 0 0;
		font-family: var(--font-mono), monospace;
		font-size: 0.85rem;
		color: var(--color-text);
		transition: opacity var(--motion-min-ms) var(--ease-out-quint);
	}

	@media (prefers-reduced-motion: reduce) {
		.readout {
			transition: none;
		}
	}
</style>
