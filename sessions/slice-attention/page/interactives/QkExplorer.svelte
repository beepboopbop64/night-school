<script>
  const KEYS = [
    { id: 'k1', angle: 20 },
    { id: 'k2', angle: 70 },
    { id: 'k3', angle: 110 },
    { id: 'k4', angle: 160 },
  ];

  const MIN = 0;
  const MAX = 360;
  const STEP = 5;
  const CX = 150;
  const CY = 150;
  const R = 108;
  const TRACK_H = 150;

  let queryAngle = $state(90);
  let sliderEl = $state(null);
  let dragging = $state(false);

  function clamp(v) {
    return Math.max(MIN, Math.min(MAX, v));
  }

  function toRad(deg) {
    return (deg * Math.PI) / 180;
  }

  function pointOnCircle(angleDeg, radius) {
    const rad = toRad(angleDeg);
    return {
      x: CX + radius * Math.cos(rad),
      y: CY - radius * Math.sin(rad),
    };
  }

  function labelPoint(angleDeg, radiusOffset = 24) {
    return pointOnCircle(angleDeg, R + radiusOffset);
  }

  function arrowPoints(angleDeg) {
    const tip = pointOnCircle(angleDeg, R);
    const rad = toRad(angleDeg);
    const dx = Math.cos(rad);
    const dy = -Math.sin(rad);
    const px = -dy;
    const py = dx;
    const size = 15;
    const half = 6.5;
    const baseX = tip.x - dx * size;
    const baseY = tip.y - dy * size;
    const leftX = baseX + px * half;
    const leftY = baseY + py * half;
    const rightX = baseX - px * half;
    const rightY = baseY - py * half;
    return `${tip.x},${tip.y} ${leftX},${leftY} ${rightX},${rightY}`;
  }

  function fmt(n) {
    const v = Math.abs(n) < 0.005 ? 0 : n;
    return v.toFixed(2);
  }

  function barHeight(score) {
    return Math.abs(score) * (TRACK_H / 2);
  }

  function barTop(score) {
    const h = barHeight(score);
    return score >= 0 ? TRACK_H / 2 - h : TRACK_H / 2;
  }

  let queryTip = $derived(pointOnCircle(queryAngle, R));

  // When the query lines up with a key, its label would land right on top
  // of the key's label. Nudge the query label around the circle so the two
  // never collide, however close the vectors get.
  function queryLabelAngle(angle) {
    let nudged = angle;
    for (const k of KEYS) {
      let delta = ((angle - k.angle + 540) % 360) - 180;
      if (Math.abs(delta) < 16) {
        nudged = angle + (delta >= 0 ? 22 : -22);
        break;
      }
    }
    return nudged;
  }

  let scores = $derived.by(() => {
    const raw = KEYS.map((k) => {
      const diff = toRad(queryAngle - k.angle);
      return { id: k.id, angle: k.angle, score: Math.cos(diff) };
    });
    const max = Math.max(...raw.map((r) => r.score));
    return raw.map((r) => ({ ...r, leading: r.score >= max - 0.0001 }));
  });

  function setAngleFromClient(clientX, clientY) {
    if (!sliderEl) return;
    const rect = sliderEl.getBoundingClientRect();
    const cx = rect.left + rect.width / 2;
    const cy = rect.top + rect.height / 2;
    const dx = clientX - cx;
    const dy = cy - clientY;
    let angle = (Math.atan2(dy, dx) * 180) / Math.PI;
    if (angle < 0) angle += 360;
    queryAngle = clamp(Math.round(angle));
  }

  function onPointerDown(e) {
    dragging = true;
    if (sliderEl && sliderEl.setPointerCapture) {
      try {
        sliderEl.setPointerCapture(e.pointerId);
      } catch (err) {
        /* ignore */
      }
    }
    setAngleFromClient(e.clientX, e.clientY);
  }

  function onPointerMove(e) {
    if (!dragging) return;
    setAngleFromClient(e.clientX, e.clientY);
  }

  function endDrag(e) {
    dragging = false;
    if (sliderEl && sliderEl.releasePointerCapture && e && e.pointerId != null) {
      try {
        sliderEl.releasePointerCapture(e.pointerId);
      } catch (err) {
        /* ignore */
      }
    }
  }

  function onKeydown(e) {
    let next = queryAngle;
    if (e.key === 'ArrowRight' || e.key === 'ArrowUp') {
      next = clamp(queryAngle + STEP);
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') {
      next = clamp(queryAngle - STEP);
    } else if (e.key === 'Home') {
      next = MIN;
    } else if (e.key === 'End') {
      next = MAX;
    } else {
      return;
    }
    e.preventDefault();
    queryAngle = next;
  }
</script>

