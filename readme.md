# AMFI-Disable

Welcome! I am a software engineer focused on native macOS desktop applications, browser extensions, interactive web games, and developer CLI tooling. I build local-first, highly responsive software with clean interfaces and zero telemetry.

---

## macOS Native Apps

### [Juicer](https://github.com/AMFI-Disable/Juicer)

Local-first macOS system utility consolidating app uninstallers, orphan cleaners, `launchd` editors, cache pruners, and system tweakers.

- **Tech Stack**: Swift, SwiftUI (macOS 14+)
- **Install**: `brew tap AMFI-Disable/tap && brew install --cask juicer`

### [BrewStore](https://github.com/AMFI-Disable/BrewStore)

Native macOS GUI and CLI companion for installing, updating, auditing, and managing Homebrew casks, formulae, and services.

- **Tech Stack**: Swift, SwiftUI (macOS 14+)
- **Install**: `brew tap AMFI-Disable/tap && brew install --cask brewstore`

### [PathDeck](https://github.com/AMFI-Disable/PathDeck)

Native macOS GUI studio for visually managing, reordering, and backing up shell `PATH` entries, aliases, and environment variables.

- **Tech Stack**: Swift, SwiftUI (macOS 14+)

---

## Browser Extensions And Userscripts

### [GeoFS_Extension](https://github.com/AMFI-Disable/GeoFS_Extension)

Unified Manifest V3 Chrome extension (plus archived legacy userscripts) providing an all-in-one flight deck companion for GeoFS V3.9/V4.0.

- **Tech Stack**: TypeScript, JavaScript, Vite, Vitest

### [Lichess-AutoPlayer](https://github.com/AMFI-Disable/Lichess-AutoPlayer)

Userscript powered by Stockfish WebAssembly for automated Lichess quick-pairing and chess play with an optional native mouse companion server.

- **Tech Stack**: JavaScript, Node.js, Stockfish WASM, C++

### [GimSell_Gimkit-Seller](https://github.com/AMFI-Disable/GimSell_Gimkit-Seller)

In-page userscript with a floating widget that automates selling duplicate cosmetics (Gims, trails, stickers) in the Gimkit Locker.

- **Tech Stack**: JavaScript (Tampermonkey / Violentmonkey)

### [FMG_Free-MapGenie](https://github.com/AMFI-Disable/FMG_Free-MapGenie)

Chromium/Firefox extension (WXT v3 rewrite in progress) that unlocks MapGenie Pro features client-side using Dexie.

- **Tech Stack**: TypeScript, JavaScript, WXT, Dexie (forked from `V1P3R-FMG/free-map-genie`)

### [TornTools](https://github.com/AMFI-Disable/TornTools)

Browser extension adding quality-of-life tools, calculators, and UI enhancements for the text-based RPG Torn.com.

- **Tech Stack**: TypeScript, Bun (forked from `Mephiles/torntools_extension`)

---

## Browser Games

### [RenYing](https://github.com/AMFI-Disable/RenYing)

Ink-wash martial-arts 1v1 fighting game in the browser featuring 16 heroes, serverless WebRTC P2P multiplayer, and an optional Cloudflare Worker.

