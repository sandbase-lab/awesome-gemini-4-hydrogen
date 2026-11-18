# Gemini 4 Hydrogen 对比 Claude Opus 5.5、Fable 5.2、Gemini 4 Carbon 等模型

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们测到的。** Lab [Evals 榜单][evals] 展示 Artificial Analysis 的数据；Lab [Pelican Test][pelican] 用同一份固定提示词跑每个模型并给结果打分。样本不大，但所有人的条件一致。
2. **创作者报告的。** 发在 X 上的同提示词运行，附他们自己的提示词、花费和耗时。有参考价值，但我们没有验证。

Gemini 4 Hydrogen 于 2026 年 11 月 12 日公布。本页依据的是发布时的数据，当时其中还没有这个模型的实测行。创作者一侧数据很多，因为模型刚出来，大家都在用同样的提示词去试它。

## 我们测到的：Lab Evals 榜单与 Pelican Test

**本合集所依据的数据中，Lab Evals 榜单和 Pelican Test 排行榜上都没有 Gemini 4 Hydrogen 这一行。** 在它出现之前，本页的任何实测数字都无法把它和其他模型放在一起比较。下表的对手行取自同系列 [MiniMax M3.1 Flash 合集](https://github.com/sandbase-lab/awesome-minimax-m3-1-flash/blob/main/docs/zh-CN/model-comparison.md)中记录的快照（Artificial Analysis 快照 2026-10-19；Pelican Test 读取于 2026-10-20）。它们不是 Gemini 4 Hydrogen 的结果。最新数据请查看[实时榜单][evals]。

| 模型（榜单上的行） | 智能指数（2026-10-19） | 单任务成本（2026-10-19） |
|---|---|---|
| **Gemini 4 Hydrogen** | **不在榜上** | — |
| Claude Opus 5.5 (Max) | 57.6（第 1） | $5.98（第 188） |
| Gemini 4 Argon (High) | 52.6（第 9） | $1.99（第 158） |
| GPT-6.1 Sol (Max) | 51.8（第 13） | $0.724（第 112） |
| DeepSeek V4.1 Flash 1017 (Max) | 45.1（第 36） | $0.262（第 74） |
| Claude Haiku 5.5 (Max) | 43.4（第 46） | $0.213（第 67） |

| 模型（排行榜上的行） | 得分（2026-10-20） | 平均成本 |
|---|---|---|
| **Gemini 4 Hydrogen** | **不在排行榜上** | — |
| openai/gpt-6.1-sol | 3.79 | $0.026 |
| google/gemini-4-argon | 3.75 | $0.150 |
| anthropic/claude-opus-5.5 | 3.46 | $0.223 |
| deepseek/deepseek-v4.1-flash | 3.44 | $0.017 |

这说明什么、不说明什么：

- **Gemini 4 Hydrogen 没有实测分数。** 下面创作者报告的价格，目前还无法和榜单对照。
- **榜单上的价格区间很大。** 上表对手的单任务成本从 $0.213 到 $5.98，所以同一提示词下相差几倍的成本差距是合理的。但它依然只是某位创作者的单次运行。

## 创作者报告的

发在 X 上的同提示词运行。数字按创作者自述：工具、推理设置和运行次数各不相同，往往只跑一次。点进链接可以两边一起看。成本是创作者自己的数字，不是我们的测量。

| 创作者 | 任务 | Gemini 4 Hydrogen | 对手 | 创作者结论 |
|---|---|---|---|---|
| [@marcthecreatorr][bikes] | SVG 女孩和猫骑连体自行车，黄金时刻 | 约 15 分钟，约 $0.9 API 费用（在 Cursor 中） | Claude Code 中的 Opus 5.5：约 1 小时，约 $18 API 费用 | Opus 在细节（夜间模式、音乐）上花了更多时间；Hydrogen "不到一美元就更快地做完了整个场景" |
| [@EnvolDev][rio] | "Rio Above the Clouds" 影片，一条提示词 | $6.21 · 1 小时 33 分 48 秒 | Opus 5.5：$60.89 · 2 小时 19 分 35 秒 · Fable 5.2：$76.04 · 1 小时 59 分 11 秒 · GPT-6 Astra：$16.89 · 34 分 06 秒 | "Gemini 4 Hydrogen 用 $6.21 做完了整部影片……但它是所有模型里最差的。" |
| [@EnvolDev][cathedral] | "Cathedral of Ice" 场景 | $4.27 · 1 小时 23 分 40 秒 | Gemini 4 Carbon：$8.83 · 2 小时 39 分 10 秒 · GPT-6.1 Sol：$3.11 · 54 分 19 秒 · Muse Spark 1.3：$5.56 · 2 小时 | GPT-6.1 Sol "是四个里最便宜、也最快的" |
| [@SidraMiconi][mito] | 线粒体马达模拟，一个应用 | 约 $0.36 · 201 秒，一次调用加一次相机修正 | — | 自己做的作品，没有对手 |
| [@noclipepe][walk] | 行走的生物，神经网络加遗传算法 | 27 代 · 最佳 7.5 米 · 36 分 43 秒 | Fable 5.2：29 代 · 最佳 7.4 米 · 1 小时 34 分 · Qwen 4 Max：32 代 · 最佳 6.1 米 · 1 小时 6 分 | "Gemini 以 10 厘米险胜 Fable。跪着赢的。只有 Fable 真的能走。" |
| [@DanielZambrini][daniel] | 火柴人对光标，对比 Fable 5.2 | 作者称它"是较小的模型，仍能做出相当不错的结果" | Fable 5.2 | "Fable 明显更好，但如果我赶时间又想省钱，用 Hydrogen 也完全可以" |
| [@analogalok][motor] | 电动机动画，单个 HTML 文件 | — | Qwen 4 Max、Qwen 3.8 Max | Hydrogen "在 3D 写实度和视觉清晰度上整体做得最好" |
| [@Aki_LIG][aki] | Three.js 骑自行车的鹈鹕，与早先模型同一提示词 | — | 早先的模型（6.1 Terra） | "在鹈鹕测试里从没见过这样的"（译文）；"输出完全不同" |
| [@SahilPanhotra][lion] | 狮子在四个季节里抛接球，带声音的交互式 SVG | — | Gemini 4 Carbon | Carbon "在原始细节和物理上更强"；Hydrogen 的季节切换和容器穿模"干净得多"，但抛接球是假的 |
| [@Dain0x][globe] | 三模型地球对比 | — | GPT-6.2 Sol · Fable 5.2 | "在我看来，这组视觉对比里 Fable 赢了。" |

请结合作者本人给出的限定来读这张表：

- 花费是作者的数字。Rio 帖子说明两次测试之间的设置有变化（这次是 Extra High，之前是 High），所以各次运行并不严格可比（[@EnvolDev][rio]）。
- 质量上意见分裂。Hydrogen 在一组对比中的 3D 写实度和行走比赛里受到好评；但在 Rio 影片和地球对比中，质量上的胜者是其他模型。
- 有一条帖子说整个成果都是 Hydrogen 做的，但作者的技术说明里写的是 ComfyUI 图生视频流程，用的是另一个模型。它不属于 HTML 页面的对比范畴（[@nyapan_mohy][nyapan]）。

这些帖子合起来的规律是：在花费上，Hydrogen 在这些对比中属于便宜的一档。按上面的数字我们自己算，Rio 影片的花费约为 Opus 5.5 的十分之一，大教堂场景约为 Gemini 4 Carbon 的一半。质量上结论并不一致，目前也没有实测榜单能支持任何一方。

## 重跑一次再相信对比

设置一变，结果就变。用同一提示词自己跑一遍：把提示词粘到 [Lab 文本竞技场][arena]，选两三个模型；或者按[教程](tutorial.md)用 API。

## 更多实测

- [Lab Evals 榜单][evals]：查看是否出现 Gemini 4 Hydrogen 的行，出现后请重新检查本页。
- [Lab Pelican Test][pelican]：同一提示词、同一评分方式，画作直接展示。
- [SandBase Lab 上的全部 AI 视频合集][collections]：其他模型的同类列表。

---

Lab 数据：[Evals 榜单][evals]（Artificial Analysis，2026-10-19 快照）与 [Pelican Test][pelican]（2026-10-20 读取），均按同系列列表中的记录引用，两者都没有 Gemini 4 Hydrogen 的行。创作者数据：他们本人的帖子，已附链接，未经我们独立验证。

[evals]: https://www.sandbase.ai/leaderboards?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[pelican]: https://www.sandbase.ai/arena/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-hydrogen&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[collections]: https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[bikes]: https://x.com/marcthecreatorr/status/2120956699951628637
[rio]: https://x.com/EnvolDev/status/2121701704139956250
[cathedral]: https://x.com/EnvolDev/status/2122105333887934810
[mito]: https://x.com/SidraMiconi/status/2121745863827697687
[walk]: https://x.com/noclipepe/status/2122349082723176738
[daniel]: https://x.com/DanielZambrini/status/2121289822677483740
[motor]: https://x.com/analogalok/status/2122221106304352257
[aki]: https://x.com/Aki_LIG/status/2121960943361896596
[lion]: https://x.com/SahilPanhotra/status/2120978349967458704
[globe]: https://x.com/Dain0x/status/2122075114883690862
[nyapan]: https://x.com/nyapan_mohy/status/2122253350808744004
