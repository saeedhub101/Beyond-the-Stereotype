# Render Prompt Pack — Part One (Scenes 01–10)

**Purpose:** Copy-ready prompts for testing a free/local image-to-video workflow. This is a production preparation file, not rendered footage. Keep dialogue and final sound in the edit; do not rely on a video model to render readable dialogue or lip-sync perfectly.

## Required workflow
1. Create and approve one reference portrait for each speaking character before generating shots. Keep those exact references for all shots.
2. Generate each shot as its own short clip (roughly 4–8 seconds); do not ask the model to render an entire multi-beat scene at once.
3. Prefer image-to-video from approved reference stills. Keep the same model/version, aspect ratio, seed when supported, and reference images across shots.
4. Generate silent picture first; add the screenplay dialogue, room tone, and music in editing. Never invent a voice identity from shot to shot.
5. Log the actual model, settings, output filename, and verification result. Do not change `production/scene-status.json` to rendered until an actual clip exists and has been inspected.

## Global visual prompt (prepend to every shot)
Grounded contemporary cinematic realism, 16:9, natural human proportions and skin texture, restrained natural color grade, practical motivated lighting, subtle handheld or controlled tripod movement, believable eye-lines and body mechanics, realistic contemporary city and workplace, quiet observational acting, nuanced facial expressions, natural depth of field, no glossy commercial aesthetic. Cast appearance must match the approved reference images exactly. Preserve the same wardrobe within a continuous scene. Keep gestures small and physically plausible.

## Character locks
- **Adam:** 34-year-old Muslim engineer, short dark hair, neatly trimmed beard, brown eyes, average build, understated neutral workwear. Warm, calm presence; no exaggerated sternness.
- **Mariam:** 30-year-old Muslim architect, dark eyes, elegant modest hijab outdoors, modest contemporary workwear. At home she wears comfortable modest clothing without hijab. Intelligent, warm, self-possessed; never passive or ornamental.
- **Daniel:** 35-year-old Black American software engineer, short hair, casual-professional wardrobe, lively and sincere.
- **Sophie:** 32-year-old British project manager, shoulder-length dark hair, polished professional wardrobe, composed and attentive.
- **Older man / young woman / colleague:** ordinary, specific, believable people; no caricatured expressions or costumes.

## Global negative prompt (append when supported)
No face morphing, identity drift, age changes, hair or beard changes, hijab changes within the same outdoor scene, wardrobe flicker, duplicated people, extra fingers, fused hands, broken anatomy, floating objects, impossible reflections, unreadable fake signage, subtitles, logos, watermarks, exaggerated religious symbolism, prayer scenes, violence, stereotypes, preachy staging, melodramatic acting, beauty-filter skin, artificial smiles, abrupt camera teleportation.

---

## Scene 01 — A Better Morning
**Continuity:** Apartment kitchen / dining area, morning. Adam and Mariam are relaxed spouses. Mariam wears modest comfortable home clothes without hijab.

### Shot 01A — Establishing
**Prompt:** Wide, calm morning view of a lived-in contemporary apartment kitchen connected to a small dining table. Soft daylight through a window, breakfast being prepared, a laptop open to a generic engineering model with abstract lines and shapes but no legible text. Adam studies the screen while Mariam prepares breakfast in the same space. Natural domestic atmosphere, gentle slow push-in.

### Shot 01B — Mariam spots the issue
**Prompt:** Medium two-shot at table height. Mariam leans slightly toward the laptop and points to one part of the abstract model, explaining a thoughtful alternative. Adam listens and turns toward her rather than dismissing her. Warm, equal partnership, subtle expressions, hands move naturally.

### Shot 01C — The idea works
**Prompt:** Over-the-shoulder view of Adam testing a changed configuration on the laptop; abstract model geometry changes in a plausible way, no readable text. He pauses, recognizes the improvement, and looks at Mariam with appreciative amusement. Avoid close-up fake interface text.

### Shot 01D — Shared laugh
**Prompt:** Medium close two-shot, Adam and Mariam exchange a quick affectionate joke and laugh naturally, understated rather than staged. Breakfast remains in foreground, soft morning light, stable faces and clothing.

## Scene 02 — Before the Door
**Continuity:** Same apartment entryway, immediately after Scene 01. Mariam is now ready to leave and puts on her consistent outdoor hijab.

### Shot 02A — Getting ready
**Prompt:** Medium shot in the apartment entryway. Mariam finishes arranging her elegant modest hijab in a natural, unhurried movement; a folder rests on a small console beside keys and a phone. Adam notices the folder and picks it up.