- **Tech Stack**: HTML5 Canvas, JavaScript, WebRTC, Cloudflare Workers
- **Play**: [amfi-disable.github.io/RenYing](https://amfi-disable.github.io/RenYing/)

### [DustIII](https://github.com/AMFI-Disable/DustIII)

Static-site browser-native 5v5 bomb defusal shooter on Dust II with CS2-style economy, spray patterns, wallbangs, utility, and four bot tiers.

- **Tech Stack**: JavaScript, Three.js (WebGL 2 / ES Modules)
- **Play**: [amfi-disable.github.io/DustIII](https://amfi-disable.github.io/DustIII/)

---

## CLI And Developer Tools

### [OmniSuite](https://github.com/AMFI-Disable/OmniSuite)

Terminal workstation (CLI + Textual TUI) for competitive debate/forensics to store, filter, and rapidly retrieve AFF/NEG debate cards during crossfire.

- **Tech Stack**: Python 3.10+, Textual, Docker, `uv`

### [Brew-Ghost](https://github.com/AMFI-Disable/Brew-Ghost)

Behavioral Homebrew cleanup CLI that analyzes Bash/Zsh shell history to safely identify and purge packages unused for over 90 days.

- **Tech Stack**: Python, Shell (Bash / Zsh)
- **Install**: `brew tap AMFI-Disable/tap && brew install brew-ghost`

---

## Homebrew Distribution

- **[Homebrew-Tap](https://github.com/AMFI-Disable/Homebrew-Tap)**: Central Homebrew tap (`AMFI-Disable/tap`) hosting casks (`casks/juicer.rb`, `casks/brewstore.rb`) and CLI formulae (`formula/brew-ghost.rb`).
- *Legacy taps ([Homebrew-Juicer](https://github.com/AMFI-Disable/Homebrew-Juicer), [Homebrew-BrewStore](https://github.com/AMFI-Disable/Homebrew-BrewStore)) have been archived and consolidated into `Homebrew-Tap`.*

---

## Technical Skills And Technologies

| Category | Technologies |
| :--- | :--- |
| **Languages** | Swift, TypeScript, JavaScript, Python, C++, Ruby, Shell (Bash / Zsh) |
| **macOS & Desktop** | SwiftUI, AppKit, Combine, Xcode, XcodeGen |
| **Web & Extensions** | Manifest V3, WXT, Vite, Vitest, Three.js, HTML5 Canvas, WebRTC, Stockfish WASM |
| **CLI & Tooling** | Textual, Bun, `uv`, Docker, GitHub Actions, Homebrew Packaging |

---

## Core Engineering Principles

- **Local-First Privacy**: Zero telemetry, zero tracker dependencies, and complete client-side data ownership.
- **Native Desktop Performance**: Native SwiftUI and AppKit implementations designed to feel integrated into macOS.
- **Clean Code & Test Integrity**: Consistent architecture, automated CI validation, and clear documentation across all repositories.

---

## GitHub Activity & Stars

[![Total Stars](https://img.shields.io/github/stars/AMFI-Disable?affiliations=OWNER&style=flat-square&label=Total%20Stars&color=f59e0b)](https://github.com/AMFI-Disable?tab=repositories)

> **105 combined stars** across all AMFI-Disable repositories.

### Contribution Hexagon Graph

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/AMFI-Disable/AMFI-Disable/main/assets/contribution-hexagon-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/AMFI-Disable/AMFI-Disable/main/assets/contribution-hexagon-light.svg" />
  <img alt="AMFI-Disable Hexagonal Contribution Graph" src="https://raw.githubusercontent.com/AMFI-Disable/AMFI-Disable/main/assets/contribution-hexagon-dark.svg" />
</picture>

### Star History

<a href="https://www.star-history.com/?type=date&repos=AMFI-Disable%2FAMFI-Disable%2CAMFI-Disable%2FAMFI-Disable.github.io%2CAMFI-Disable%2FBrew-Ghost%2CAMFI-Disable%2FBrewStore%2CAMFI-Disable%2FDustIII%2CAMFI-Disable%2FFMG_Free-MapGenie%2CAMFI-Disable%2FGeoFS_Extension%2CAMFI-Disable%2FGimSell_Gimkit-Seller%2CAMFI-Disable%2FHomebrew-BrewStore%2CAMFI-Disable%2FHomebrew-Juicer%2CAMFI-Disable%2FHomebrew-Tap%2CAMFI-Disable%2FJuicer%2CAMFI-Disable%2FLichess-AutoPlayer%2CAMFI-Disable%2FOmniSuite%2CAMFI-Disable%2FPathDeck%2CAMFI-Disable%2FRenYing%2CAMFI-Disable%2FTornTools">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=AMFI-Disable/AMFI-Disable%2CAMFI-Disable/AMFI-Disable.github.io%2CAMFI-Disable/Brew-Ghost%2CAMFI-Disable/BrewStore%2CAMFI-Disable/DustIII%2CAMFI-Disable/FMG_Free-MapGenie%2CAMFI-Disable/GeoFS_Extension%2CAMFI-Disable/GimSell_Gimkit-Seller%2CAMFI-Disable/Homebrew-BrewStore%2CAMFI-Disable/Homebrew-Juicer%2CAMFI-Disable/Homebrew-Tap%2CAMFI-Disable/Juicer%2CAMFI-Disable/Lichess-AutoPlayer%2CAMFI-Disable/OmniSuite%2CAMFI-Disable/PathDeck%2CAMFI-Disable/RenYing%2CAMFI-Disable/TornTools&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=AMFI-Disable/AMFI-Disable%2CAMFI-Disable/AMFI-Disable.github.io%2CAMFI-Disable/Brew-Ghost%2CAMFI-Disable/BrewStore%2CAMFI-Disable/DustIII%2CAMFI-Disable/FMG_Free-MapGenie%2CAMFI-Disable/GeoFS_Extension%2CAMFI-Disable/GimSell_Gimkit-Seller%2CAMFI-Disable/Homebrew-BrewStore%2CAMFI-Disable/Homebrew-Juicer%2CAMFI-Disable/Homebrew-Tap%2CAMFI-Disable/Juicer%2CAMFI-Disable/Lichess-AutoPlayer%2CAMFI-Disable/OmniSuite%2CAMFI-Disable/PathDeck%2CAMFI-Disable/RenYing%2CAMFI-Disable/TornTools&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=AMFI-Disable/AMFI-Disable%2CAMFI-Disable/AMFI-Disable.github.io%2CAMFI-Disable/Brew-Ghost%2CAMFI-Disable/BrewStore%2CAMFI-Disable/DustIII%2CAMFI-Disable/FMG_Free-MapGenie%2CAMFI-Disable/GeoFS_Extension%2CAMFI-Disable/GimSell_Gimkit-Seller%2CAMFI-Disable/Homebrew-BrewStore%2CAMFI-Disable/Homebrew-Juicer%2CAMFI-Disable/Homebrew-Tap%2CAMFI-Disable/Juicer%2CAMFI-Disable/Lichess-AutoPlayer%2CAMFI-Disable/OmniSuite%2CAMFI-Disable/PathDeck%2CAMFI-Disable/RenYing%2CAMFI-Disable/TornTools&type=date&legend=top-left" />
  </picture>
</a>
