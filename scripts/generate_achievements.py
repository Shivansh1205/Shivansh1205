from pathlib import Path

ASSETS = Path("assets")
ASSETS.mkdir(exist_ok=True)

# Your custom trophies (self hosted)
items = [
    "🏆 455+ LeetCode Problems Solved",
    "🧠 AI/ML Projects (Healthcare + Analytics)",
    "🌍 Open Source Contributor",
    "📊 Streamlit Dashboards",
    "🐳 Docker + SQL + GitHub",
]

lines = "\n".join([
    f'<text x="20" y="{60+i*22}" font-family="Fira Code, monospace" font-size="14" fill="#f8f8f2">{t}</text>'
    for i, t in enumerate(items)
])

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="650" height="190">
  <rect width="650" height="190" rx="14" fill="#282a36"/>
  <text x="20" y="35" font-family="Fira Code, monospace" font-size="18" fill="#ffb86c">
    Achievements
  </text>
  {lines}
</svg>
"""

(ASSETS / "achievements.svg").write_text(svg, encoding="utf-8")
