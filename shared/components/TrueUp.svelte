<!--
	TrueUp.svelte — the Night School signature motif (BRAND.md).

	An SVG path is born as a freehand sketch (low-frequency hand-jitter,
	~1.5–2px amplitude) and, on trigger, interpolates to the exact clean path
	over ~800ms on the True-Up ease. The Trued Mint glow blooms at the instant
	displacement hits zero.

	HARD RULE: never apply this to text. Sketchiness lives in lines, never letters.

	Fires once per component instance (a header underline trues once on load,
	never again). Re-mount with {#key} to replay.

	prefers-reduced-motion: no wobble — the sketch crossfades to the clean
	trued path, glow included.
-->
<script lang="ts">
	import { onMount } from 'svelte';

	interface Props {
		/** The clean SVG path data (the exact line the sketch trues into). */
		d: string;
		/** viewBox width in px units. */
		width?: number;
		/** viewBox height in px units. */
		height?: number;
		/** Rising edge starts the true-up. Defaults to true (trues on mount). */
		trigger?: boolean;
		/** Stroke color — a CSS var reference, never raw hex. */
		stroke?: string;
		/** Glow color at settle. */
		glowColor?: string;
		strokeWidth?: number;
		/** Displacement amplitude in px (brand spec: 1.5–2). */
		amplitude?: number;
		/** True-up duration in ms (brand spec: 800). */
		durationMs?: number;
		/** Noise seed, for a stable sketch across re-renders. */
		seed?: number;
		/** If the SVG is scaled by CSS, stretch to fill. */
		class?: string;
	}

	let {
		d,
		width = 320,
		height = 24,
		trigger = true,
		stroke = 'var(--color-brand-mint)',
		glowColor = 'var(--color-brand-mint)',
		strokeWidth = 2.5,
		amplitude = 1.8,
		durationMs = 800,
		seed = 7,
		class: className = ''
	}: Props = $props();

	/** Path currently rendered: sketch before/through the true-up, clean after. */
	let renderedD = $state(d);
	/** Glow bloom opacity 0..1; blooms exactly when displacement hits zero. */
	let glow = $state(0);
	/** Crossfade state for reduced motion. */
	let reducedMotion = $state(false);
	let crossfade = $state(false);
	let sketchD = $state('');

	let pathEl: SVGPathElement | undefined = $state();
	// $state so the trigger effect re-fires once sampling completes, regardless
	// of effect ordering.
	let sampled: Sampled | null = $state(null);
	let started = false;
	let raf = 0;

	/** easeOutQuint — the True-Up ease (motion.easeOutQuint token). */
	const ease = (t: number): number => 1 - Math.pow(1 - t, 5);

	/** Deterministic pseudo-random in [-1, 1). */
	function prand(i: number): number {
		const x = Math.sin(i * 127.1 + seed * 311.7) * 43758.5453;
		return (x - Math.floor(x)) * 2 - 1;
	}

	interface Sampled {
		pts: { x: number; y: number }[];
		normals: { x: number; y: number }[];
		offsets: number[];
	}

	/** Sample the clean path; precompute per-point normals and jitter offsets. */
	function sample(el: SVGPathElement): Sampled {
		const total = el.getTotalLength();
		const step = Math.max(4, Math.min(8, total / 48));
		const n = Math.max(2, Math.ceil(total / step) + 1);
		const pts: { x: number; y: number }[] = [];
		for (let i = 0; i < n; i += 1) {
			const p = el.getPointAtLength((total * i) / (n - 1));
			pts.push({ x: p.x, y: p.y });
		}
		const normals = pts.map((p, i) => {
			const a = pts[Math.max(0, i - 1)];
			const b = pts[Math.min(pts.length - 1, i + 1)];
			const dx = b.x - a.x;
			const dy = b.y - a.y;
			const len = Math.hypot(dx, dy) || 1;
			return { x: -dy / len, y: dx / len };
		});
		// Low-frequency wobble: two incommensurate sines along arclength plus a
		// pinch of per-point grain. Endpoints stay pinned — a sketch still starts
		// and ends where it means to.
		const p1 = prand(1) * Math.PI;
		const p2 = prand(2) * Math.PI;
		const offsets = pts.map((_, i) => {
			const s = (total * i) / (pts.length - 1);
			const pin = Math.min(1, (Math.min(i, pts.length - 1 - i) / (pts.length - 1)) * 6);
			const wave = Math.sin(s / 26 + p1) * 0.62 + Math.sin(s / 71 + p2) * 0.38;
			return (wave + prand(i + 10) * 0.22) * pin;
		});
		return { pts, normals, offsets };
	}

	/** Path data for the sketch at displacement scale k (k=1 rough, k=0 clean). */
	function sketchPath(s: Sampled, k: number): string {
		const parts = s.pts.map((p, i) => {
			const off = s.offsets[i] * amplitude * k;
			const x = (p.x + s.normals[i].x * off).toFixed(2);
			const y = (p.y + s.normals[i].y * off).toFixed(2);
			return `${i === 0 ? 'M' : 'L'}${x} ${y}`;
		});
		return parts.join(' ');
	}

	/** Bloom the mint glow: sharp rise the instant displacement hits zero, then settle. */
	function bloom(start: number, now: number): number {
		const t = now - start;
		const rise = 240;
		const settleAt = 0.45; // steady settle-glow
		if (t <= rise) return ease(t / rise);
		const decay = Math.min(1, (t - rise) / 500);
		return 1 - (1 - settleAt) * ease(decay);
	}

	function trueUp(): void {
		if (started || !sampled) return;
		started = true;
		const s = sampled;

		if (reducedMotion) {
			// Crossfade, no wobble: the static sketch fades out, clean+glow fade in.
			requestAnimationFrame(() => {
				crossfade = true;
				glow = 0.45;
			});
			return;
		}

		let t0 = 0;
		let bloomStart = 0;
		const frame = (now: number): void => {
			if (t0 === 0) t0 = now;
			const t = Math.min(1, (now - t0) / durationMs);
			const k = 1 - ease(t);
			renderedD = k > 0.001 ? sketchPath(s, k) : d;
			if (t >= 1) {
				if (bloomStart === 0) bloomStart = now;
				glow = bloom(bloomStart, now);
				if (now - bloomStart >= 760) {
					glow = 0.45;
					return; // settled
				}
			}
			raf = requestAnimationFrame(frame);
		};
		raf = requestAnimationFrame(frame);
	}

	// Mount: sample the clean path once, then the line is BORN ROUGH (a sketch)
	// until the trigger trues it. onMount (not $effect) so writing `sampled`
	// cannot re-run this block and cancel a live animation.
	onMount(() => {
		reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		if (pathEl) {
			sampled = sample(pathEl);
			sketchD = sketchPath(sampled, 1);
			if (!reducedMotion) renderedD = sketchD;
		}
		return () => cancelAnimationFrame(raf);
	});

	$effect(() => {
		if (trigger && sampled) trueUp();
	});

	const filterId = `trueup-glow-${Math.random().toString(36).slice(2, 9)}`;
</script>

<svg
	class={className}
	viewBox="0 0 {width} {height}"
	width={width}
	height={height}
	fill="none"
	aria-hidden="true"
	overflow="visible"
>
	<defs>
		<filter id={filterId} x="-40%" y="-400%" width="180%" height="900%">
			<feGaussianBlur stdDeviation="3.2" />
		</filter>
	</defs>

	{#if reducedMotion && sketchD}
		<path
			d={sketchD}
			stroke={stroke}
			stroke-width={strokeWidth}
			stroke-linecap="round"
			class="xfade"
			style:opacity={crossfade ? 0 : 1}
		/>
	{/if}

	<!-- Trued Mint settle-glow: blooms at the instant displacement hits zero. -->
	<path
		d={renderedD}
		stroke={glowColor}
		stroke-width={strokeWidth * 2.6}
		stroke-linecap="round"
		filter="url(#{filterId})"
		class:xfade={reducedMotion}
		style:opacity={glow * 0.85}
	/>

	<path
		bind:this={pathEl}
		d={renderedD}
		stroke={stroke}
		stroke-width={strokeWidth}
		stroke-linecap="round"
		class:xfade={reducedMotion}
		style:opacity={reducedMotion ? (crossfade ? 1 : 0) : 1}
	/>
</svg>

<style>
	svg {
		display: block;
	}

	.xfade {
		transition: opacity var(--motion-true-up-ms, 800ms) ease;
	}
</style>
