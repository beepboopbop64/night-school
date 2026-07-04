---
session: attention
aha: "Attention is a soft lookup table."
audience: >-
  John Santerre's Berkeley MIDS and SMU MSDS grad students. Average age about
  31, employed, evenings only, applied maturity, heterogeneous and rusty math.
  They use LLMs at work and know Python dictionaries cold; they do not have
  fresh linear algebra. Assume intelligence, never fluency. Same voice as the
  KC exemplar, deeper math, just-in-time visual refreshers instead of
  remedial runway.
notebook: "yes: single-head attention fits in roughly 30 lines of NumPy, matching John's minimal-dependency code.py teaching pattern, and the aha is directly checkable in code (start from a hard dict lookup, relax it with softmax, watch attention fall out)."
videoTargetSeconds: 480
videoHardCapSeconds: 540
flaggedForJake:
  - id: D-O2
    decision: "Pilot scope is single-head dot-product attention only; multi-head and positional encoding move to the closing breadcrumb toward session 2."
    rationale: "One session, one aha: the soft-lookup claim is fully provable with a single head, and stacking heads or position on top before the lookup lands would break the one-new-idea-per-beat budget."
---

# Session brief: attention

## The aha, and how it could be wrong

**"Attention is a soft lookup table."** The claim is falsifiable, and the
session must earn it component by component:

- A dictionary lookup has a query (the key you ask with), stored keys, and
  stored values. Attention has exactly these three objects, by name.
- A hard lookup scores each stored key 0 or 1 against the query and returns
  one value. Attention scores each key continuously (dot product) and returns
  a weighted blend of all values (softmax mixing).
- The limit test: as score gaps grow (or temperature drops), softmax
  sharpens toward argmax and attention returns exactly the classic hard
  lookup. If any piece of the mechanism fails to map (queries, keys, values,
  scores, mixing, the hard-lookup limit), the metaphor is decoration and the
  session fails its own sentence.

The metaphor must survive beats 3 through 8 without strain: the compression
beat writes softmax(qK^T / sqrt(d_k))V as literally "the lookup, made soft,"
term by term, color by color.

## Hook candidates

At least one treatment per candidate at S2. Hook A is the frontrunner on
DOCTRINE's own criteria (real story, named people, dates, consequences), but
each opens a genuinely different gap.

### Hook A: The bottleneck that broke translation (real history, 2014)

**Cold open.** In 2014 the best neural translators read a whole sentence,
squeezed everything they understood into one fixed-size vector, then wrote
the translation from that vector alone. Quality collapsed as sentences got
longer, and Ilya Sutskever's team at Google found a strange hack that bought
real accuracy: feed the sentence in backwards. That same September, Dzmitry
Bahdanau, a visiting student in Yoshua Bengio's Montreal lab, proposed
something that was not a hack: stop compressing. Let the model look back at
every word, and learn, for each word it writes, where to look.

**The gap it opens.** "Where to look" is a choice, and choices are discrete,
and you cannot take a gradient through a discrete choice. So how do you make
looking learnable? The learner should feel the impossibility before the
resolution: the fix is to never actually choose. The fix outlived the
architecture it rescued; three years later "Attention Is All You Need" threw
away the recurrent network and kept only the fix.

**Names, dates, stakes.** Sutskever, Vinyals, Le (NeurIPS 2014, seq2seq,
fixed-vector bottleneck, source-reversal trick). Cho et al. 2014 (measured
the collapse on long sentences). Bahdanau, Cho, Bengio (arXiv Sept 2014,
ICLR 2015: attention as learned soft alignment). Vaswani et al. 2017.
Stakes: this one repair is now the load-bearing operation in every LLM these
students touch at work, and it shipped to a billion users when Google
Translate went neural in 2016.

**Needs S1 verification.** Exact reversal-trick numbers (BLEU or perplexity
deltas citable on screen); which Cho et al. paper and figure shows BLEU vs
sentence length (we want to redraw that curve in tokens); Bahdanau's exact
status in the Bengio lab and the arXiv 1409.0473 submission date; the
RNNsearch vs RNNencdec long-sentence figure; GNMT deployment date and a
citable source for the Google Translate switch.