### Shot 02B — The forgotten folder
**Prompt:** Two-shot by the door. Adam offers Mariam the folder with a lightly teasing expression; she takes it and replies with dry humor. Their affection feels familiar and private, no exaggerated romantic posing.

### Shot 02C — Leaving together
**Prompt:** Rear three-quarter view as Adam and Mariam check that they have their belongings and walk out together into a normal apartment corridor. Keep Mariam's hijab and both outfits identical to the previous shot; natural walking cadence.

## Scene 03 — The Small Detour
**Continuity:** Ordinary city sidewalk and transit stop in daylight. Mariam wears her outdoor hijab. Help is offered respectfully, without making recipients helpless.

### Shot 03A — Notice, don't assume
**Prompt:** Wide city sidewalk near a transit stop. An older man has several grocery bags and is briefly struggling to balance them; nearby a young woman studies a transit map with uncertainty. Adam and Mariam notice, exchange a quick glance, and approach calmly, leaving personal space.

### Shot 03B — Adam asks first
**Prompt:** Medium shot. Adam gestures gently toward the grocery bags and asks the older man if he would like help; the man considers, then accepts. Keep the older man dignified and active in the exchange, with realistic bag weight and hand placement.

### Shot 03C — Mariam checks together
**Prompt:** Medium shot at a transit map. Mariam stands beside the young woman, both looking at the map and station signage together. Mariam points to a route while the young woman follows along, engaged and capable. Avoid legible generated signage or close-ups of text.

### Shot 03D — They move on
**Prompt:** Natural wide shot as the older man continues on with the bags now easier to manage and the young woman heads toward the correct platform. Adam and Mariam continue their own journey without waiting for praise or looking back for approval.

## Scene 04 — The Model
**Continuity:** Modern engineering office, daytime. Adam and Daniel work at adjacent workstations; Sophie joins the discussion. Screens contain abstract diagrams, not readable generated text.

### Shot 04A — A concern in the data
**Prompt:** Medium close-up of Adam studying a large monitor with a generic infrastructure stress model represented by clean charts and structural diagrams. His expression shifts from concentration to careful concern, not panic. Office daylight, understated professional wardrobe.

### Shot 04B — Explain the assumption
**Prompt:** Medium three-person office discussion. Adam calmly indicates one assumption in the model; Daniel listens with curious humor, Sophie is attentive and ready to review the evidence. No one is portrayed as foolish or villainous.

### Shot 04C — Test the alternative
**Prompt:** Over-the-shoulder view of a workstation showing a generic engineering diagram being compared with a second case. Adam, Daniel, and Sophie look at the result together. No legible text, no dramatic alarm graphics, realistic collaborative problem-solving.

## Scene 05 — The Kitchen Question
**Continuity:** Office kitchen during a modest team celebration. Keep it friendly, inclusive, and nonjudgmental. Adam chooses sparkling water; other adults make their own choices without ridicule.

### Shot 05A — The offer
**Prompt:** Medium shot in an office kitchen with a few colleagues chatting after work. Daniel offers Adam a drink in a casual, friendly way. Adam smiles and reaches for a clear glass of sparkling water instead. No prominent alcohol branding, no one reacts negatively.

### Shot 05B — A sincere question
**Prompt:** Medium two-shot beside the counter. Daniel asks a respectful question with genuine curiosity; Adam answers calmly, making comfortable eye contact. Their posture remains relaxed and equal, no confrontation, no sermon-like gestures.

### Shot 05C — Shared joke
**Prompt:** Close two-shot as Daniel and Adam share a small joke about clear heads and spreadsheets. Both laugh naturally, and Daniel lifts his own glass in a light toast. Keep the mood warm and ordinary; no judgment of anyone's drink choice.

## Scene 06 — Room to Breathe
**Continuity:** Architecture studio with a courtyard design pinned up or displayed on a monitor. Mariam is the lead professional presenting evidence.

### Shot 06A — The design
**Prompt:** Wide shot of an architecture studio. Mariam stands beside a large courtyard presentation showing shade trees, clear accessible paths, benches, and people of varied ages using the space. The colleague and others listen. Diagrams are visually clear but contain no readable text.

### Shot 06B — Cost concern
**Prompt:** Medium shot of a colleague asking a practical question about initial cost, with a thoughtful rather than dismissive expression. Mariam listens without interrupting and prepares to compare two design options.

