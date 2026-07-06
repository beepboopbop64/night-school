# Screening report: dotprod, round-05

VERDICT: PASS (all five critics clean).

## round-1
- FAIL **sam** — probes: driving=true aha=true retrieval=false (Driving question: student captures core meaning—reducing two lists to one score measuring match/alignment. Aha sentence: student correctly describes the multiply-and-add procedure and its meter role, adding valid insight about length inflation. Retrieval: student proposes normalization plus multiply-and-add rather than directly identifying the two operations (multiply and sum) that comprise the dot product itself.)
- PASS **petra** — clean
- PASS **vera** — clean
- FAIL **tracer** — T2: text says 'You already saw length raise the score when c1 stretched' but the only stretch demo on the page named the candidate 'Night Drive' | T2: the page instructs 'point the probe straight along c1 and set its length back to 1.0 first' and 'Double c1's length exactly, same direction'
- PASS **iris** — clean

## round-2
- PASS **sam** — probes: driving=true aha=true retrieval=true (Driving question: Student accurately restates the core problem with concrete example (song traits vs personal taste), capturing how to reduce two multi-dimensional objects into a single score. Aha sentence: Student demonstrates that dot product measures similarity while critically identifying its length bias, showing nuanced understanding beyond bare recitation. Retrieval: Student identifies two substantively correct operations (normalize, dot product) that produce a similarity score from two vectors, consistent with their insight about length bias, with transparent acknowledgment of inference.)
- PASS **tracer** — clean

