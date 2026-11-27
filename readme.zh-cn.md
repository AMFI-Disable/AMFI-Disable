# AMFI-Disable

[English](readme.md) · [参与贡献](contributing.zh-cn.md) · [项目主页](https://amfi-disable.github.io/)

这里收录我的 macOS 应用、终端工具、浏览器扩展，以及 BigBrainDevBros 成员共同维护的游戏。主页可以按类别、项目名或技术搜索，也可以直接复制安装命令。

## 项目导航

| 分区 | 项目与用途 |
| --- | --- |
| [AMFI Studio](https://amfi-disable.github.io/#studio) | **BrewStore** 用于查找、安装和更新 Homebrew 软件。**Juicer** 集中管理本机应用、服务和开发缓存。**PathDeck** 用于查看和调整 shell 路径、别名与环境变量，并备份配置。 |
| [AMFI Terminal](https://amfi-disable.github.io/#terminal) | **OmniSuite** 帮助辩手整理证据卡片、检索材料和编写简报。**Brew-Ghost** 结合 Homebrew 软件包和 shell 历史查找可能闲置的工具。 |
| [AMFI Hangar](https://amfi-disable.github.io/#hangar) | **GeoFS Extension** 将飞行控制、仪表、检查单和着陆记录整合到模拟器。**GimSell** 预览储物柜里可见的重复藏品。**Lichess-AutoPlayer** 提供独立的[预走练习棋盘](https://amfi-disable.github.io/Lichess-AutoPlayer/practice.html)。 |
| [AMFI Arcade](https://amfi-disable.github.io/#arcade) | [刃影](https://bigbraindevbros.github.io/RenYing/)是水墨武侠格斗游戏。[FaceOff](https://bigbraindevbros.github.io/FaceOff/)提供限时擂台对决。[VANTAGE](https://bigbraindevbros.github.io/VANTAGE/)是 HilbertQiu 创作的程序化城市射击游戏。 |

## 安装与活动

Juicer 和 BrewStore 的当前 cask 由[中央 Homebrew Tap](https://github.com/AMFI-Disable/Homebrew-Tap)发布。安装时选择所需的应用：

```sh
brew install --cask AMFI-Disable/tap/juicer
brew install --cask AMFI-Disable/tap/brewstore
```

以前的独立 tap 已归档。应用的发行记录和系统要求以对应项目为准。[公开仓库星标统计](readme.md#github-star-history--activity)分别列出个人和组织的总数及快照日期；同一页还展示个人贡献图。项目主要采用 Swift、SwiftUI、Python、TypeScript 和浏览器原生接口。
