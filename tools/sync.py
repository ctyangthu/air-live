"""Copy the three airlines' timetables and audit results from the sibling projects into data/.

    python3 tools/sync.py

Run this after changing eva-live, ci-live or jx-live. tools/build.py only reads data/, so this repository builds alone.
"""
import pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
for name, code in (("eva-live", "eva"), ("ci-live", "ci"), ("jx-live", "jx")):
    shutil.copy(ROOT.parent / name / "data" / "schedule-nw26.txt", ROOT / "data" / f"schedule-{code}.txt")
    print(name, "copied")
