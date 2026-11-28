# Changelog

All notable changes, profile revisions, and portfolio updates for the AMFI-Disable profile are documented in this file.

---

## [Unreleased]

### Documentation

- Published a bilingual project roadmap (`docs/roadmap.md`, `docs/roadmap.zh-cn.md`) with acceptance checks for each area.
- Added Simplified Chinese project and contribution guides and bilingual feedback templates.

### Added

- **GeoFS_Extension Portfolio Entry**: Replaced legacy `GeoFS-V3.9` ecosystem links with unified [GeoFS_Extension](https://github.com/AMFI-Disable/GeoFS_Extension) Manifest V3 extension entry.
- **TornTools Portfolio Entry**: Added [TornTools](https://github.com/AMFI-Disable/TornTools) to the Web Extensions section in `readme.md`, documenting its TypeScript and WXT browser extension architecture.
- **DustIII Portfolio Entry**: Added [DustIII](https://github.com/AMFI-Disable/DustIII) to the interactive games section, covering its CS2-style bomb defusal ruleset, tactical bot AI, and static Three.js delivery, with a direct link to the live GitHub Pages build.

### Changed

- Refreshed dark and light hexagonal contribution SVG assets via the scheduled activity graph workflow.

- Refresh the public Star History scope and owner totals from the daily inventory. Link the chess showcase to the standalone practice board.

- Restored the hosted Star History chart in `readme.md`, removed temporary local SVG star-history generator scripts (`scripts/generate_star_history.py`, `scripts/test_star_history.py`) and `assets/star-history.svg`, and refreshed contribution hexagon SVGs.
- Generate the combined public star history and owner totals daily from GitHub. Direct Studio installs to the central tap.

- Restored the Star History chart in `readme.md`, refreshed hexagonal contribution SVG assets, and updated `.github/workflows/update-contributions.yml` to use `actions/checkout@v7`, `actions/setup-python@v7`, and `AMFI-Disable` git author identity.
- Consolidated Homebrew distribution references in `readme.md` to point `Juicer` and `BrewStore` cask installs to the central `AMFI-Disable/tap` repository and mark `Homebrew-Juicer` and `Homebrew-BrewStore` as archived.
- Reorganized `readme.md` into standardized portfolio categories (`macOS Native Apps`, `Browser Extensions And Userscripts`, `Browser Games`, `CLI And Developer Tools`, `Homebrew Distribution`) with aligned tech stacks and fork attributions.
- Restored active project maintenance status references across developer profile in `readme.md`, removing archived markers from featured applications (BrewStore, Juicer, PathDeck, OmniSuite) and Homebrew taps (Homebrew-BrewStore, Homebrew-Juicer).
- Updated Juicer profile summary in `readme.md` to highlight its native SwiftUI local-first systems architecture and removed deprecated JuicerKit references.
- Overhauled `.github/` issue/PR templates and `security.md` to remove emoji status markers, use plain-text `Yes` / `No` values, and standardize vulnerability reporting workflows.

---

## [2.0.0] - Portfolio Restructuring And Identity Realignment

### Added

- **AMFI-Disable Casing Alignment**: Standardized all developer references and remote repository links to `AMFI-Disable`.
- **Featured macOS Applications**: Added comprehensive coverage for [Juicer](https://github.com/AMFI-Disable/Juicer), [BrewStore](https://github.com/AMFI-Disable/BrewStore), and [PathDeck](https://github.com/AMFI-Disable/PathDeck).
- **Homebrew Taps Section**: Linked dedicated tap repositories (`Homebrew-Juicer`, `Homebrew-BrewStore`, `Homebrew-Tap`).
- **Policy Compliance Check**: Removed obsolete references and ensured zero direct binary download links in adherence to GitHub policies.

---

## [1.0.0] - Initial Profile Publication

### Added

- **Initial Portfolio Layout**: Initial public developer profile introducing OmniSuite, GeoFS flight simulator suite, and browser extensions.
