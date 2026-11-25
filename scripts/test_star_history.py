import unittest
import xml.etree.ElementTree as ET
from datetime import date
from unittest.mock import patch

from generate_star_history import collect, render


class StarHistoryTests(unittest.TestCase):
    def test_scope_and_dates(self):
        def repo(name, private=False, stars=2):
            return {"owner": {"login": name}, "private": private,
                    "stargazers_count": stars, "full_name": f"{name}/test"}

        responses = [
            [repo("AMFI-Disable"), repo("AMFI-Disable", private=True), repo("unrelated")],
            [{"starred_at": "2026-11-20T05:00:00Z"}] * 2,
            [repo("BigBrainDevBros", stars=0)],
        ]
        with patch("generate_star_history.pages", side_effect=responses):
            history, totals = collect()
        self.assertEqual(totals, {"AMFI-Disable": 2, "BigBrainDevBros": 0})
        self.assertEqual(history, {date(2026, 11, 20): 2})
        chart = ET.fromstring(render(history, totals, date(2026, 11, 25)))
        self.assertIn("2 public repository stars", "".join(chart.itertext()))

    def test_incomplete_page_fails(self):
        repo = {"owner": {"login": "AMFI-Disable"}, "private": False,
                "stargazers_count": 2, "full_name": "AMFI-Disable/test"}
        with patch("generate_star_history.pages", side_effect=[[repo], []]):
            with self.assertRaises(ValueError):
                collect()

    def test_empty_chart(self):
        chart = ET.fromstring(render({}, {}, date(2026, 11, 25)))
        self.assertIn("0 public repository stars", "".join(chart.itertext()))
