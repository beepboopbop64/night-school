# Review notes: dotprod, round-04

Write freeform prose under any anchor below, or under General. Every
note is triaged; nothing is silently dropped.

Conventions:
- `@spine` or `@global` anywhere in a note marks it spine-level; the
  round PAUSES with an editable plan instead of auto-executing.
- `#style` tags a taste rule to harvest into the show bible.
- `@wontfix-candidate` marks a note you suspect conflicts with a bible
  rule; triage will surface the conflict prominently.

## @video/beat-01

## @video/beat-02

## @video/beat-03

The a . b annotation renders in periwinkle, which is the candidates' color. The annotation names the reading the machine produces, so it belongs in lilac like the score readout it sits on (or neutral cream). One color change, then re-render.

## @video/beat-04

The card on screen literally says "retrieval prompt" for the entire beat. That is a stage direction leaking onto the screen, not content; a student pausing the frame sees a box naming the KIND of card instead of the card. Put the actual question on it: "Two arrows go in. What two operations turn them into the score?" Also the beat's planned on-screen text never rendered anywhere: land "two arrows in, one number out" as the label when the matched entries pool into the readout, and "different aisle, same meter" as the landing line. Iris passed this frame, so log the miss: screen text that names the kind of moment instead of its substance should read as a violation.

## @video/beat-04b

Same disease, three headers: "Guess", "Reveal", "Next" are the director talking to the crew. The guess card should pose the actual doubling question and need no header; the reveal needs no header at all, the stacked 4.2 / x2 / 8.4 IS the reveal (that part is genuinely good, keep it exactly); the closing card's header, if it needs one, is "For the walk home". And the closing card says "Keep the direction. Lose the size." while the breadcrumb everywhere else says keeps the direction and FORGETS the size. Make it "Keep the direction. Forget the size." so the callback lands on the canon phrasing.

## @page/beat-01

"Try answering that before you read on" repeats "before you read on" from the blockquote one sentence earlier. Cut the second occurrence: "Try answering it first; it's genuinely harder than it sounds."

## @page/beat-02

The call-your-shot cannot be called: all four candidates start at unit length, so every bar tops out at the same 1.0 the moment you point at it, and at the initial 90 degrees c2 and c3 tie at 0.9 with c2 arbitrarily bolded as leading. A student who honors the prompt discovers it has no answer and stops taking our prompts seriously. Replace the blockquote with the falsifiable version, and cue the full sweep while you are at it: "Before you touch the probe: swing it all the way around. Does any bar ever drop below zero? Call it." Beat-03's debrief assumes the student saw zero and negative; right now nothing tells them to go look.

## @page/beat-03

This one misteaches and it is the aha beat, so it goes first. The section claims "the direction is the only thing the sum ever responded to," "one honest reading of alignment," and "It tracks direction exactly" one screen AFTER the interactive's length handle showed the score climbing on length alone. Scope every direction-only claim to the equal-length sweep ("while every arrow held the same length, direction was all the sum ever responded to"), drop "exactly," and soften "honest": beat-04b's whole point is that this reading can be bought. Keep the aha sentence itself verbatim.

While in there: give the notation a referent in half a clause, "a is the probe's list, b is the candidate's," because right now a . b lands as a decal, not a thing you could use. End the section with the doc's generative close instead of the current restatement: "Before you scroll on: positive, zero, negative. Say what each reading claims about two vectors, in your own words." And "Step back from the sweep for a second" is the "for a second" filler again; vary it.

## @page/beat-04

Retitle: the heading says "Same math, different aisle" while the chapter list above it, the storyboard, and extension prompt 3's verbatim quote all say "Same meter, different aisle." One page, two names for the same section.

"Lift the whole thing out of the record store": no record store was ever planted. Beat-01 is a music app and a data center. Swap to the music app and let "different aisle" carry as plain idiom.

The section also performs the whole transfer for the reader and ends on a summary. Open with the retrieval blockquote the video and doc both carry ("From memory: two arrows go in. What two operations turn them into the score?"), and pose the mapping as a fill-in before confirming it: "In the job aisle, which list plays the probe?" That also fixes the stacked-asks overload screening flagged, because the page now sequences recall, then transfer.

## @page/beat-04b

"Sit with" appears twice in this one section ("But sit with it for a second," "For the walk home, sit with this:"), and we have banned that construction in two separate rounds now. Purge both, no filler phrase repeating anywhere in the section.

"Not a bug exactly, more like an unpaid invitation" does not parse; invitations are not paid. "A standing invitation."

