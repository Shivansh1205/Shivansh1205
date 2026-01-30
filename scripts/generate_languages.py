import os, requests
from pathlib import Path
from collections import Counter

USER = "Shivansh1205"
TOKEN = os.environ.get("GH_TOKEN")

ASSETS = Path("assets")
ASSETS.mkdir(exist_ok=True)

headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}

repos = requests.get(f"https://api.github.com/users/{USER}/repos?per_page=100", headers=headers).json()

lang_counter = Counter()
for r in repos:
    if not isinstance(r, dict):
        continue
    url = r.get("languages_url")
    if not url:
        continue
    langs = requests.get(url, headers=headers).json()
    for k, v in langs.items():
        lang_counter[k] += v

top = lang_counter.most_common(5)
lines = "\n".join(
    [f'<text x="20" y="{70+i*22}" font-family="Fira Code, monospace" font-size="14" fill="#f8f8f2">{i+1}. {name}</text>'
     for i, (name, _) in enumerate(top)]
)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="320" height="160">
  <rect width="320" height="160" rx="14" fill="#282a36"/>
  <text x="20" y="35" font-family="Fira Code, monospace" font-size="18" fill="#50fa7b">
    Top Languages
  </text>
  {lines}
</svg>
"""

(ASSETS / "languages.svg").write_text(svg, encoding="utf-8")
