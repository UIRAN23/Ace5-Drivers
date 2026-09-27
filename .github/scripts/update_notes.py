import json
import os
from pathlib import Path
import re

root = Path(__file__).resolve().parents[2]
feed = json.loads((root / "update.json").read_text(encoding="utf-8"))
version = feed["version"]
if not re.fullmatch(r"v\d+\.\d+\.\d+", version):
    raise ValueError("Invalid current version")
text = os.environ["CHANGELOG"].replace("\\n", "\n").strip()
if not text or len(text.encode()) > 32768:
    raise ValueError("Changelog must contain 1 to 32768 bytes")
(root / "changelogs").mkdir(exist_ok=True)
(root / "changelogs" / (version + ".md")).write_text(text + "\n", encoding="utf-8")
(root / "changelog.md").write_text(text + "\n", encoding="utf-8")
