# Beyond the Stereotype

An independent, staged production project for a character-driven feature film about Muslim everyday life, friendship, integrity, and coexistence.

## Current status

- [x] Repository scaffold and continuity bible
- [x] First 10-scene screenplay package
- [x] Free GitHub Actions validation and resumable scene ledger
- [ ] Visual character reference sheets
- [ ] Tested, genuinely free video-generation pipeline
- [ ] Rendered scene videos and consistent character voices

**Important:** GitHub Actions is orchestration, not a free unlimited GPU or video-generation service. The current workflow validates and packages production inputs; it does not claim to generate finished video. No paid API, credits, or secret keys are required by this starter workflow.

## Project structure

- screenplay/ — screenplay drafts, broken into scenes
- characters/ — canonical character descriptions and continuity rules
- voices/ — stable voice specifications
- production/scene-status.json — resumable scene ledger
- scripts/ — validation and production helper scripts
- .github/workflows/film-production.yml — manual, free GitHub Actions workflow

## Run the workflow

Open **Actions → Film production (free orchestration) → Run workflow**. Select a scene range. The workflow validates the scene package and stores a downloadable artifact. It marks scenes as *prepared*, never *rendered*, until a real video file is actually produced and verified.

## Free-first rules

1. Do not call paid services or use paid credits.
2. Do not invent video/audio outputs or mark unrendered scenes complete.
3. Save each successfully produced scene immediately and resume from the last verified scene.
4. Reuse the character and voice bibles for every scene.
5. Keep production assets separate from the Adam-City project.

## Film concept

**Title:** Beyond the Stereotype  
**Target runtime:** approximately 90 minutes, produced in small batches.  
**Dialogue:** English, for consistent AI speech support.  
**Core cast:** Adam, Mariam, Daniel, and Sophie.  
**Creative boundaries:** no prayer scenes, no violence, no caricatures, no forced preaching. The story demonstrates faith through ordinary choices, kindness, professional honesty, and friendship.
