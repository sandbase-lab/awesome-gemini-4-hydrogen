# Gemini 4 Hydrogen 提示词写法：如何为视频提示 Gemini 4 Hydrogen

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

Gemini 4 Hydrogen 不直接输出视频。它写代码：一个独立的 HTML 页面（含 Three.js 或 SVG 动画），或一个单独的 SVG 文件。作者再把输出的页面播放过程录下来。下面的写法来自作者随视频公开的提示词，每条都链接到它来自的帖子。合集还很新，所以本指南目前有七条写法，并会随着公开的提示词增多而增加。

## 1. 要一个文件，并说明库怎么加载

在开头几句就说清交付物和加载方式。电动机动画的提示词正是这么写的：

- "create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn"（[@analogalok][motor]）。作者写道 Hydrogen"在 3D 写实度和视觉清晰度上整体做得最好"，建出了弯曲的马蹄形磁铁和细致的换向器。

这里大多数提示词都用单个 HTML 文件加 CDN 库，它也不需要构建步骤，录制起来最省事。

## 2. 指明渲染方式，并说清楚物理上要发生什么

渲染方式决定页面长什么样、哪里会出问题。点名渲染方式，再写清楚你想要的物理行为，结果会更容易检查：

- 不含 JavaScript 的 SVG 场景："create an SVG of a girl and her cat on joined bikes, golden hour, ghibli style"（[@marcthecreatorr][bikes]）。作者称在 Cursor 里用了约 15 分钟、约 $0.9 的 API 费用。
- 带声音的交互式 SVG：一只狮子在四个季节里骑车、抛接球，并带 Web Audio 音效（[@SahilPanhotra][lion]）。作者发现抛接球是假的，球悬在原地。如果物理很重要，就直接写出来，比如"每个球沿弧线穿过交叉点"（这是我们的建议，不是作者的提示词），这样才会要求动作本身。
- 3D 场景用 Three.js，并写明材质和光照："thick lava swells, splits its dark crust and folds down rock steps in a violet basalt gorge at twilight"（[@teddyaisi][lava]）。

## 3. 把动作写完整，用完整的句子

这组提示词里写得最细的一条，描述的是角色怎么动，而不只是长什么样。作者沿用了早先测试的提示词，要求鹈鹕真的骑车：

> 「Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。」

译文由我们提供："用 Three.js 做一个 3D 场景：一只鹈鹕骑着自行车沿海岸公路前进。它真的在骑车，用两只脚蹬踏板，用翅膀操控车把，车轮随着蹬踏转动。"作者说，同一提示词在早先的模型上得到的结果完全不同（[@Aki_LIG][pelican]）。

## 4. 设定思考强度，并要求一次调用生成整个应用

一位作者在高思考强度下做了一个线粒体马达模拟。模型用一次调用、一条提示词写出了整个应用，形状使用真实的 cryo-EM 坐标，运动做了简化。作者事后只做了一处小的相机修正。这次运行用了 201 秒，约 36 美分（[@SidraMiconi][mito]）。思考强度要有意识地选，并记下来：另一位作者的对比帖提到，那次运行用的是 Extra High，而之前的测试只能跑到 High（[@EnvolDev][rio]）。

## 5. 要一个可以度量的结果

模拟类需求一旦让页面报出数字，就容易比较。一位作者用神经网络加遗传算法进化行走的生物，按代数和最佳距离比较了三个模型。Hydrogen 在 27 代、36 分钟内达到 7.5 米，而 Fable 5.2 是 29 代、1 小时 34 分钟、7.4 米（[@noclipepe][walk]）。这些是作者自己的数字。

## 6. 给场景起个名字，写清地点和终点

带地点和时间的标题能给模型一个清楚的目标。同一位作者的两条提示词就是这样命名场景的："Rio Above the Clouds" 和 "Cathedral of Ice"（[@EnvolDev][rio]、[@EnvolDev][cathedral]）。写清楚最后一帧应该是什么样，结果才能对照检查。第 2 节的熔岩提示词用"溢出每一级台阶"这个画面做到了这一点。

## 7. 运行前先定好预算

同一条提示词，花费和耗时差别很大。Rio 影片这条，一位作者报告 Hydrogen 花费 $6.21，而 Opus 5.5 为 $60.89，Fable 5.2 为 $76.04（[@EnvolDev][rio]）。大教堂场景上，Hydrogen 为 $4.27，Gemini 4 Carbon 为 $8.83，GPT-6.1 Sol 为 $3.11（[@EnvolDev][cathedral]）。`max_tokens` 要给隐藏的推理留出空间（API 示例用的是 128,000），每次运行后检查 `usage`。

## 可以直接用的提示词

```text
把 [主题] 做成一个从磁盘直接打开就能跑的独立 HTML 文件。

画面：[风格，例如 low-poly / 电影感 / 霓虹]，[氛围、光照、配色]。
运动：[什么在动、怎么动，用完整的句子写]。加载后自动播放 [10] 秒的镜头巡游，然后循环。
交互：[拖拽 = …，滚轮 = …，点击 = …，按键 = …]。
物理与规则：[必须成立的条件：数量、速度、碰撞、齿轮比]。

技术：
- 用 CDN 加载库，不需要构建步骤。场景是 3D 的就用 Three.js。
- 不要外部图片、字体、音频：贴图用代码生成，声音用 Web Audio。
- 铺满视口、不出现滚动条、笔记本上 60 fps。
- 完成前自检：页面加载零 console 错误，每个操作都可用。
- 只返回完整的 HTML，从 <!DOCTYPE html> 到 </html>，不要省略。
```

可以到 [Lab 文本竞技场][arena] 里，把这段同时跑在 Gemini 4 Hydrogen 和其他模型上对比；用 API 的方式见[教程](tutorial.md)。

## 参数设置

- **思考强度。** 有作者在一次调用生成应用时用 high（[@SidraMiconi][mito]），在对比中用 Extra High（[@EnvolDev][rio]）。选定强度，并和结果一起记下来。
- **输出预算。** 推理计入 `max_tokens`，并按输出价计费。[教程](tutorial.md)里的 API 示例用的是 128,000。
- **一次生成 vs. 迭代。** 记下你做的是哪一种。有位作者的应用来自一次调用加一次相机修正（[@SidraMiconi][mito]），每多一轮，耗时和花费都会变化。

---

引文均为短摘录并注明作者，完整提示词和视频请点链接。日文原文的翻译为我们所做。

[motor]: https://x.com/analogalok/status/2122221106304352257
[bikes]: https://x.com/marcthecreatorr/status/2120956699951628637
[lion]: https://x.com/SahilPanhotra/status/2120978349967458704
[lava]: https://x.com/teddyaisi/status/2121977175612219870
[pelican]: https://x.com/Aki_LIG/status/2121960943361896596
[mito]: https://x.com/SidraMiconi/status/2121745863827697687
[rio]: https://x.com/EnvolDev/status/2121701704139956250
[walk]: https://x.com/noclipepe/status/2122349082723176738
[cathedral]: https://x.com/EnvolDev/status/2122105333887934810
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-hydrogen&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