The doubling test can visibly fail in the widget it points at: at the default probe angle the one-decimal readouts show 0.3 becoming 0.7, which reads as MORE than double, and a c1 left stretched from beat-02 cannot double at all because the handle caps at 2.0. One steering sentence before the test fixes all of it: point the probe straight along c1 and set its length back to 1.0 first; then the doubling reads a clean 1.0 to 2.0 under any rounding.

The breadcrumb drifted: this page says "keeps the direction information but forgets the size" while the video, doc, and extension prompt 1's verbatim quote say "keeps the direction and forgets the size." Align to the canon.

And the close never comes home. The opening scene, the app that nailed your taste, never returns. One sentence before the walk-home question: "Next time the app hands you a stranger's song that is exactly right, you will know the number that said ship it, and you will know that number can be shouted over." Mirror the same return in the doc's final section. Page and doc only; the video's closing card is covered by the note above.

## @ix/dot-alignment

The initial probe angle of 90 degrees sits exactly on the c2/c3 bisector: a dead tie at 0.9 that the first-wins tiebreak falsely resolves by bolding c2 as "leading." Move the initial angle off the bisector (40 degrees gives a unique honest leader) and suppress the leading emphasis whenever scores tie.

Accessibility: the SVG's internal labels plus the readout row serialize into an unparseable text run ("c1 c2 c3 c4 probe 0.3 c1 0.9 c2 ...") for assistive tech and text extraction. Give each score readout an aria-label like "c2 score 0.9" and mark the decorative SVG text aria-hidden.

## @doc

"Same meter, new aisle" is a third name for the beat-04 section; use "Same meter, different aisle" like everything else.

Comma splice: "The meter was never asked to measure size, it was supposed to measure agreement in direction..." Full stop after "size."

"Close the loop yourself before the next section:" is immediately followed by section 4 opening "Time to close the loop." Keep the section-4 opener (it is locked in narration); rewrite the section-3 closer without the phrase, and do not reach for "one more," which the doc already uses twice.

The prediction prompts all wear the same "Before you read on" frame, three times, plus the page's copies. Vary at least two so the ritual does not read as a template.

The honest-edges callout promises "tidy integers so your eyes can do the arithmetic," but the interactive the reader is sitting next to shows one-decimal readouts and never shows a single vector entry. Keep the mandated readability phrase, drop the eyes-do-the-arithmetic promise.

Mirror the recursive close from @page/beat-04b in the final section.

## @ext

This one is blocking and it is a regression: round-03 already ruled on it. Prompt 2 opens "In 'the score behind the song' we said scaled dot-product attention is the similarity meter wearing a work uniform: query dot key, divided by sqrt(d_k), fed into a softmax," and the Attention Is All You Need hook promises "the exact dot-product-divided-by-sqrt(d_k)-then-softmax we walked through." The session never mentions attention, softmax, or sqrt(d_k) on any surface. A student scrolls back, finds nothing, and stops trusting the page at the exact moment we hand them off. Reword both forward-looking, preview framing only: the meter SHOWS UP in transformers as scaled dot-product attention, next session's machine if you want a preview tonight; the hook becomes "you will see tonight's meter in its work uniform: a dot product, divided by sqrt(d_k), then softmaxed, scoring every word against every other word." No "we said," no "we walked through," anywhere in the menu.

Separately: the first LLM prompt's visible text names the answer to the walk-home breadcrumb ("dividing each vector by its own length (cosine similarity)"), and the first project brief names it again. The page must never display the breadcrumb's answer; the gap is the point. Reword so the learner proposes the fix and the LLM stress-tests it, and keep cosine and normalize out of ALL visible menu text: prompts, what-good-looks-like lines, and project briefs alike.

After the beat-04 retitle, confirm prompt 3's quoted section title matches the page heading.

## @notebook

## General

#style: on-screen text in video is content, never stage directions. Words that name the kind of moment ("retrieval prompt," "Guess," "Reveal," "Next," "prediction card") never render; a card that poses a question shows the question itself.

#style: a callback may only reference an image the lesson actually planted. Before writing "the X," check that X exists upstream on the same surface.

#style: the close returns the opening image, recharged. If the final section never touches the scene that opened the lesson, the lesson is not finished.

#style: extensions preview forward, never claim coverage backward. "We said" or "we walked through" may only describe things a student can scroll up and find.

#style: no visible surface states the answer to the walk-home breadcrumb; the gap stays open until the next session opens with it.