### Hook B: The dictionary that fails gracefully (puzzle)

**Cold open.** Here is a data structure everyone in this room used this
week: the dictionary. `d["cat"]` returns a value; `d["feline"]` raises
KeyError, because the dictionary has no idea those are nearly the same
question. Now imagine a dictionary with partial credit: ask for "feline" and
it hands back mostly cat's value, a little of kitten's, essentially none of
carburetor's. What would that data structure even look like, and could a
model learn it?

**The gap it opens.** Two nested impossibilities: what does "partial credit
on a key match" mean, precisely, and how do you take a gradient through a
lookup? This hook is the aha inverted into a puzzle, which is its power and
its risk: **the treatment must withhold the identification until beat 5.**
Open only with the brittle-lookup obstruction; the learner should build the
forgiving dictionary piece by piece and only then be told the thing they
built has a famous name. If beat 1 says "this is attention," the aha is
narrated, not engineered, and the treatment fails.

**Names, dates, stakes.** No historical cast needed; the stakes are that
this forgiving dictionary is the core operation of every LLM. Real lineage
available if the treatment wants teeth: content-based soft addressing in
Neural Turing Machines (Graves et al. 2014), Memory Networks (Weston et al.
2014), Key-Value Memory Networks (Miller et al. 2016), and the query/key/
value vocabulary itself, which is retrieval-systems language.

**Needs S1 verification.** Whether Vaswani et al. or contemporaries
explicitly credit retrieval/database terminology for query, key, value; the
NTM and Memory Networks dates and the honest one-line version of that
lineage (we must not imply attention was invented as a database).

### Hook C: The heatmap that lied (wrong-looking result)

**Cold open.** A sentiment model reads a movie review, calls it negative,
and explains itself with a heatmap: attention weights glowing over the words
it looked at. In 2019 Sarthak Jain and Byron Wallace ran an uncomfortable
experiment: holding the model's prediction essentially fixed, they found
very different attention maps that supported the same answer. Same output,
contradictory explanations. If the heatmap can be swapped without changing
the model's mind, what was it ever telling you?

**The gap it opens.** The weights obviously do something, because the
mechanism works. So if they are not reasons, what is their actual job? The
resolution is the aha itself: they are the mixing weights of a soft lookup,
and asking them to be explanations is asking a hash function to justify
itself. This hook voices the session's primary misconception in beat 1,
which is exactly where Muller says it belongs for a misconception-prone
topic.

**Names, dates, stakes.** Jain and Wallace, "Attention is not Explanation"
(NAACL 2019); the rebuttal by Wiegreffe and Pinter, "Attention is not not
Explanation" (EMNLP 2019). Stakes: attention heatmaps still get shipped as
interpretability in model cards and product demos, including in domains
where a wrong explanation costs money or safety.

**Needs S1 verification.** The precise experimental claims and their scope
(the 2019 results are on specific RNN classification setups, not
transformers broadly; we need the defensible one-sentence version); the
rebuttal's actual counterclaim; whether Serrano and Smith 2019 belongs in
the account; a citable real-world example of an attention map presented as
an explanation, if a defensible one exists.

### Hook D (spare sketch, not a full candidate)

"The animal didn't cross the street because it was too tired." Swap "tired"
for "wide" and the referent of "it" flips; the learner resolves it
instantly, and the question is what machinery lets a model ask who "it" is
about. Provenance is Google's 2017 Transformer announcement, and every
attention explainer since has used it, which is the problem. Available to a
treatment as a beat-2 or beat-7 example, not as the cold open. S1: confirm
the sentence's provenance if used.

## Misconceptions to voice

All three seeded entries in `harness/checks/misconceptions.yaml` trigger on
this session's corpus. The storyboard must carry at least one
`misconceptionBeat: true` per L9; the primary one is non-negotiable.

