# Project Roadmap

[简体中文](roadmap.zh-cn.md) · [Project Directory](../readme.md)

These priorities describe the next checks for contributors. Each project maintainer decides when a change is ready to ship.

| Area | Next milestone | How to verify it |
| --- | --- | --- |
| Studio | Exercise Juicer upgrades, BrewStore recovery after an interrupted refresh, and PathDeck edits made while a shell profile is open. | Start from a previous installation on a disposable macOS account. Compare preferences, package state and shell configuration before and after cancellation or recovery. |
| Terminal | Make Brew-Ghost's inactivity evidence easier to review and preserve OmniSuite citations through export and recovery. | Try a history with missing dates and a copied evidence vault. Check that the user can review a package decision and trace an exported quote to its source. |
| Hangar | Complete GeoFS live flight checks and keep browser utilities usable when the host page changes. | Record simulator version, aircraft, pilot input and observed response. For map notes and inventory tools, use user-owned or synthetic data. |
| Arcade | Verify RenYing keyboard and save flows and run a FaceOff room through disconnect and rematch. Coordinate VANTAGE distribution changes with its maintainer. | Compare both peers' scores and state after reconnecting. Record the game revision, language and screen size with each finding. |
| Distribution | Verify migration from archived taps to the active Homebrew tap. | Use an existing installation and a nondefault applications directory. Check the binary location and preferences after migration. |
| Website | Keep the searchable directory accessible when its data is missing or outdated. | Navigate with a keyboard and screen reader at mobile and desktop widths. Verify the language link, update date and links to each project. |

For current release availability and open issues, follow the links in the [project directory](../readme.md). Release tags use a lowercase v and semantic version numbers after the project's acceptance checks pass.
