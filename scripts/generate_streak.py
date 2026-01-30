import os, requests
from pathlib import Path
from datetime import datetime, timedelta

USER = "Shivansh1205"
TOKEN = os.environ.get("GH_TOKEN")
ASSETS = Path("assets")
ASSETS.mkdir(exist_ok=True)

headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}

# We approximate streak based on last 90 days commit activity
events = requests.get(
    f"https://api.github.com/users/{USER}/events/public?per_page=100",
    headers=headers
).json()

days = set()
for e in events:
    if not isinstance(e, dict):
        continue
    created = e.get("created_at")
    if created:
        days.add(created[:10])

# Calculate streak
today = datetime.utcnow().date()
streak = 0
for i in range(0, 365):
    d = today - timedelta(days=i)
    if str(d) in days:
        streak += 1
    else:
        break

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="460" height="120">
  <rect width="460" height="120" rx="14" fill="#282a36"/>
  <text x="20" y="35" font-family="Fira Code, monospace" font-size="18" fill="#8be9fd">
    Current Streak
  </text>
  <text x="20" y="80" font-family="Fira Code, monospace" font-size="28" fill="#f8f8f2">
    🔥 {streak} days
  </text>
</svg>
"""

(ASSETS / "streak.svg").write_text(svg, encoding="utf-8")
