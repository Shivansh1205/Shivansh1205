import os
from pathlib import Path
from datetime import datetime

ASSETS = Path("assets")
ASSETS.mkdir(exist_ok=True)

counter_file = ASSETS / "profile_views.txt"
if not counter_file.exists():
    counter_file.write_text("0", encoding="utf-8")

views = int(counter_file.read_text(encoding="utf-8").strip())
views += 1
counter_file.write_text(str(views), encoding="utf-8")

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="260" height="40">
  <rect width="260" height="40" rx="10" fill="#282a36"/>
  <text x="16" y="25" font-family="Fira Code, monospace" font-size="14" fill="#bd93f9">
    👀 Profile Views: {views}
  </text>
</svg>
"""

(ASSETS / "profile_views.svg").write_text(svg, encoding="utf-8")
