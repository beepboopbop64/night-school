# S2 judgment: attention treatment best-of-3

Showrunner, 2026-07-04. Three candidates read in full against ARCHITECTURE
section 4 (S2 gate), DOCTRINE (arc, voice, NON-NEGOTIABLES), BRAND (tokens,
motif, vocabulary), and the S1 dossier (fact discipline). Verdict below,
then the scorecard, then per-candidate rationale, then the graft ledger.
Losers stay in this directory and ride in Jake's review packet appendix.

## Verdict

**Winner: `candidate-obstruction-first`, merged.** The merged treatment is
`../treatment.md`; the compiled spine is `../spine.md`.

```yaml
decision:
  id: d-s2-winner
  what: Ship obstruction-first as the treatment base, with named grafts from history-first and metaphor-first.
  why: It is the only candidate whose aha beat adds nothing new at the snap; the learner invents the escape in beat 4 and recognizes its identity in beat 5, which is the doctrine's engineered aha executed twice.
  alternatives:
    - "history-first (same verified facts and a superb hook, but it invents the softmax blend inside the aha beat, so B5 carries two new ideas and the snap is crowded)"
    - "metaphor-first (best honesty instruments and the best close in the field of three, but it drops the entire verified 2014 story: no named people, no collapse curve, no rescue payoff, so beats 1 and 5 run on charm instead of stakes)"
```

## Scorecard

Scored 0 to 5 per axis. Axes are the S2 gate criteria plus the judging
heuristics in the showrunner charter.

| Axis | history-first | obstruction-first | metaphor-first |
|---|---|---|---|
| Hook gate (care in 30s; question before definition; real story preferred) | 5.0 | 5.0 | 3.5 |
| Causal chain (each beat forces the next; 4 Cs) | 4.5 | 5.0 | 4.0 |
| Aha engineering (all components pre-established; snap, not narration) | 3.5 | 5.0 | 3.5 |
| Misconception beats (L9; voiced before correct account) | 5.0 | 5.0 | 4.5 |
| Honest metaphor and disclosure discipline | 4.5 | 4.5 | 5.0 |
| Technical correctness of on-screen numbers | 3.5 | 3.5 | 5.0 |
| Voice, humor landing bar, AI-tell hygiene | 4.5 | 5.0 | 4.5 |
| Pacing and budget (L10; grad-student altitude) | 4.0 | 4.5 | 4.5 |
| Brand fidelity (true-up, vocabulary, color discipline) | 4.5 | 4.0 | 4.5 |
| DOCTRINE fidelity overall (L-check self-audit quality) | 4.5 | 5.0 | 4.5 |
| **Total** | **43.5** | **46.0** | **43.5** |

Hard gates, all three candidates: hook exists (pass, pass, pass); no
fabricated autobiography (pass all three; see watch-item below); honest
metaphors (pass all three; metaphor-first sets the standard); aha sentence
honored verbatim, no substitution (pass all three).

## Per-candidate rationale

### obstruction-first (winner)

What it got right, and why it wins:

1. **The aha blocking is structurally superior.** The escape (exponentiate,
   normalize, blend) is built in beat 4 scene 2 as the resolution of the
   felt wall, so beat 5 opens with the machine already running and asks only
   "You have seen this shape before. Where?" Nothing new enters the aha
   beat. That is Danek executed to the letter: the learner self-connects
   twice, once inventing the mechanism, once recognizing its identity. The
   other two candidates make beat 5 do invention and recognition at once.
2. **The felt obstruction is the spine, not a stop on the tour.** The hard
   lookup answers perfectly and learns nothing, with a gradient meter
   flatlining on screen; the beat-2 cliff returns inside the toy with
   numbers on it. This is the doctrine's productive-failure demand at full
   strength, and it is what makes "stop choosing" feel inevitable.
3. **Best hook prose of the three.** Same verified 2014 story as
   history-first, but with rhythm, one landing joke that carries the
   absurdity claim ("what if the first words were just... closer"), and the
   dossier's causation caution executed visually (the Sep 1 / Sep 10
   timeline chip). "So the field kept squeezing. And an intern in Montreal
   decided to stop" is the best sentence in the competition.
4. **Cleanest self-audit.** Predictions P1 through P5 before every reveal,
   scene splits documented, disclosure ledger complete, trim plan named.

What it got wrong (all fixed in the merge):

1. **Numeric inconsistency (shared with history-first).** Beat 4.2 shows
   softmax on the raw scores 4, 2, 0, -4 and quotes weights 0.766 / 0.186 /
   0.045 / 0.003. Those weights are only correct after dividing scores by
   sqrt(2) (dossier 1.5). Unscaled, softmax gives roughly 0.867 / 0.117 /
   0.016 / 0.000. Fixed with metaphor-first's bookkeeping-factor move.
2. **Color discipline breach.** "Amber weight bars" in beats 4 and 5: the
   PASSED qk-similarity seed locks scores to lilac `data.params`, and
   weights are normalized scores, the same object family. Amber belongs to
   the query alone. Weights stay lilac; the heatmap-lookalike moment works
   on layout, not on stealing the query's color.
3. **The aha beat was still overloaded** with the GNMT deployment stakes
   (its own trim plan flags this). Stakes move to beat 8, where
   history-first proved they land harder as the closing payoff.
4. **No title.** Grafted from history-first.
5. **The hook lacked an explicit question line** (the question arrived at
   beat 2). One closing line added so NON-NEGOTIABLE 1 is satisfied inside
   beat 1 rather than by the technicality that no definitions precede it.

