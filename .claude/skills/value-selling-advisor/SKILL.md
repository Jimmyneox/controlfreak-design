---
name: value-selling-advisor
description: Write consultative, value-based, story-driven sales copy for a Control Freak product. It researches the buyer's pain in three layers, tells a relatable story from that pain to the feature that fixes it, shares expertise freely, and contrasts low-pressure "seeking" questions with pushy buy requests. Use for pitches, site and brochure copy, sales emails, demo scripts and objection handling, or when the user says "value-selling-advisor" or asks for a story-driven pitch.
---

# Value-selling advisor

Jimmy's sales approach, first written as a Gemini skill (2026-10-27). It combines
consultative selling (diagnose first) with value-based selling (show the cost of the problem
and the value of fixing it). Sources: IDC, "Value-based selling versus consultative: when to
use each approach", and ecosystems.io, "Storytelling in sales: why your sales pitch needs a
value story".

## Control Freak rules come first

Read these before writing, because they override anything below:
- `design/STYLE.md`
- `design/PARENT_BRAND.md`
- the product's `products/<code>/PUBLIC_BRIEF.md`
- the newest rows of `DECISIONS.md`

In short:
- **Facts:** only what the PUBLIC_BRIEF and the product's market file (`01-market.md`) say. Cite
  every number, and label every estimate as one. Never invent a statistic, review, testimonial,
  customer or quote. A story is either a real, sourced example or clearly marked as an
  illustration ("Picture this: …").
- **Prices:** none, unless DECISIONS says the price is set ("pricing is not set until
  engineering and costs are calculated"). Tier names only: Starter / Pro.
- **Wording to avoid:**
  - "never cloud HA" and "via HA bridges"
  - calling a product a "pool add-on", or saying it needs another controller
  - "works with every chiller" (or every pump, every tank)
  - naming competitors on public pages
  - fear-mongering
  - safety claims beyond what the Engineer has cleared (see DECISIONS)
- **Lines to carry:** use the approved voice line and the approved Home Assistant lines word for
  word: "Works with the Control Freak gear you already own…" and the safety line.
- **Copy ownership:** CFP Product Writer owns the final buyer copy. Output from this skill is a
  draft for the Writer, unless the user asked for the final copy.
- **Language:** plain American English, and short sentences.

## Method

1. **Research the pain in three layers**, from the market file, the voice-of-customer research
   (`design/research/`) and sourced web research:
   - **Friction:** the daily hassle (checking the pit every time it rains, dosing by hand,
     juggling five apps).
   - **Financial risk:** what it costs when it goes wrong, as a sourced figure (for example, the
     average water-damage claim).
   - **Emotional pinpoint:** the moment the buyer feels it (lying awake during a storm, the trip
     cut short, the dead coral).
2. **Tell the story from pinpoint to safety.** Validate the frustration in the buyer's own
   words. Then explain, like a knowledgeable best friend, how one specific feature protects them.
   Use one feature per story and a concrete outcome. Never use jargon that the brief doesn't
   explain.
3. **Share insight generously.** Give away real, useful expertise (what to check, what fails
   first, what to ask any vendor), so the reader learns something even if they never buy. Be
   humble, and don't gatekeep or sound like a brochure.
4. **Use seeking questions, not buy requests.** Close with low-pressure questions that help the
   buyer diagnose their own situation. When asked, show them side by side:

   | Seeking question (pulls in) | Buy request (pushes away) |
   |---|---|
   | "When the power flickers, how do you find out the sump is still running?" | "Order now before stock runs out." |

## Output

- Lead with the pain, then the story, then the feature, then the outcome, then a seeking
  question, then a soft next step ("Join the beta", "Try the demo").
- List the sources under the draft, and mark anything that needs the Writer's or the Engineer's
  sign-off.
- For sales emails, write in the first person as the sender. Keep it under 150 words unless the
  user asks for more. Don't send anything: external mail needs Jimmy.
