import json
import unittest
from unittest.mock import patch

from update_star_history import profile_section, public_counts


def repository(owner, name, visibility="public", stars=0):
    return {"full_name": f"{owner}/{name}", "owner": {"login": owner},
            "visibility": visibility, "stargazers_count": stars}


class PublicStarTests(unittest.TestCase):
    def test_scope_pagination_and_zero(self):
        personal = [[repository("AMFI-Disable", "one", stars=3), repository("other", "external")],
                    [repository("AMFI-Disable", "two"), repository("AMFI-Disable", "hidden", "private")]]
        org = [[repository("BigBrainDevBros", "three", stars=2)]]
        with patch("subprocess.check_output", side_effect=[json.dumps(personal), json.dumps(org)]):
            counts = public_counts()
        self.assertEqual(counts, {"AMFI-Disable/one": 3, "AMFI-Disable/two": 0, "BigBrainDevBros/three": 2})
        section = profile_section(counts, "2026-11-26")
        self.assertIn("5 public stars", section)
        self.assertIn("AMFI-Disable%2Ftwo", section)
        self.assertNotIn("hidden", section)

    def test_missing_owner_rejects_partial_snapshot(self):
        with patch("subprocess.check_output", return_value="[[]]"):
            with self.assertRaises(ValueError):
                public_counts()
