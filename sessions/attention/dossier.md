# S1 dossier: attention

Session: `attention`. Aha: "Attention is a soft lookup table."
Researcher pass, 2026-07-04. Every load-bearing claim below has an entry in
`sources.yaml` with a resolving URL. Quotes are verbatim from the cited
source unless marked as paraphrase. One hook claim FAILED verification and
one is PARTIAL; both are itemized in section 8 before anything else uses
them.

---

## 1. The mechanism, correctly

### 1.1 Objects and dimensions

For a sequence of n tokens, each token carries a representation
x_i in R^(d_model). Three learned projection matrices turn each x_i into
three roles:

- query q_i = x_i W_Q, with q_i in R^(d_k): the question this token asks.
- key k_j = x_j W_K, with k_j in R^(d_k): the label under which token j can
  be found.
- value v_j = x_j W_V, with v_j in R^(d_v): the content token j hands over
  when found.

In Vaswani et al.'s base model, d_model = 512 and each head uses
d_k = d_v = 64. The canonical definition, verbatim from section 3.2: "An
attention function can be described as mapping a query and a set of
key-value pairs to an output, where the query, keys, values, and output are
all vectors."

### 1.2 The computation, three steps

1. Score every key against the query: e_j = (q . k_j) / sqrt(d_k).
2. Normalize scores to mixing weights: a_j = softmax(e)_j =
   exp(e_j) / sum_m exp(e_m). All a_j are positive and sum to 1.
3. Blend the values: out = sum_j a_j v_j.

Matrix form for all queries at once: Attention(Q, K, V) =
softmax(Q K^T / sqrt(d_k)) V. Every token's output is a weighted average of
value vectors; nothing is selected, nothing is discarded.

The dictionary correspondence, term by term:

| Python dict            | Attention                                  |
|------------------------|--------------------------------------------|
| the key you ask with   | query q                                    |
| stored keys            | keys k_1..k_n                              |
| stored values          | values v_1..v_n                            |
| exact match (0 or 1)   | continuous score q . k_j / sqrt(d_k)       |
| return one value       | return softmax-weighted blend of all values |
| KeyError on miss       | no miss is possible; weights just spread    |
| unordered              | permutation of (k_j, v_j) pairs leaves the output unchanged |

The last row is exact and useful: a dict has no notion of order, and neither
does dot-product attention. Reordering the key-value pairs permutes the
weights identically, so the blend is unchanged. This is why transformers
need positional encoding, which is the session's closing breadcrumb (D-O2).

### 1.3 Why sqrt(d_k): the no-handwave pack

Vaswani et al., section 3.2.1: "We suspect that for large values of d_k,
the dot products grow large in magnitude, pushing the softmax function into
regions where it has extremely small gradients." Their footnote 4 gives the
variance argument: "assume that the components of q and k are independent
random variables with mean 0 and variance 1. Then their dot product ... has
mean 0 and variance d_k." So the typical score magnitude grows like
sqrt(d_k), and dividing by sqrt(d_k) restores unit variance at every width.

Numeric demonstration (checkable by hand or in the notebook):

- d_k = 2: typical scores near +/- sqrt(2) = 1.41. softmax([1.41, -1.41]) =
  [0.944, 0.056]. Gradients are healthy.
- d_k = 64: typical scores near +/- 8. softmax([8, -8]) =
  [0.9999997, 0.0000003]. The softmax gradient factor w(1 - w) for the top
  weight is about 3e-7: the layer is effectively frozen for learning.
- Divide both by sqrt(64) = 8: softmax([1, -1]) = [0.881, 0.119], gradient
  factor about 0.105. Same relative preference, alive again.

Honest framing for the writers: the paper says "We suspect"; the variance
argument is exact, the gradient story is the authors' motivated hypothesis,
and it is standard practice, not a proven optimum.

### 1.4 The hard-lookup limit: what makes the aha falsifiable

Scale all scores by 1/T before the softmax (T is a temperature; this is a
property of softmax, not a dial that exists in the transformer; disclose
that). As T -> 0, the largest score's weight goes to 1 and all others to 0
(with ties splitting evenly). Two-line argument: softmax(e/T)_j =
1 / sum_m exp((e_m - e_j)/T); for the argmax, every exponent goes to
-infinity, so the sum goes to 1.

