import os, requests
from pathlib import Path

USER = "Shivansh1205"
TOKEN = os.environ.get("GH_TOKEN")

ASSETS = Path("assets")
ASSETS.mkdir(exist_ok=True)

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Basic user info
u = requests.get(f"https://api.github.com/users/{USER}", headers=headers).json()
repos = requests.get(f"https://api.github.com/users/{USER}/repos?per_page=100", headers=headers).json()

public_repos = u.get("public_repos", 0)
followers = u.get("followers", 0)
total_stars = sum(r.get("stargazers_count", 0) for r in repos if isinstance(r, dict))
total_forks = sum(r.get("forks_count", 0) for r in repos if isinstance(r, dict))

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="460" height="160">
  <rect width="460" height="160" rx="14" fill="#282a36"/>
  <text x="20" y="35" font-family="Fira Code, monospace" font-size="18" fill="#ff79c6">
    GitHub Stats
  </text>

  <text x="20" y="70" font-family="Fira Code, monospace" font-size="14" fill="#f8f8f2">
    ⭐ Stars: {total_stars}
  </text>
  <text x="20" y="95" font-family="Fira Code, monospace" font-size="14" fill="#f8f8f2">
    🍴 Forks: {total_forks}
  </text>
  <text x="20" y="120" font-family="Fira Code, monospace" font-size="14" fill="#f8f8f2">
    📦 Public Repos: {public_repos}
  </text>
  <text x="20" y="145" font-family="Fira Code, monospace" font-size="14" fill="#f8f8f2">
    👥 Followers: {followers}
  </text>
</svg>
"""

(ASSETS / "stats.svg").write_text(svg, encoding="utf-8")