1. **`attention-weights-are-explanations`** (primary, must be voiced and
   refuted before the correct account). High weight does not mean "this
   token caused the output." The soft-lookup framing is itself the
   refutation: mixing weights are plumbing, not reasons.
2. **`softmax-picks-the-max`**. Softmax discards nothing; it converts scores
   into a full probability-weighted blend. Voice it where softmax first
   appears (the compression beat), ideally with the temperature/sharpness
   limit that also proves the aha's hard-lookup correspondence.
3. **`similarity-means-identical`**. Dot-product similarity is alignment in
   a learned space, not sameness. Voice it at the elemental unit, where the
   qk-similarity seed already shows scores rising and dying with direction.

## Seeds to absorb

- `lessons/sessions/slice-attention/beat.yaml` (qk-similarity, PASSED the
  Iris loop): one query swept across four keys, scores as live bars. This is
  the elemental-unit beat, nearly verbatim.
- `lessons/sessions/slice-attention/interactive.yaml` (qk-explorer): the
  learner drags the query's angle and feels alignment become the score.
  Reference from the corresponding beat's `interactiveSpec`; this is the
  felt-obstruction candidate for the page track.

## Open questions for the researcher (S1)

1. Verify every fact flagged under the hooks above; kill any hook fact that
   cannot be sourced.
2. Find the single best citable quantitative artifact for the bottleneck
   story: a BLEU vs sentence-length curve we can honestly redraw with
   tokens, with paper and figure number.
3. The sqrt(d_k) scaling story: the variance argument in Vaswani et al.
   section 3.2.1, plus a tiny numeric example (d_k of 2 vs 64) we can show
   without cheating. This is a no-handwave callout candidate.
4. Prior-art audit for the fresh-angle statement: 3b1b's 2024 attention
   chapter, Jay Alammar's Illustrated Transformer, Karpathy's nanoGPT
   walkthrough. What does each already do, and what does our soft-lookup
   framing plus felt-obstruction interactive add that they lack?
5. The honest lineage of "soft lookup" (NTM, Memory Networks, Key-Value
   Memory Networks): one paragraph, dated, so hook B can carry real history
   without overclaiming.
6. What is the defensible scope of "attention maps are not faithful
   explanations" as of 2026? Any follow-up work that sharpens or softens
   Jain and Wallace for transformer-era models?
7. Worked micro-example numbers for the storyboard: a 4-token sentence with
   small integer-ish dot products where the softmax weights are legible on
   screen and the weighted blend is visibly "mostly one value, a little of
   the others."

## S0 gate self-check (ARCHITECTURE section 4)

- Aha stated as one falsifiable sentence in front-matter: yes, with the
  limit test that would falsify it.
- At least 2 concrete hook candidates: three full candidates plus one spare
  sketch; one (Hook A) is a real historical story with named people, dates,
  and stakes, verification flags marked.
- Audience statement matches John Santerre's student profile: yes
  (front-matter, per docs/research/05).
- Notebook candidacy recorded with reason: yes (front-matter).
- Scope decision recorded for Jake, never silently assumed: yes
  (`flaggedForJake`, D-O2).

```yaml
decision:
  id: d-s0-notebook-yes
  what: Commit the attention session to shipping a companion notebook.
  why: The aha is checkable in code (relax a hard dict lookup into softmax and attention appears), and John's own teaching pattern pairs every concept with minimal clean code.
  alternatives: ["no-notebook (rejected: this is the single topic on his frontier where running the math IS the retrieval act)"]
```

```yaml
decision:
  id: d-s0-hook-slate
  what: Send hooks A, B, and C to S2 as the three independently-steered treatment seeds, one hook per Story Writer.
  why: They open three genuinely different gaps (history, puzzle, wrong-looking result), which maximizes what best-of-3 judging can compare.
  alternatives: ["three treatments off hook A alone (rejected: converged drafts waste the best-of-3)", "hook D as a full candidate (rejected: most overused example in the genre; fails the fresh-angle bar as an opener)"]
```