So the classic hard dict lookup is exactly the T -> 0 (or large score gap)
limit of attention, and attention is the differentiable relaxation of the
lookup. This is the falsification test the brief demands: if any component
failed to map (it does not), the metaphor would be decoration. The same
limit also shows why the hard version is unlearnable: at the limit, the
gradient factor w(1 - w) is 0. Gradient flows only while the lookup stays
soft.

Textbook support for the correspondence (this analogy has prior art; see
section 6): d2l.ai defines Attention(q, D) = sum_i alpha(q, k_i) v_i over a
database D of key-value pairs and notes the special case where "exactly one
of the weights alpha(q, k_i) is 1, while all others are 0. This is akin to a
traditional database query."

### 1.5 Worked micro-example (storyboard-ready numbers)

d_k = 2 so it matches the qk-explorer's draggable 2D geometry. The learner
asks for something cat-like ("feline"). Four stored tokens. All numbers
below are exact to the shown precision (computed, not invented).

- Query: q = [2, 0]
- Keys: cat [2, 0]; kitten [1, 1]; car [0, 2]; sofa [-2, 0]
- Values: cat [1.0, 0.0]; kitten [0.8, 0.2]; car [0.0, 1.0]; sofa [-1.0, 0.0]

| token  | q . k | / sqrt(2) | softmax weight |
|--------|-------|-----------|----------------|
| cat    | 4     | 2.83      | 0.766          |
| kitten | 2     | 1.41      | 0.186          |
| car    | 0     | 0.00      | 0.045          |
| sofa   | -4    | -2.83     | 0.003          |

Output = 0.766 [1, 0] + 0.186 [0.8, 0.2] + 0.045 [0, 1] + 0.003 [-1, 0]
= [0.912, 0.083]: mostly cat's value, a little kitten, essentially none of
car or sofa. This is the brief's "partial credit" made numeric.

The two payoffs from the same numbers:

- Softmax did not pick the max: the top weight is 0.766, not 1. Weight
  0.186 of kitten is still in the answer.
- Sharpen the scores by 5x (T = 0.2): weights become
  [0.9992, 0.0008, 0.000001, 0.0000000]. Sharpen by 20x: [1, 0, 0, 0] to
  eight decimal places. The dict lookup reappears on screen.

### 1.6 Simplifications the session will adopt (disclose each)

1. Single head only. Real transformers run h heads in parallel (h = 8 in
   the base model) and concatenate. Our "single head with learned W_Q, W_K,
   W_V" is exactly their multi-head machinery with h = 1. (D-O2 breadcrumb.)
2. No positional encoding. Without it the mechanism is order-blind (section
   1.2); honest because the dict is order-blind too, and the fix is session
   2's opening problem.
3. No causal mask. Decoder-only LLMs zero out future keys before the
   softmax (set scores to -infinity). One sentence of honesty when the LLM
   connection is made; the mechanism is otherwise unchanged.
4. Temperature is pedagogy. The transformer has no temperature knob in the
   attention layer; the sqrt(d_k) divisor is the fixed, principled cousin.
   Say "scale the scores" and the claim stays true.
5. Historical scoring differences. Bahdanau 2014 scored with a small
   feedforward net, a(s_{i-1}, h_j) = v_a^T tanh(W_a s_{i-1} + U_a h_j),
   not a dot product; plain dot-product scoring was catalogued by Luong et
   al. 2015 (their section 3.1: dot, general, concat) and scaled by Vaswani
   et al. 2017. If the video shows softmax(qk/sqrt(d_k)) over the 2014
   story, one line of disclosure is owed.
6. In Vaswani et al., the learned projections are introduced with
   multi-head attention; scaled dot-product attention itself takes Q, K, V
   as given. Fold this into disclosure 1.

---

## 2. Story candidates (all facts verified; URLs in sources.yaml)

### Candidate A: The bottleneck that broke translation (frontrunner)

