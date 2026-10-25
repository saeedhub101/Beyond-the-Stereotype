# Free Production Pipeline Assessment

Updated: 2026-10-25

## Decision

Do not connect a paid hosted video API. Do not claim GitHub Actions can render the film on its standard hosted runner. The current Actions workflow is only a validator and source-package builder.

## Video candidate: Wan 2.2 TI2V-5B

- Official repository: https://github.com/Wan-Video/Wan2.2
- The official project describes TI2V-5B as supporting text-to-video and image-to-video at 720p and 24 fps, and says it can run on consumer GPUs such as an RTX 4090.
- The repository advertises Apache-2.0 for the code; model weights and any related assets must still be checked against their own published terms before distribution.
- This is a locally/self-hosted model, not a free unlimited web API. The project requires compatible GPU hardware and model weights. A standard GitHub-hosted Actions runner is not a suitable assumed GPU host.
- Use fixed character reference images and image-to-video where possible; text-only generation alone is not enough to guarantee that faces, wardrobe, and identity remain stable.

## Voice candidate: GPT-SoVITS

- Official repository: https://github.com/RVC-Boss/GPT-SoVITS
- The project documents few-shot text-to-speech and voice conversion from short reference audio, and supports English.
- Before production, inspect the exact model-weight licenses and confirm rights for every reference voice. Use only original/authorized voices. Do not assume that a code license automatically grants rights to every downloadable model or voice dataset.
- Generate a small test for each of the four characters and check identity consistency, pronunciation, and emotional performance before making a production decision.

## Hard constraint: genuinely free

“Open source” does not mean that GPU compute is free. No production GPU has been established by this repository. Do not start paid instances, use credit-based generation websites, or add API secrets. First test only on a genuinely available free runtime or on hardware the project owner already has access to.

## Next acceptance test

1. Verify a free runtime is actually available and permits the model download and inference.
2. Produce one short, low-resolution test clip using an original character reference image.
3. Produce two short lines for one character using the same voice configuration.
4. Check face continuity, audio intelligibility, license terms, runtime limits, and persistence of files.
5. If the free runtime cannot do this, report the blocker honestly; do not mark any scene rendered.
6. Once a scene output is genuinely generated, save it to `scenes/scene-NNN/`, validate it, and update the scene ledger immediately.

## Status

- Video pipeline: **not yet proven on a free compute resource**.
- Voice pipeline: **not yet tested in this project**.
- Scenes rendered: **0**.
- Paid credits used by this project: **0**.