## Sam (cold walk)
- driving question: How do you take two things that each have a bunch of different qualities (like a song's traits and your taste) and boil their match down to a single number, and what is that operation actually doing under the hood?
- aha restated: Turning each thing into a list of numbers (a vector), multiplying matching entries and adding them up (the dot product) gives you a similarity meter that's positive when things agree, zero when unrelated, and negative when opposed, but it secretly rewards length as well as direction, so a longer vector can win without actually matching better.
- retrieval answer: The cheapest fix is to normalize the vectors first, divide each one by its own length before doing the multiply-and-add, so only direction is left and the size can't shout over alignment anymore (basically cosine similarity), though I'm inferring that since the session never says the word 'normalize' outright.
- matcher (claude-haiku-4-5): Driving question: Student accurately restates the core problem with concrete example (song traits vs personal taste), capturing how to reduce two multi-dimensional objects into a single score. Aha sentence: Student demonstrates that dot product measures similarity while critically identifying its length bias, showing nuanced understanding beyond bare recitation. Retrieval: Student identifies two substantively correct operations (normalize, dot product) that produce a similarity score from two vectors, consistent with their insight about length bias, with transparent acknowledgment of inference.
- confusion/boredom map:
  - [click] beat-01 / 0:00: The 'no single ruler works' framing made the problem feel concrete right away, good hook.
  - [click] beat-02 / 1:00 (numeric example): The tiny worked example (2,1 dot 1,3 = 5) was the first moment the recipe actually clicked.
  - [notation] beat-02 / interactive widget text (loud/fast numbers, 'taste at 40°'): Seeing a wall of numbers like '0.77 0.64 0.94 0.34' and 'taste at 40°' with no clear layout in the text extract left me guessing which number belonged to which arrow/candidate.
  - [overload] beat-02 / interactive widget (four candidates + bars + degrees): Too many moving pieces described at once (arrows, degrees, stacked bar segments, lilac/mint slices) for a text-only read; I'd have needed the actual visual to track it.
  - [click] beat-02 / length-stretch moment: The reveal that stretching a candidate raises its score with zero rotation was the first 'oh, that's the catch' moment.
  - [click] beat-03 / 'the dot product is a similarity meter': Naming the thing after building it by hand felt satisfying, like the payoff finally landed.
  - [click] beat-04 / back to the data center: Tying the probe/candidate language back to 'your taste' and 'the catalog' closed the loop nicely.
  - [click] beat-04b / doubling test: 4.2 to 8.4 exactly was a clean, satisfying confirmation of linearity.
  - [confusion] beat-05 / closing 'cheapest fix' question: The session ends by asking me to name the fix but never states it anywhere in the main text, so I'm left unsure if I'm supposed to already know cosine normalization or if that's genuinely left open.
  - [boredom] beat-05 / 'still up' extensions menu: By the time I hit the three optional doors (argue/read/build) I was ready to close the tab, this felt like homework tacked onto dessert.
- advisory (never gates): curiosity=3 wouldFinish=true It moved briskly and the arrow/meter idea clicked, but the interactive widget's dense numbers were hard to parse from text alone and the ending left the actual fix unresolved, which felt a bit like being sent home with an unfinished thought at 9pm.

## Petra (pedagogy, 30 rules)
- ADVISORY R10: beat-03 shows the concrete-to-schematic fade explicitly (the three probe-position stills 'collapse into one lilac meter dial'), but the schematic-to-symbolic fade is not shown: the annotation 'a . b' is described as simply sitting on the score readout ('A small lilac mono annotation, a . b, sits on the score readout') rather than growing out of the dial or bar the way the arrows grew out of the stacked lists in beat-02. -> Have the a·b notation visibly condense out of the meter dial or the summed bar (e.g., the two multiplied-and-added digits sliding together into the dot) so the diagram-to-notation fade is shown, not just co-present.
- ADVISORY R19: The length-cheat reveal in beat-02 ('So a big score means two songs are the same, right? ... Stretch a candidate's arrow longer... its score climbs anyway on length alone') states the intuitive misconception and immediately demonstrates the refutation with no demanded guess beforehand, unlike the negative-score sweep ('does any score go negative? ... Made your call?') and the beat-04b doubling reveal ('does the score double exactly, or just drift up? Made your call?'), both of which carry explicit prediction cues. -> Insert a one-line prediction prompt before the stretch (e.g., 'c1's direction is pinned; guess what stretching it does to its score') so the session's central misconception correction gets the same demanded-guess treatment as the other major reveals.
- ADVISORY R3: The interactive score bar stacks a lilac 'loud product' slice with a mint 'fast product' slice ('The lilac slice of each bar is its loud product, the mint slice its fast product'), but mint is the locked color for the aha true-up (spine section 5, data.fit) and is spent again for the aha sentence's mint glow in beat-03. Reusing mint earlier as a generic vector-component color dilutes its signal value at the actual aha moment. -> Color the two stacked product slices with a pair unrelated to the locked semantic set (or two shades within the existing periwinkle/lilac family), and reserve mint exclusively for the beat-03 true-up.

## Vera (voice, Opus final pass)
- ADVISORY V-DASH: 'Try answering it first; it's genuinely harder than it sounds.' -> 'Try answering it first. It's genuinely harder than it sounds.'
- ADVISORY V-DASH: 'Agreeing hard on a quality adds a lot; pulling in opposite directions can subtract.' -> 'Agreeing hard on a quality adds a lot. Pulling in opposite directions can subtract.'
- ADVISORY V-DASH: 'Nothing about its direction changed; it never got any closer to the probe.' -> 'Nothing about its direction changed. It never got any closer to the probe.'
- ADVISORY V-DASH: 'the mint slice its fast product; stacked, they are the score.' -> 'the mint slice its fast product. Stacked, they are the score.'

## Tracer (confused-student trace)
- ADVISORY T1: beat-03 calls the dot product 'one honest reading of alignment' right after beat-02 already demonstrated that a stretched candidate's score climbs on length alone with no change in alignment ("a long arrow can fake a high number"); calling the reading 'honest' here sits oddly against a beat later explicitly titled 'The honest look' (beat-04b), which exists specifically to complicate this claim -> hedge the claim here, e.g. 'one reading of alignment comes out — as long as length stays fixed' — so 'honest' isn't spent before the beat that earns the word
- ADVISORY T2: the page has used 'arrow' consistently throughout (probe arrow, candidate arrows, taste arrow) and never uses the word 'vector' anywhere before this sentence; 'vectors' appears here unglossed -> say 'two arrows' to match the vocabulary the page has built, or add a one-clause aside the first time 'vector' appears ('vector — the arrow you've been turning')
- ADVISORY T3: 'one more aisle' presumes a first aisle, but the video never used the word 'aisle' before this point — the catalog was called a 'shelf' in beat-04 ('The catalog is a shelf of candidates'), not an aisle -> either introduce 'aisle' earlier (e.g. pair it with 'shelf' in beat-04) or drop the implied callback: 'try it in one more setting: score yourself against a job posting'

## Iris (cross-media continuity)
- no findings
