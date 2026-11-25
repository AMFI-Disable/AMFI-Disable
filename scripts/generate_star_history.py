"""Render public repository stars for both owners from GitHub's stargazer dates."""

import itertools
import json
import subprocess
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

OWNERS = {"AMFI-Disable": "users", "BigBrainDevBros": "orgs"}
ROOT = Path(__file__).resolve().parents[1]


def pages(endpoint):
    result = subprocess.check_output([
        "gh", "api", "--paginate", "--slurp", "-H",
        "Accept: application/vnd.github.star+json", endpoint,
    ], text=True)
    return itertools.chain.from_iterable(json.loads(result))


def collect():
    history = Counter()
    totals = {}
    for owner, kind in OWNERS.items():
        total = 0
        scope = "owner" if kind == "users" else "public"
        for repo in pages(f"{kind}/{owner}/repos?type={scope}&per_page=100"):
            if repo["private"] or repo["owner"]["login"].lower() != owner.lower():
                continue
            if repo["stargazers_count"] == 0:
                continue
            stars = list(pages(f'repos/{repo["full_name"]}/stargazers?per_page=100'))
            if len(stars) != repo["stargazers_count"]:
                raise ValueError(f'Star count changed during collection for {repo["full_name"]}')
            history.update(date.fromisoformat(star["starred_at"][:10]) for star in stars)
            total += len(stars)
        totals[owner] = total
    return history, totals


def render(history, totals, today):
    total = sum(totals.values())
    start = min(history, default=today)
    days = max(1, (today - start).days)
    path = ["M 44 190"]
    running = 0
    for day, count in sorted(history.items()):
        running += count
        x = 44 + 612 * (day - start).days / days
        y = 190 - 100 * running / max(total, 1)
        path.append(f"H {x:.1f} V {y:.1f}")
    path.append("H 656")
    breakdown = " · ".join(f"{owner} {count}" for owner, count in totals.items())
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 245" role="img" aria-labelledby="title desc">
  <title id="title">{total} public repository stars</title>
  <desc id="desc">{breakdown}. Cumulative dates of current stars as of {today} UTC.</desc>
  <rect width="700" height="245" rx="12" fill="#101c2e"/>
  <g fill="#f6f8fa" font-family="system-ui,sans-serif">
    <text x="32" y="39" font-size="24" font-weight="700">{total} public repository stars</text>
    <text x="32" y="65" font-size="16" fill="#c7d7eb">{breakdown}</text>
    <path d="M44 90H656 M44 140H656 M44 190H656" stroke="#36465a" fill="none"/>
    <text x="37" y="95" text-anchor="end" font-size="12">{total}</text>
    <text x="37" y="195" text-anchor="end" font-size="12">0</text>
    <path d="{' '.join(path)}" stroke="#72dfcb" stroke-width="3" fill="none"/>
    <text x="44" y="220" font-size="14">{start}</text>
    <text x="656" y="220" text-anchor="end" font-size="14">{today} UTC</text>
  </g>
</svg>
'''


if __name__ == "__main__":
    events, owner_totals = collect()
    today = datetime.now(timezone.utc).date()
    (ROOT / "assets/star-history.svg").write_text(render(events, owner_totals, today))