<div class="qk-root" data-interactive="qk-explorer">
  <p class="instruction">Turn q until it lines up with a key.</p>

  <div
    class="diagram"
    role="slider"
    tabindex="0"
    bind:this={sliderEl}
    aria-valuemin={MIN}
    aria-valuemax={MAX}
    aria-valuenow={queryAngle}
    aria-valuetext={`${queryAngle} degrees`}
    aria-label="Query angle in degrees"
    onpointerdown={onPointerDown}
    onpointermove={onPointerMove}
    onpointerup={endDrag}
    onpointercancel={endDrag}
    onkeydown={onKeydown}
  >
    <svg viewBox="0 0 300 300" aria-hidden="true">
      <circle class="guide" cx={CX} cy={CY} r={R} />
      <circle class="center-dot" cx={CX} cy={CY} r="3.5" />

      {#each scores as s (s.id)}
        {@const tip = pointOnCircle(s.angle, R)}
        {@const lbl = labelPoint(s.angle)}
        <line
          class="key-line"
          class:leading={s.leading}
          x1={CX}
          y1={CY}
          x2={tip.x}
          y2={tip.y}
        />
        <circle class="key-dot" class:leading={s.leading} cx={tip.x} cy={tip.y} r="5" />
        <text class="label-text key-label" x={lbl.x} y={lbl.y} text-anchor="middle" dominant-baseline="middle">
          {s.id}
        </text>
      {/each}

      <line class="query-line" x1={CX} y1={CY} x2={queryTip.x} y2={queryTip.y} />
      <polygon class="query-arrow" points={arrowPoints(queryAngle)} />
      {#each [labelPoint(queryLabelAngle(queryAngle))] as lbl}
        <text class="label-text query-label" x={lbl.x} y={lbl.y} text-anchor="middle" dominant-baseline="middle">
          q
        </text>
      {/each}
    </svg>
  </div>

  <p class="angle-readout">q = <span class="angle-value">{queryAngle}</span> deg</p>

  <div class="scores-row">
    {#each scores as s (s.id)}
      <div class="score-col">
        <span class="score-label">{s.id}</span>
        <div class="bar-track">
          <div class="baseline"></div>
          <div
            class="bar-fill"
            class:leading={s.leading}
            style={`top:${barTop(s.score)}px; height:${barHeight(s.score)}px;`}
          ></div>
        </div>
        <span class="score-value" class:leading={s.leading}>{fmt(s.score)}</span>
      </div>
    {/each}
  </div>
</div>

<style>
  .qk-root,
  .qk-root * {
    box-sizing: border-box;
  }

  .qk-root {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    width: 100%;
    max-width: 640px;
    margin: 0 auto;
    padding: 1.25rem;
    background: var(--color-bg);
    color: var(--color-text);
    font-family: var(--font-body);
  }

  .instruction {
    margin: 0;
    font-size: 0.95rem;
    opacity: 0.8;
    text-align: center;
  }

  .diagram {
    position: relative;
    width: 100%;
    max-width: 420px;
    min-width: 220px;
    aspect-ratio: 1 / 1;
    touch-action: none;
    cursor: grab;
    border-radius: 8px;
  }

  .diagram:active {
    cursor: grabbing;
  }

  .diagram:focus-visible {
    outline: 2px solid var(--data-heat);
    outline-offset: 6px;
  }

  .diagram svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  .guide {
    fill: none;
    stroke: var(--color-text);
    opacity: 0.15;
    stroke-width: 1;
  }

  .center-dot {
    fill: var(--color-text);
    opacity: 0.4;
  }

  .key-line {
    stroke: var(--data-observed);
    stroke-width: 2.5;
    opacity: 0.55;
  }

  .key-line.leading {
    stroke-width: 4;
    opacity: 1;
  }

  .key-dot {
    fill: var(--data-observed);
    opacity: 0.7;
  }

  .key-dot.leading {
    opacity: 1;
  }

  .query-line {
    stroke: var(--data-heat);
    stroke-width: 4.5;
    stroke-linecap: round;
  }

  .query-arrow {
    fill: var(--data-heat);
  }

  .label-text {
    font-family: var(--font-mono);
    fill: var(--color-text);
    font-size: 15px;
  }

  .query-label {
    font-size: 16px;
    font-weight: 700;
  }

  .angle-readout {
    margin: 0;
    font-family: var(--font-mono);
    font-size: 1rem;
    color: var(--data-heat);
  }

  .angle-value {
    font-variant-numeric: tabular-nums;
  }

  .scores-row {
    display: flex;
    width: 100%;
    max-width: 520px;
    justify-content: space-between;
    gap: 0.6rem;
    margin-top: 0.25rem;
  }

  .score-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.4rem;
    flex: 1 1 0;
    min-width: 0;
  }

  .score-label {
    font-family: var(--font-mono);
    font-size: 0.85rem;
    color: var(--color-text);
    opacity: 0.85;
  }

  .bar-track {
    position: relative;
    width: 100%;
    max-width: 46px;
    height: 150px;
  }

  .baseline {
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    height: 1px;
    background: var(--color-text);
    opacity: 0.25;
  }

  .bar-fill {
    position: absolute;
    left: 0;
    right: 0;
    background: var(--data-params);
    border-radius: 3px;
    opacity: 0.75;
  }

  .bar-fill.leading {
    opacity: 1;
  }

  .score-value {
    font-family: var(--font-mono);
    font-size: 0.95rem;
    color: var(--data-params);
    font-variant-numeric: tabular-nums;
    opacity: 0.8;
  }

  .score-value.leading {
    opacity: 1;
    font-weight: 700;
  }

  @media (prefers-reduced-motion: reduce) {
    .qk-root * {
      transition: none !important;
      animation: none !important;
    }
  }
</style>