The story in five sentences. In 2014 the best neural translator (Sutskever,
Vinyals, and Le at Google, NIPS 2014) read a whole sentence and squeezed it
into one fixed-size vector before writing the translation; their deep LSTM
represented any sentence, however long, as 8000 real numbers. Cho, van
Merrienboer, Bahdanau, and Bengio measured what that costs (arXiv Sep 3,
2014): performance "degrades rapidly as the length of the sentence and the
number of unknown words increase." Sutskever's team had bought accuracy
with a strange hack, feeding the source sentence in backwards, which
dropped a single LSTM's test perplexity from 5.8 to 4.7 and raised its BLEU
from 25.9 to 30.6 on WMT'14 English to French. That same September (arXiv
v1, Sep 1, 2014; ICLR 2015 oral), Dzmitry Bahdanau, an intern in Yoshua
Bengio's Montreal lab, posted the fix that was not a hack: stop
compressing, keep every encoder state, and let the decoder learn where to
look; his RNNsearch-50 scored 26.75 BLEU against the encoder-decoder's
17.82 and showed "no performance deterioration even with sentences of
length 50 or more." The fix outlived the architecture it rescued: Google
Translate went neural in production in September 2016 (Chinese to English,
about 18 million translations a day, on a service with more than 500
million users translating over 100 billion words a day), and in 2017
Vaswani et al. threw away the recurrence and kept only attention.

Why it maps: "where to look" is discrete and gradients need continuity; the
resolution is that the model never actually chooses, it blends, and the
blend is the soft lookup. Bahdanau's own account (email published by
Karpathy, Dec 2024, with permission) supplies the human beat: an MSc intern
from Jacobs University with about five weeks left in his internship,
inspired by his own eye movements ("Your gaze shifts back and forth between
source and target sequence as you translate," as quoted in the published
correspondence), implemented softmax-weighted averaging, and it worked on
the first try; he called it RNNSearch, and "The better name (attention) was
only added by Yoshua to the conclusion in one of the final passes."
(Wrinkle for accuracy: the phrase "mechanism of attention" does appear in
the paper's section 3.1, so deliver the naming anecdote as Bahdanau's
recollection, not as a claim that the word appears only in the conclusion.)

On-screen artifacts, verified: Bahdanau et al. Figure 2, caption "The BLEU
scores of the generated translations on the test set with respect to the
lengths of the sentences" (RNNsearch-50 flat, RNNencdec collapsing); Table
1 (RNNencdec-50: 17.82 all / 26.71 no unknown words; RNNsearch-50: 26.75 /
34.16); the reversal numbers above; Cho et al.'s BLEU vs length figure
(caption "The BLEU scores achieved by (a) the RNNenc and (b) the grConv for
sentences of a given length"; numbered Figure 4 in the ar5iv rendering;
re-check the figure number in the anthology PDF before putting a number on
screen).

Caution flags: do not say "a billion users" (FAILED, section 8); do not
imply Bahdanau was reacting to Sutskever's paper (Bahdanau's arXiv v1 of
Sep 1 precedes seq2seq's arXiv v1 of Sep 10; the bottleneck he attacked was
in Cho et al.'s June 2014 encoder-decoder, a paper he is on); attribute the
reversal numbers to a single LSTM (the famous 34.8 BLEU is a 5-LSTM
ensemble with reversal); lineage priority is publicly contested by
Schmidhuber (fast-weight programmers, 1992), while Bahdanau's account says
the idea emerged independently; the session does not need to adjudicate,
and if the history is told, "independently discovered soft-memory ideas
were in the air in 2014" is the safe true sentence.

### Candidate C: The heatmap that lied (verified, scope-disciplined)

The story in five sentences. By 2016, attention weights were being sold as
interpretability, most visibly in medicine: RETAIN (NIPS 2016) promised
clinicians "a two-level neural attention model that detects influential
past visits and significant clinical variables within those visits." In
NAACL 2019, Sarthak Jain and Byron Wallace trained standard BiLSTM
attention classifiers across eight datasets (sentiment, clinical notes from
MIMIC, QA, NLI) and asked whether the heatmap was the reason for the
prediction. They found "learned attention weights are frequently
uncorrelated with gradient-based measures of feature importance" and that
one "can identify very different attention distributions that nonetheless
yield equivalent predictions"; in their words, "one cannot conclude that
the model made a particular prediction because it attended over inputs in a
specific way." The debate then sharpened rather than settled: Serrano and
Smith (ACL 2019) found attention weights only noisily predict input
importance (paraphrase), while Wiegreffe and Pinter's "Attention is not not
Explanation" (EMNLP 2019) showed the adversarial maps "don't perform well
on the simple diagnostic, indicating that prior work does not disprove the
usefulness of attention mechanisms for explainability," and Bibal et al.
(ACL 2022) mapped a whole unresolved literature. The resolution is the
session's aha: the weights are the mixing coefficients of a soft lookup,
plumbing rather than reasons, and asking plumbing to justify the house is a
category error.

