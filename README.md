# Night School — Sessions

*Advanced machine learning, after hours. Stories first. Rigor always. Kettle's on.*

This is the **product repo**: static-hostable Night School sessions (GitHub Pages compatible), produced by the [lesson-harness](../lesson_plan/) and reviewed by Jake in batched rounds. It deploys alone — the harness is never a runtime dependency of the site.

```
site/       SvelteKit + adapter-static + mdsvex shell aggregating all sessions
shared/     interactive primitives (TrueUp.svelte, progress line, video embed) · generated Manim style/colors
sessions/   one directory per session (brief -> storyboard -> tracks -> rounds -> state; see ARCHITECTURE.md §3)
metrics/    critic-misses.ndjson — the cross-session "critic passed it, Jake flagged it" ledger
FRICTION.md manual-work receipts: where operator time actually goes
```

Generated files (`site/src/styles/tokens.css`, `shared/manim/colors.py`) come from the harness's `config/tokens.json` and carry DO-NOT-EDIT headers. Raw hex literals fail CI in this repo.

Rendered video (`sessions/*/media/`) is gitignored — hosting is open decision D-O1 (resolved before first deploy; Git LFS on Pages is ruled out).