Watch-item for Vera, ruled allowed: the hook's "my favorite desperate hack
in the history of the field" is first-person taste, not a fabricated
anecdote or simulated access. The honesty rules ban invented events and
simulated vulnerability; a narrator with preferences is the KC voice
working. If it reads as costume at table-read, cut without appeal.

### history-first (second; loses on blocking, not on substance)

What it got right: the strongest hook discipline (rescue line withheld for
B5 payoff; the amber gaze dot planted 60 seconds in, seeding the query
color before anything is named: grafted); the stakes placed at the close
where they belong (grafted); the question-form title and surrealist-triplet
subtitle, both exactly to BRAND spec (grafted); landing line "Gradient
flows only while the lookup stays soft," which is the compression beat in
eight words (grafted); correct color assignments including values as
`data.truth` (adopted in the spine); the explicit KeyError code-well moment
in B4 (grafted, shared with metaphor-first).

Why it loses: the softmax blend is invented inside B5. The aha beat then
carries a new mechanism plus the dict recognition plus the misconception
refutation plus the history payoff in 70 seconds. The showrunner heuristic
is that the aha must be engineered, every component separately established
before the snap; history-first establishes the components of the LOOKUP
before B5 but not the components of the FIX. Obstruction-first hands the
learner the fix one beat earlier and keeps the snap pure. A strong hook
with a fixable middle beats a strong hook with a crowded aha, and both
hooks here are the same hook.

### metaphor-first (third; best instruments, weakest engine)

What it got right: the drift ledger, a per-row correspondence table with
exact / honest-analogy status for every metaphor claim, is the best honesty
instrument any candidate produced and goes into the spine nearly verbatim
(grafted); the sqrt(d_k) bookkeeping-factor catch, the one live technical
correction in the competition (grafted); the dual-heatmap morph visual, two
different lilac weight maps collapsing to the same output bar, which is the
strongest possible refutation image for the primary misconception
(grafted); the P6 true-or-false prediction before the 2019 verdict, which
the winner lacked (grafted); the most complete extensions menu, with
what-good-looks-like notes and the paired 2019 fight (merged); disciplined
silent-inference moments (sofa's negative score left unnarrated).

Why it loses: the hook gate. The recipe box and the 9pm kitchen are
charming, brand-adjacent, and honest, but the candidate trades away the
entire verified history: no named people, no dates, no collapse curve, no
first-try vindication, no production stakes. The doctrine's hook spec asks
for named people, dates, and consequences where possible, and here they are
not merely possible but verified, plotted, and sitting in the dossier with
a figure to redraw. Beat 5 also runs the most crowded of the three (blend
construction, shares, misconception, P3, reveal, causal-mask line, lineage
line in 70 seconds), and the bookkeeping factor, its own best catch, lands
mid-aha where a wart is most expensive. The recursive kitchen close ("the
lemon thing was never filed under L") is the best writing in any candidate
and cannot be grafted, because it depends on the hook we are not using. It
is the one real cost of this verdict.

## Graft ledger (what the merged treatment takes, and from where)

| # | Graft | From | Into |
|---|---|---|---|
| G1 | Pay 1/sqrt(d_k) at the blend with one forward-reference line so 0.766 / 0.186 / 0.045 / 0.003 are exact on screen | metaphor-first | B4.2 |
| G2 | Title "How Do You Take a Gradient Through a Choice?" + subtitle "One vector, five weeks, eight thousand numbers." | history-first | front matter |
| G3 | Amber gaze-dot in the hook, seeding the query color 60s before it is named | history-first | B1 |
| G4 | Explicit KeyError code well: d["feline"] dies one synonym from a key it is holding | history-first (and metaphor-first independently) | B4.1 |
| G5 | "kitten, noted... anyway, one hundred percent cat" carries the discarded-runner-up claim | metaphor-first | B4.1 |
| G6 | GNMT stakes move from the aha beat to the close; landing line "The fix outlived the architecture it rescued." | history-first | B5 -> B8 |
| G7 | Compression landing line "Gradient flows only while the lookup stays soft." | history-first | B6 |
| G8 | P6 true-or-false prediction before the Jain and Wallace reveal, plus the dual-heatmap morph and the session's single rose cross-out | metaphor-first | B7 |
| G9 | Drift ledger (metaphor registry with per-row honesty status) | metaphor-first | spine.md |
| G10 | Extensions menu merged: what-good-looks-like notes, paired 2019 fight, Nadaraya-Watson stretch | metaphor-first + obstruction-first | B8 / spine |
| G11 | Weights stay lilac everywhere (fixes winner's amber-bars breach); values locked to data.truth with a shape channel | history-first + seed | spine colors |
| G12 | Hook closes on an explicit question line | new (gate compliance) | B1 |

## Corrections applied to the winner (not grafts, rulings)

```yaml
decision:
  id: d-s2-scaling-at-blend
  what: Divide scores by sqrt(d_k) at the beat-4 blend with one honest forward reference, paid in full at the formula.
  why: The dossier's precomputed weights, the sharpening demo, and the notebook all assume scaled scores; showing unscaled softmax with those numbers would be false on screen.
  alternatives: ["recompute unscaled weights for beat 4 and rescale at beat 6 (rejected: two sets of weights on screen for the same example burns novelty budget and invites a continuity error)"]
```

```yaml
decision:
  id: d-s2-weights-stay-lilac
  what: Attention weights render in data.params lilac in every beat; amber is the query's alone.
  why: Weights are normalized scores, the same object family the PASSED seed locked to lilac; one color, one job, everywhere.
  alternatives: ["amber bars for the heatmap-lookalike moment (rejected: breaks the series color ledger for one visual pun)"]
```
