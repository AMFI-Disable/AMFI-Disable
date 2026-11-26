"""Refresh the public repository snapshot shared by the profile and project hub."""

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
OWNERS = {"AMFI-Disable": "users", "BigBrainDevBros": "orgs"}
START = "<!-- public-star-history:start -->"
END = "<!-- public-star-history:end -->"


def public_counts():
    counts = {}
    for owner, kind in OWNERS.items():
        endpoint = f"{kind}/{owner}/repos?per_page=100&type={'owner' if kind == 'users' else 'public'}"
        pages = json.loads(subprocess.check_output(["gh", "api", "--paginate", "--slurp", endpoint]))
        for page in pages:
            for repo in page:
                if repo["visibility"] == "public" and repo["owner"]["login"].lower() == owner.lower():
                    counts[repo["full_name"]] = repo["stargazers_count"]
        if not any(name.startswith(owner + "/") for name in counts):
            raise ValueError(f"No public repositories returned for {owner}")
    return dict(sorted(counts.items()))


def profile_section(repos, checked):
    query = quote(",".join(repos), safe="")
    chart = f"https://api.star-history.com/chart?repos={query}&amp;type=date"
    totals = [sum(count for name, count in repos.items() if name.startswith(owner + "/")) for owner in OWNERS]
    return f"""{START}
[![AMFI-Disable stars](https://img.shields.io/badge/AMFI--Disable-{totals[0]}-f59e0b?style=flat-square)](https://github.com/AMFI-Disable?tab=repositories) [![BigBrainDevBros stars](https://img.shields.io/badge/BigBrainDevBros-{totals[1]}-f59e0b?style=flat-square)](https://github.com/orgs/BigBrainDevBros/repositories)

**{sum(totals)} public stars** across {len(repos)} repositories. AMFI-Disable has {totals[0]} and BigBrainDevBros has {totals[1]}. Snapshot from {checked} UTC.

### Combined Star History

<a href="https://www.star-history.com/?type=date&amp;repos={query}">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="{chart}&amp;theme=dark&amp;legend=top-left" />
    <img alt="Star history for public AMFI-Disable and BigBrainDevBros repositories" src="{chart}&amp;legend=top-left" />
  </picture>
</a>
{END}"""


def main():
    readme = ROOT / "readme.md"
    before, section = readme.read_text().split(START)
    _, after = section.split(END)
    repos = public_counts()
    snapshot = ROOT / "assets/public-stars.json"
    previous = json.loads(snapshot.read_text()) if snapshot.exists() else {}
    checked = previous.get("date") if previous.get("repos") == repos else datetime.now(timezone.utc).date().isoformat()
    snapshot.write_text(json.dumps({"date": checked, "repos": repos}, indent=2) + "\n")
    readme.write_text(before + profile_section(repos, checked) + after)


if __name__ == "__main__":
    main()
