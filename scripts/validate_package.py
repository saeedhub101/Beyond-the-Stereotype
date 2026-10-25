#!/usr/bin/env python3
"""Validate the screenplay package; this does not render audio or video."""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    root / "screenplay/part-01-scenes-01-10.md",
    root / "production/scene-status.json",
    root / "characters/continuity.md",
    root / "voices/voice-bible.md",
]
errors = [f"Missing or empty required file: {p.relative_to(root)}"
          for p in required if not p.is_file() or p.stat().st_size == 0]
if not errors:
    screenplay = required[0].read_text(encoding="utf-8")
    found = [int(n) for n in re.findall(r"^### Scene (\d+) —", screenplay, re.M)]
    expected = list(range(1, 11))
    if found != expected:
        errors.append(f"Expected scenes 1-10 in order; found {found}")
    try:
        ledger = json.loads(required[1].read_text(encoding="utf-8"))
        scenes = ledger.get("scenes", [])
        if [s.get("id") for s in scenes[:10]] != expected:
            errors.append("Scene ledger must contain scene IDs 1-10 in order")
        for scene in scenes:
            if scene.get("status") == "rendered" and not scene.get("video"):
                errors.append(f"Scene {scene.get('id')} marked rendered without a video path")
    except (json.JSONDecodeError, AttributeError) as exc:
        errors.append(f"Invalid scene-status.json: {exc}")
if errors:
    print("PACKAGE VALIDATION FAILED")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("PACKAGE VALIDATION PASSED")
print("Scenes 01-10 are scripted and ready for production planning.")
print("No video or audio render was performed by this validator.")