Why it maps: the misconception IS the primary seeded misconception, voiced
in beat 1 exactly where Muller wants it, and the refutation is not a
patch but the correct account of the mechanism.

Defensible one-sentence scope (writers must not overclaim): on BiLSTM
classifiers for classification, QA, and NLI (explicitly not seq2seq, not
transformers), attention weights correlated weakly with other importance
measures and could often be swapped for very different distributions
without changing predictions; Jain and Wallace themselves write that the
relationship "is not obvious, at least for RNN encoders," and "we have not
considered seq2seq tasks."

### Candidate B (lineage teeth for the puzzle hook): the twice-found dictionary

The honest one-paragraph history, dated. In 2014 the differentiable-memory
idea surfaced at least twice, independently. In Montreal (arXiv Sep 1,
2014), Bahdanau, Cho, and Bengio made a translator "(soft-)search for parts
of a source sentence," softmax-weighting encoder states; by Bahdanau's own
published account this was not influenced by other memory papers. At
DeepMind and Facebook that same fall, Neural Turing Machines (arXiv Oct 20,
2014) coupled networks to memory "by attentional processes ...
differentiable end-to-end," and Memory Networks (arXiv Oct 15, 2014; ICLR
2015) trained a long-term memory that "can be read and written to." The
explicit key-value split arrived with Key-Value Memory Networks (arXiv Jun
9, 2016; EMNLP 2016), "utilizing different encodings in the addressing and
output stages of the memory read operation": address by key, answer with
value. Vaswani et al. (2017) then defined attention as "mapping a query and
a set of key-value pairs to an output" and made it the whole architecture;
the paper uses retrieval-flavored vocabulary but credits no database
lineage, so say the terminology "matches how retrieval systems talk," never
that attention was borrowed from databases (see section 8). Textbooks
closed the loop later: d2l.ai now teaches attention as a generalization of
querying a database of key-value pairs, hard exact-match lookup being the
one-hot special case.

---

## 3. Misconception list (learner's voice, then the refutation)

All three seeded ids in `harness/checks/misconceptions.yaml` trigger on
this corpus. Placement per the brief; the primary is non-negotiable.

1. `attention-weights-are-explanations` (primary; voice in beat 1 if hook C
   leads, and before the correct account regardless).
   Learner's voice: "The model put 40 percent of its attention on
   'terrible', so 'terrible' is 40 percent of why it said negative."
   Refutation: weights are the mixing coefficients of a soft lookup, not a
   causal account. Empirically (BiLSTM classifiers): weights correlate
   weakly with gradient and leave-one-out importance, and very different
   maps can yield the same prediction (Jain and Wallace 2019); the debate
   over when they do explain is real and unresolved (Wiegreffe and Pinter
   2019; Serrano and Smith 2019; Bibal et al. 2022). The mechanism-level
   point needs no experiment: a weighted average's coefficients tell you
   what was blended, not why the recipe was chosen; the why lives in W_Q
   and W_K, which built the scores.

2. `softmax-picks-the-max` (voice where softmax first appears, the
   compression beat).
   Learner's voice: "Softmax is just a smooth argmax; it picks the winner."
   Refutation: nothing is discarded. In the micro-example the winner gets
   0.766 and the runner-up's 0.186 is measurably in the output. Sharpness
   is a function of score gaps (and any scaling): multiply the scores by 5
   and the weights become 0.9992 / 0.0008; only in the limit does the hard
   lookup reappear. This limit is simultaneously the proof of the aha and
   the refutation of the misconception; spend it once, on screen.

