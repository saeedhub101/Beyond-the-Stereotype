# Production ledger and rendering policy

The scene ledger is the source of truth for resumability.

- scripted: screenplay exists.
- prepared: inputs have been validated and packaged.
- rendered: a real video file exists and has been checked.
- verified: visual, audio, and continuity review has passed.

Never mark a scene rendered or verified just because a workflow succeeded. The current workflow packages free source inputs; a genuinely free rendering engine still needs a capability and licensing test before integration. Scene outputs should eventually live in scenes/scene-001/, scenes/scene-002/, etc., with a manifest and checksums. Commit each verified scene promptly so interrupted runs resume from the last confirmed output.