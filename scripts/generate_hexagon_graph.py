#!/usr/bin/env python3
"""Generate dark and light hexagonal GitHub contribution graph SVGs."""

import http.client
import math
import os
import re
import subprocess
import urllib.request

USERNAME = "AMFI-Disable"
URL = f"https://github.com/users/{USERNAME}/contributions"

THEMES = {
    "dark": {
        "bg": "#0d1117",
        "border": "#30363d",
        "text": "#e6edf3",
        "muted": "#8b949e",
        "levels": ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"],
        "stroke": "#0b0e14",
    },
    "light": {
        "bg": "#ffffff",
        "border": "#d0d7de",
        "text": "#1f2328",
        "muted": "#656d76",
        "levels": ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"],
        "stroke": "#ffffff",
    },
}


def fetch_contributions() -> tuple[int, dict[tuple[int, int], tuple[int, str]]]:
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except http.client.IncompleteRead as exc:
        html = exc.partial.decode("utf-8", errors="ignore")
    if "contribution-day-component" not in html:
        html = subprocess.check_output(["curl", "-sL", URL], text=True)

    total_match = re.search(r"([\d,]+)\s+contributions?\s+in\s+the\s+last\s+year", html)
    total = int(total_match.group(1).replace(",", "")) if total_match else 0

    cells: dict[tuple[int, int], tuple[int, str]] = {}
    pattern = re.compile(
        r'data-date="([^"]+)"[^>]*id="contribution-day-component-(\d+)-(\d+)"[^>]*data-level="(\d+)"'
    )
    for date_str, row_s, col_s, level_s in pattern.findall(html):
        cells[(int(row_s), int(col_s))] = (int(level_s), date_str)
    return total, cells


def hex_points(cx: float, cy: float, r: float) -> str:
    pts = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        pts.append(f"{cx + r * math.cos(angle):.2f},{cy + r * math.sin(angle):.2f}")
    return " ".join(pts)


def render_svg(theme_name: str, total: int, cells: dict[tuple[int, int], tuple[int, str]]) -> str:
    t = THEMES[theme_name]
    max_col = max((c for _, c in cells), default=52)
    r = 7.4
    dx = math.sqrt(3) * r + 1.6
    dy = 1.5 * r + 1.6
    pad_x = 24.0
    pad_top = 48.0
    pad_bottom = 36.0

    width = pad_x * 2 + (max_col + 1.5) * dx
    height = pad_top + 7 * dy + pad_bottom

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}" role="img" aria-label="{USERNAME} hexagonal contribution graph">',
        f'  <rect x="0.5" y="0.5" width="{width - 1:.0f}" height="{height - 1:.0f}" rx="12" fill="{t["bg"]}" stroke="{t["border"]}"/>',
        f'  <text x="{pad_x}" y="28" fill="{t["text"]}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="13" font-weight="600">@{USERNAME} · {total:,} contributions in the last year</text>',
    ]

    for (row, col), (level, date_str) in sorted(cells.items()):
        cx = pad_x + r + col * dx + (dx / 2.0 if row % 2 == 1 else 0.0)
        cy = pad_top + r + row * dy
        fill = t["levels"][min(max(level, 0), 4)]
        lines.append(
            f'  <polygon points="{hex_points(cx, cy, r)}" fill="{fill}" stroke="{t["stroke"]}" stroke-width="0.6"><title>{date_str}: level {level}</title></polygon>'
        )

    # Legend
    ly = height - 16
    lx_start = width - pad_x - 5 * 16 - 42
    lines.append(
        f'  <text x="{lx_start - 32:.1f}" y="{ly + 4:.1f}" fill="{t["muted"]}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11">Less</text>'
    )
    for i, color in enumerate(t["levels"]):
        lines.append(
            f'  <polygon points="{hex_points(lx_start + i * 16, ly, 6.0)}" fill="{color}" stroke="{t["stroke"]}" stroke-width="0.5"/>'
        )
    lines.append(
        f'  <text x="{lx_start + 5 * 16 + 2:.1f}" y="{ly + 4:.1f}" fill="{t["muted"]}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11">More</text>'
    )
    lines.append("</svg>\n")
    return "\n".join(lines)


def main() -> None:
    total, cells = fetch_contributions()
    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
    os.makedirs(out_dir, exist_ok=True)
    for theme in ("dark", "light"):
        svg = render_svg(theme, total, cells)
        out_path = os.path.join(out_dir, f"contribution-hexagon-{theme}.svg")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Wrote {out_path} ({len(cells)} days, {total} total)")


if __name__ == "__main__":
    main()
