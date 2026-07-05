# Screening report: dotprod, round-03

VERDICT: PASS (all four critics clean).

## round-1
- FAIL **sam** — probes: driving=true aha=false retrieval=true (Driving question correctly reframes the task as converting two lists into a single similarity score, capturing the core meaning. Aha statement introduces contradictory caveats claiming the dot product 'secretly' rewards magnitude in ways that can make high scores indicate length rather than similarity, undermining the canonical claim it is a similarity meter. Retrieval accurately describes multiply-and-add operations and correctly identifies the output as a similarity score.)
- PASS **petra** — clean
- FAIL **vera** — V-DASH: 'Nothing about its direction changed; it never got any closer to the probe.'
- PASS **iris** — clean

## round-2
- PASS **sam** — probes: driving=true aha=true retrieval=true (Driving question: Student captures the core task—reducing two numerical lists to a single match score—with concrete examples. Aha sentence: Student correctly describes dot product's mechanism (entry-by-entry multiply-and-sum) and its directional sensitivity, then identifies its critical flaw (magnitude inflation), enriching the canonical claim. Retrieval prompt: Student proposes normalization/cosine similarity as the fix that preserves directional agreement while eliminating magnitude bias, directly addressing the problem flagged in the aha and providing a substantively correct two-operation procedure (normalize, then dot product).)
- PASS **vera** — clean

## Sam (cold walk)
- driving question: How do you turn two totally different lists of qualities (a song's traits vs. a listener's taste, or later a resume vs. a job posting) into one single number that says how well they match?
- aha restated: Multiplying two vectors entry-by-entry and summing gives a clean similarity score that tracks direction (alignment) perfectly, but that same score also grows just from making a vector longer, so it secretly confuses 'more aligned' with 'bigger.'
- retrieval answer: The cheap fix is to divide out the lengths of the vectors before comparing them (normalize, i.e. cosine similarity), so you keep the directional agreement but the score stops caring how long either vector is.
- matcher (claude-haiku-4-5): Driving question: Student captures the core task—reducing two numerical lists to a single match score—with concrete examples. Aha sentence: Student correctly describes dot product's mechanism (entry-by-entry multiply-and-sum) and its directional sensitivity, then identifies its critical flaw (magnitude inflation), enriching the canonical claim. Retrieval prompt: Student proposes normalization/cosine similarity as the fix that preserves directional agreement while eliminating magnitude bias, directly addressing the problem flagged in the aha and providing a substantively correct two-operation procedure (normalize, then dot product).
- confusion/boredom map:
  - [click] hero / opening question: The Spotify hook made the abstract 'score a match' question feel concrete and relatable right away.
  - [confusion] beat-02 / 'Drag the probe' widget text: The listed numbers (0 c1, 1 c2, 1 c3, 0 c4) show up with no clear label for what they represent, felt like a leftover UI dump rather than something I could parse as a reader.
  - [click] beat-02 / recipe line: 'Multiply entry by entry, then add' as the whole recipe was satisfyingly simple after the buildup about tangled qualities.
  - [notation] beat-03 / 'a . b' annotation: The small mono symbol 'a . b' appears right when the term is being coined, but it's never tied back explicitly to what a and b are in the earlier arrows, so it landed as a label more than an equation I understood.
  - [click] beat-03 / naming beat: 'The dot product is a similarity meter' was a clean, quotable aha moment.
  - [overload] beat-04 / domain-swap section: A lot happens back to back here, retrieval prompt, domain swap to resumes, a guess card, then the stretch reveal, and by the third restatement of 'multiply matched entries, add them up' it started to feel repetitive rather than additive.
  - [click] beat-04 / stretch reveal: Watching the score climb while the arrow's direction visibly stays the same made the flaw concrete and convincing.
  - [boredom] closing card / walk-home question: By the time the cliffhanger question arrived I had already guessed the answer (normalize somehow) from the repeated setup, so the suspense felt a bit flat.
- advisory (never gates): curiosity=4 wouldFinish=true It felt clear and well-paced for the first two beats but started to drag slightly by the end from restating the same recipe multiple times before finally getting to the actual twist.

## Petra (pedagogy, 30 rules)
- ADVISORY R10: beat-01's visual is two number columns (schematic-numeric, not a concrete picture) that simply cut to beat-02's arrows ('One amber probe arrow and four periwinkle candidate arrows appear'); no morph is staged connecting the number-list representation to the arrow representation, so the concrete->schematic fade required by the rule is never shown even though the schematic->symbolic fade later (the mint glow a.b truing up) is. -> have the number-column entries visibly rotate/collapse into the probe and candidate arrows at the top of beat-02 so the first representational jump is animated, not cut.
- ADVISORY R2: beat-04 narration makes two parallel claims, 'Long songs would win on sheer loudness, and padded resumes would win on sheer length,' but the visual at that moment ('One periwinkle candidate stretches longer... a small rose flag marks the unearned win') is staged entirely inside the already-swapped job-posting scene; the song-domain half of the claim has no visual referent on screen. -> either cut the song-domain restatement from the narration or briefly flash back to a stretching song-candidate arrow before returning to the job aisle.
- ADVISORY R3: the locked registry assigns amber to the probe and periwinkle to candidates, but beat-03's notation is described as 'a small periwinkle mono annotation, a . b,' rendering both the probe term (a) and candidate term (b) in a single color instead of color-matching each symbol to its referent. -> split the annotation coloring so 'a' renders in amber and 'b' in periwinkle, consistent with the rest of the session's term-to-referent color coding.
- ADVISORY R8: beat-02's stage direction reads 'One amber probe arrow and four periwinkle candidate arrows appear' — 'appear' is a display verb, not a build verb, at exactly the moment the plan-level check asks to be verified (intents must say draws/builds). -> rewrite the intent so the probe and candidates are drawn in sequence (e.g., probe arrow drawn first, then candidates drawn one at a time), matching the reasoning order in which they're used.

## Vera (voice, Opus final pass)
- ADVISORY V-DASH: 'Nothing about its direction changed; it never got any closer to the probe.' -> 'Nothing about its direction changed. It never got any closer to the probe.'

## Iris (cross-media continuity)
- no findings