### Shot 06C — Evidence-led answer
**Prompt:** Medium shot of Mariam explaining lifecycle trade-offs while indicating two side-by-side courtyard design boards. She is confident and precise, not preachy. The colleague studies the evidence and becomes more engaged. Natural collaborative workplace tone.

## Scene 07 — A Real Question
**Continuity:** Office corridor after the meeting. Adam and Daniel have a trusting colleague relationship.

### Shot 07A — Daniel asks directly
**Prompt:** Medium two-shot in a quiet office corridor. Daniel raises a personal question carefully, looking sincere and slightly uncertain. Adam stops and gives him full attention. Normal office background, no dramatic isolation or confrontation.

### Shot 07B — Boundary is not rejection
**Prompt:** Stable medium close two-shot. Adam explains something important with warmth and plainspoken honesty; his hands make small natural gestures. Daniel listens, gradually reassured. The scene should feel like two friends clarifying a misunderstanding, not a debate.

### Shot 07C — Ease returns
**Prompt:** The tension softens into a shared smile and a brief laugh. Daniel nods; Adam responds with a relaxed expression. They continue walking down the corridor together. Subtle acting, no forced emotional climax.

## Scene 08 — Home Is Home
**Continuity:** Same apartment kitchen in the evening. Mariam is in modest, comfortable home clothes without hijab. Adam and Mariam cook side by side.

### Shot 08A — Cooking together
**Prompt:** Wide evening kitchen shot with warm practical lights. Adam and Mariam prepare vegetables and dinner side by side; pots and ordinary kitchen items are arranged naturally. Their movements are coordinated but not choreographed.

### Shot 08B — Uneven chopping
**Prompt:** Medium close shot of a cutting board with vegetables cut into slightly different sizes, hands holding the knife safely and naturally. Mariam notices and teases Adam; he responds with a playful expression. Avoid unsafe knife handling or malformed fingers.

### Shot 08C — A domestic laugh
**Prompt:** Medium two-shot as they laugh at the engineering defense for uneven vegetables, then continue cooking together. Affection is expressed through familiarity and shared work, not exaggerated romance. Maintain the approved faces and home wardrobe.

## Scene 09 — The Correction
**Continuity:** Engineering meeting room, workday. Adam and Sophie handle a serious but calm reporting issue.

### Shot 09A — Pause before release
**Prompt:** Medium shot of Adam reviewing a printed report and an abstract engineering chart in a meeting room. He identifies a discrepancy and marks the relevant section with a pen. Paper text must remain unreadable; the focus is his careful review.

### Shot 09B — Ask to verify
**Prompt:** Two-shot across a meeting table. Adam explains that one assumption affects a margin in a particular scenario and asks to pause distribution until it is checked. Sophie listens professionally and asks for the alternative case to be documented. No blame, no defensiveness.

### Shot 09C — Responsible decision
**Prompt:** Medium shot as Sophie closes the laptop or sets the report aside to signal that distribution is paused. Adam looks relieved but still focused on the work. Their shared expression conveys responsibility, not triumph.

## Scene 10 — An Invitation
**Continuity:** Office lobby at the end of the day. Adam and Daniel are comfortable friends; Mariam may be referenced but is not required to appear in every shot.

### Shot 10A — The invitation
**Prompt:** Wide-to-medium lobby shot at the end of a workday. Daniel catches up with Adam near the exit and invites him to a casual dinner with friends. People pass naturally in the background; warm late-day light.

### Shot 10B — Considerate without fuss
**Prompt:** Medium two-shot. Daniel mentions that there will be non-alcoholic drinks. Adam responds appreciatively and clarifies that Daniel does not need to redesign the whole evening around them. Daniel replies that he is simply making room for friends. Their exchange is warm and unforced.

### Shot 10C — A touched smile
**Prompt:** Medium close-up of Adam smiling with genuine appreciation, then looking back at Daniel. Daniel returns an easy grin. End on a quiet sense of friendship opening outward, no dramatic music cue implied by the image.

---

## Editing and sound notes
- Use the screenplay dialogue verbatim; do not ask the video model to invent or visibly print dialogue.
- Record or synthesize one approved voice per character and reuse that same voice identity across all scenes. Test English pronunciation, emotional range, and consistency before producing a full scene.
- Use restrained room tone and city ambience. Music should be subtle and should not instruct the audience how to judge a character.
- Cut on listening reactions and small gestures, not only on whoever is speaking.
- If a clip changes a face, hijab, wardrobe, hand anatomy, or geography, reject it and regenerate from the approved reference rather than accepting continuity drift.
- The scenes and prompts are prepared, not rendered. Update the scene ledger only after real media files are generated and checked.