3. `similarity-means-identical` (voice at the elemental unit, on the
   qk-similarity seed).
   Learner's voice: "A high dot product means the tokens are the same kind
   of thing."
   Refutation: the score is alignment in a learned space, direction times
   direction plus magnitude, not sameness. In the seed visual the score
   rises and dies as the query rotates while the keys never change. And the
   space itself is trained: q and k are projections through W_Q and W_K, so
   what counts as similar is a learned decision, different in every head.

Proposed addition to the maintained list (new entry, for Jake's review):

```yaml
- id: attention-compares-raw-embeddings
  topic: attention
  misconception: >-
    Attention measures similarity between the tokens' embeddings directly.
    (Queries and keys are separate learned projections of the embeddings;
    W_Q and W_K define what counts as relevant, so similarity is trained,
    asymmetric, and different per head, not a fixed property of the
    embedding space.)
  triggers: ["query projection", "key projection", "w_q", "w_k"]
```

---

## 4. Prior-art scan and the fresh angle

What exists (all checked 2026-07-04):

- 3Blue1Brown, "Attention in transformers, step-by-step" (April 2024). The
  angle is geometric refinement: context moves embedding vectors ("fluffy
  blue creature"; adjectives update nouns); queries are questions nouns
  ask, keys are potential answers, values are the deltas added to
  embeddings. Uses "lookup table" only for the context-free initial token
  embedding table. No dict-relaxation arc, no hard-lookup limit, no
  explanation-debate payoff.
- Jay Alammar, "The Illustrated Transformer" (2018). Full-architecture
  walkthrough with static diagrams; on QKV it says "They're abstractions
  that are useful for calculating and thinking about attention." Explicitly
  no lookup or retrieval metaphor.
- Karpathy, "Let's build GPT: from scratch, in code, spelled out" (Jan
  2023). Code-first; frames attention as a communication mechanism, nodes
  in a directed graph aggregating information from other nodes with
  data-dependent weights via a weighted sum (paraphrase of his lecture
  notes). Teaches the matrices, not the metaphor; no misconception
  handling.
- d2l.ai, chapter 11 (Attention Mechanisms and Transformers). The closest
  prior art: opens with an explicit database of key-value pairs, defines
  Attention(q, D), and names exact-match lookup as the one-hot special
  case; also names Nadaraya-Watson (1964) kernel regression as "an early
  precursor of the current attention mechanisms." It is a textbook aside:
  stated in a paragraph, not built from an obstruction, no limit
  demonstration as a falsification test, no narrative stakes.
- Olah and Carter, "Attention and Augmented Recurrent Neural Networks"
  (distill.pub, 2016). Attention as differentiable focus: "we focus
  everywhere, just to different extents." Interactive diagrams,
  pre-transformer, RNN-era framing.

Fresh-angle statement (per 3b1b principle 19, fresh presentation over new
content): this session starts from the one data structure every learner in
the room already trusts, the Python dict, breaks it on screen with a
KeyError, and engineers attention as the differentiable repair; the
soft-lookup metaphor is treated as a falsifiable claim, proven term by term
and then proven in the limit (sharpen the scores, watch the dict come
back), rather than stated as an aside; and the same framing is cashed out
twice, once as the sqrt(d_k) variance story and once as the refutation of
heatmap-as-explanation. No existing explainer does the
obstruction-to-limit-proof arc, and none connects the lookup framing to the
attention-is-not-explanation literature. d2l states the analogy; we make it
carry the whole session and pay rent.

---

## 5. Second-instance candidates (for the stress-test beat)

1. Nadaraya-Watson kernel regression (1964, statistics, no neural nets).
   Predict f(q) as a similarity-weighted average of stored outputs:
   f(q) = sum_i v_i alpha(q, k_i) / sum_j alpha(q, k_j), where the keys are
   training inputs, the values are training outputs, and the kernel plays
   the score. d2l.ai names it "an early precursor of the current attention
   mechanisms" (citations: Nadaraya 1964; Watson 1964). Sixty years old,
   same deep structure, different surface: the forgiving dictionary was
   invented by statisticians before it was learned by networks.
2. RAG, which these students run at work (Lewis et al., NeurIPS 2020). "The
   non-parametric memory is a dense vector index of Wikipedia, accessed
   with a pre-trained neural retriever": query vector, key vectors,
   returned passages as values. The differences are the lesson: retrieval
   does a hard top-k over an external store (not differentiable through the
   index), attention does a soft blend over an internal one, inside every
   layer. Same skeleton, opposite ends of the hard-soft dial.

---

## 6. Technical fact-check pack for the writers

- Canonical formula: Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V.
  Dimensions: Q is n x d_k, K is n x d_k, V is n x d_v, output n x d_v.
  Base model: d_model 512, d_k = d_v = 64 per head, h = 8 heads.
- Vaswani et al. results if quoted: 28.4 BLEU WMT 2014 English-German; 41.8
  BLEU English-French, single-model state of the art at the time (their
  big model); arXiv v1 June 12, 2017; NIPS 2017 proceedings.
- Bahdanau scoring was additive (feedforward + tanh; section A.1.2 of
  1409.0473); Luong et al. 2015 catalogued dot / general / concat scores
  (their section 3.1); scaling by sqrt(d_k) is Vaswani et al. 2017.
- The word "attention" in the 2014 paper, section 3.1: "Intuitively, this
  implements a mechanism of attention in the decoder."
- GNMT: arXiv Sep 26, 2016 (Wu et al., 31 authors); paper abstract claims
  error reduction "by an average of 60% compared to Google's phrase-based
  production system"; production launch announced Sep 27, 2016 for Chinese
  to English, "about 18 million translations per day"; blog claim "reduces
  translation errors by more than 55%-85% on several major language pairs";
  expanded to 8 language pairs Nov 15, 2016 (English with French, German,
  Spanish, Portuguese, Chinese, Japanese, Korean, Turkish), "more than 35%
  of all Google Translate queries."
- Google Translate scale, April 2016, official: "more than 500 million of
  you" and "more than 100 billion words a day."
- Numbers with conditions, ready for screen use: seq2seq single LSTM
  reversal effect (perplexity 5.8 -> 4.7, BLEU 25.9 -> 30.6, WMT'14 En-Fr);
  ensemble headline 34.8 vs SMT baseline 33.3; Bahdanau Table 1
  (RNNencdec-50 17.82 / RNNsearch-50 26.75 on all sentences; 26.71 / 34.16
  excluding unknown words); "8000 real numbers" as the fixed sentence
  representation in Sutskever et al.
- Micro-example and sqrt(d_k) numerics: section 1.3 and 1.5 above; all
  computed to shown precision.
- Softmax hard-limit statement (safe formulation): "as the score gaps grow,
  or if you sharpen the scores, softmax approaches one-hot argmax; ties
  split evenly; the transformer itself fixes the sharpness with the
  sqrt(d_k) divisor rather than a temperature knob."

---

## 7. Notebook anchors (supporting d-s0-notebook-yes)

The aha is checkable in about 30 lines of NumPy along this exact ladder:
(1) dict lookup, KeyError on "feline"; (2) one-hot scores over keys, same
lookup as a dot product with a one-hot weight vector; (3) replace one-hot
with softmax(q K^T / sqrt(d_k)): partial credit appears (0.766 cat, 0.186
kitten); (4) blend values, compare with d["cat"]; (5) sharpen scores,
recover step 1 exactly; (6) optional: gradient through the soft version
exists, through the hard version is zero. Micro-example numbers in 1.5 are
the test vector.

---

## 8. Hook-claim verification results

VERIFIED (use freely, sources resolve):

- Sutskever/Vinyals/Le seq2seq, NIPS 2014, fixed-vector design, reversal
  trick and its numbers (with single-LSTM condition).
- Cho et al. Sep 2014 degradation finding and figure; Cho et al. June 2014
  encoder-decoder (EMNLP 2014).
- Bahdanau/Cho/Bengio arXiv 1409.0473 v1 Sep 1, 2014; ICLR 2015 oral;
  soft-search abstract language; Figure 2; Table 1 numbers; additive
  scoring; "mechanism of attention" sentence.
- Bahdanau's status: intern in Bengio's lab after the first year of his MSc
  at Jacobs University; about five weeks left in the internship; named it
  RNNSearch; Bengio supplied the word "attention" (his recollection, via
  correspondence published by Karpathy, Dec 2024, with permission).
- Vaswani et al. arXiv v1 June 12, 2017; NIPS 2017; QKV definition;
  sqrt(d_k) variance footnote and gradient rationale; d_k = 64,
  d_model = 512.
- GNMT paper Sep 26, 2016; production launch Sep 27, 2016 (zh-en); Nov 15,
  2016 8-pair rollout.
- Jain and Wallace NAACL 2019 claims, datasets, and self-stated scope;
  Wiegreffe and Pinter EMNLP 2019 counterclaims; Serrano and Smith ACL
  2019; Bibal et al. ACL 2022 survey.
- RETAIN (NIPS 2016) as a citable real-world case of attention marketed as
  clinical interpretability (a system class, deployed in research practice;
  do not claim a specific hospital deployment).
- NTM Oct 20, 2014; Memory Networks Oct 15, 2014 (ICLR 2015); Key-Value
  Memory Networks Jun 9, 2016 (EMNLP 2016) with the addressing/output
  quote.
- Hook D base sentence: "The animal didn't cross the street because it was
  too tired" is in Google's Aug 31, 2017 Transformer announcement (Jakob
  Uszkoreit), with the claim that "the Transformer clearly identified the
  two nouns 'it' could refer to."

FAILED (do not ship as written):

- "It shipped to a billion users when Google Translate went neural in
  2016" (Hook A stakes line). Google's own April 2016 number is "more than
  500 million" users; no citable 2016 source supports one billion users.
  Replacement that survives sourcing: "a service with more than 500 million
  users, translating over 100 billion words a day" or lead with the 18
  million translations a day carried by the first neural pair.

PARTIAL / conditions attached:

- Hook D's swap-word variant ("wide"): the contrast sentence pair in the
  2017 Google blog post lives inside an embedded image, and text extraction
  cannot confirm whether the published variant is "too wide" or an inverted
  sentence; the "wide" variant is genre-standard in secondary sources.
  Eyeball the blog image (or the Tensor2Tensor notebook) before putting the
  exact pair on screen. Alammar's worked example uses only "tired."
- Hook B's "the query/key/value vocabulary itself is retrieval-systems
  language": defensible only as description. Vaswani et al. credit no
  database or retrieval lineage, and Bahdanau's account says his mechanism
  arose independently of the memory-networks line. Say "the names match how
  retrieval systems talk, and a key-value memory literature was growing in
  parallel"; never say attention was borrowed from databases.
- Attention lineage priority is publicly contested (Schmidhuber's 1992
  fast-weight programmers claim vs Bahdanau's independent-origin account).
  The session need not mention it; if it does, both sides are one sentence
  each.
- Cho et al. BLEU-vs-length figure number: Figure 4 in the ar5iv rendering;
  confirm against the anthology PDF before an on-screen citation. (The
  primary redraw target is Bahdanau Figure 2 anyway, which is fully
  verified.)
- Bahdanau naming anecdote: deliver as his recollection; the word
  "attention" does appear in the paper body (section 3.1), not only in the
  conclusion.

---

## 9. Answers to the brief's seven researcher questions

1. Hook facts: verified, failed, and partial items are itemized in section
   8; every surviving fact has a sources.yaml entry.
2. Best citable quantitative artifact: Bahdanau et al. Figure 2 (caption
   quoted in section 2A) with Table 1 numbers; it shows the collapse and
   the rescue in one plot and is redrawable in tokens. Cho et al.'s figure
   is the backup; the reversal numbers are the spoken-word garnish.
3. sqrt(d_k): section 1.3; verbatim footnote, verbatim motivation sentence,
   and a computed d_k 2-vs-64 demonstration with gradient factors.
4. Prior-art audit and what our angle adds: section 4.
5. Honest soft-lookup lineage paragraph: section 2, candidate B.
6. Defensible 2026 scope of "attention maps are not faithful explanations":
   the one-sentence version in section 2C; the debate is unresolved, the
   original claims are RNN-classifier-scoped by the authors themselves, and
   the survey of record is Bibal et al. 2022.
7. Worked micro-example: section 1.5, with the sharpening and
   softmax-not-argmax payoffs precomputed.
