# Gemini 4 Hydrogen 提示词

[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

共 49 条 Gemini 4 Hydrogen 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 Gemini 4 Hydrogen 一键 **复刻**。第一次写 Gemini 4 Hydrogen 提示词？先看 [提示词写法](prompt-guide.md)。

每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。

- [3D 场景](#3d-scene) (12)
- [动效](#motion-graphics) (6)
- [产品界面](#ui-demo) (1)
- [讲解](#explainer) (1)
- [测试对比](#comparison) (29)

<a id="3d-scene"></a>

## 3D 场景

### 日出时分的体素风格中国山地寺庙

[@camperaigg](https://x.com/camperaigg/status/2120938275594756296) · 0:24 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2120938275594756296/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2120938275594756296?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
🚨 Gemini 4 Hydrogen TESTING Part 1

🏔️ I asked Gemini 4 Hydrogen to build a voxel Chinese mountain temple at sunrise.

One prompt, three quick sign-offs. I never touched Blender. 🤯

⏱️ 42 mins
🤖 Gemini 4 Hydrogen High

What it built from scratch 👇

🧱 Generated 399,949 beveled voxels in pure NumPy & Geometry Nodes—a Paifang gate, double-tiered Main Hall, 3-tier pagoda, lantern bridge, 7 snow-laden pines, and a plum blossom tree
🌊 Simulated 14,010 dynamic voxel particles per frame: a 3-tier waterfall, plunge-pool foam, gorge mist, rising incense smoke, and drifting snow
⛰️ Sculpted a V-saddle into the distant Shan Shui peaks so the rising sun breaks cleanly over the ridge at 15.0 seconds—triggering the pagoda's swinging bronze bell
🔍 Caught and fixed its own bevel pinhole light leaks (1.003x cubes + 26-neighbor culling) and a broken ShaderNodeVectorMath link in the sky shader
🎞️ Rendered all 1,440 frames in Blender 4.5 Cycles (OptiX, 16-bit AgX), graded with warm sunrise halation, and verified 0 edit clicks & 0 flash hazards

📦 24 s · 1080p60 · 399,949 voxels/frame · 12 real recordings · 0 edit clicks
```

### Three.js实现的冰晶飘落模拟

[@camperaigg](https://x.com/camperaigg/status/2120979135975809516) · 0:18 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2120979135975809516/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2120979135975809516?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
🚨 Gemini 4 Hydrogen TESTING Part 2

❄️ I asked Gemini 4 Hydrogen to make an ice crystal falling in pure Three.js.

One shot, 18 seconds, zero external models or textures. 🤯

⏱️ 13 minutes (including 1080p60 GPU renders)
💸 $4.64 in API costs
🤖 Gemini 4 Hydrogen Xhigh

What it engineered from scratch 👇

💎 Built a procedural 8,448-triangle 3D stellar dendrite with terraced hexagonal plates, 60° side branches, and internal 3D micro-bubbles
🌈 Wrote a custom GLSL ice shader with two-pass RGB chromatic dispersion (IOR 1.31), backlit subsurface scatter, and 96-tap optical DOF
🌨️ Drove 4,900 snowflakes and an 80,000-triangle forest floor from a single time-dilation clock (1.0× → 0.024× slow-mo → 1.0×)
🪨 Ground starts as dark wet basalt & 520 pine needles, then visibly swells under diamond-sparkling snowdrifts as the crystal lands
🔍 Caught & fixed Fibonacci DOF stippling on bokeh orbs, square-grid noise seams in clouds, and a NaN bug in its audio ducking bus

📦 18 s · 1080p60 · 8,448-tri dendrite · 4,900 snowflakes · 0 edit clicks
```

### 鹈鹕骑自行车的3D动画场景

[@Shohank9n1](https://x.com/Shohank9n1/status/2121089280583901375) · 0:29 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121089280583901375/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121089280583901375?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen (Xhigh)

Prompt: A 3D animated scene of a pelican riding a bicycle.

In my opinion, the Hydrogen model still needs significant improvements, especially in animation realism, movement, and overall output quality.
```

### 三维双缝干涉量子物理实验模拟

[@analogalok](https://x.com/analogalok/status/2121163760081440784) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121163760081440784/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121163760081440784?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
just one shotted a hyper realistic 3D double slit quantum physics lab in a single HTML file using Gemini 4 Hydrogen.

real Fresnel diffraction math, single photon mode, even a motorized which way detector that collapses the interference pattern in real time.

honestly makes me sick how jealous i am of kids in school right now. having this at home for $0 would’ve easily added 15-20 IQ points to my brain.

we used to stare at static 2D diagrams in dusty textbooks and pretend we understood wave particle duality lol

check out the prompt in the replies and build your own.
```

### 使用群集模式的Three.js动画测试

[@DanjiTosaka](https://x.com/DanjiTosaka/status/2121330663106474327) · 0:31 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121330663106474327/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121330663106474327?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Testing Scott idea with Gemini 4 Hydrogen swarm mode + Three.js✨ 

I'm sharing the prompt here 👇
```

### Three.js交互式3D工业机械臂

[@HarshithLucky3](https://x.com/HarshithLucky3/status/2121590376544997507) · 0:55 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121590376544997507/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121590376544997507?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Industrial Robot Arm ("KRYPTON")

single-file HTML + Three.js, zero external 3D models

Gemini 4 Krypton in Arena (under "gemini-4-hydrogen")

> interactive 3D industrial robot arm named "KRYPTON"
```

### 使用Gemini 4创建的线粒体电机模拟

[@SidraMiconi](https://x.com/SidraMiconi/status/2121745863827697687) · 0:26 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121745863827697687/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121745863827697687?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen lets you pull apart the motor in your mitochondria.
You drive its ring: 8 protons and 3 ATP per full turn.

At thinking level "high", it wrote the whole app in one call from one prompt, and I made one small camera fix afterwards.
One prompt. 201 seconds. About 36 cents.
The shape comes from real cryo-EM coordinates; the motion is simplified.
@DemisHassabis @SundarPichai
```

### Three.js中沿海骑自行车的鹈鹕3D场景

[@Aki_LIG](https://x.com/Aki_LIG/status/2121960943361896596) · 2:48 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121960943361896596/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121960943361896596?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogenやばいんですけど。。
ペリカンテストでこんなの見たことない。

プロンプトは、以前6.1 Terraに与えたのと全く同じ。
出力がまるで違います。

プロンプト👇
「Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。 ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。動作は自然で滑らか。 シーンは生き生きとして詳細豊かで、自然環境、動的効果、光影、インタラクティブ機能を備える。 あなたの3Dモデリング、アニメーション、ビジュアルデザインの能力を最大限に発揮して、洗練された、すぐに実行可能なウェブ作品を完成させて。」
```

### 使用视频Minimax模型制作的可爱角色动画

[@nyapan_mohy](https://x.com/nyapan_mohy/status/2122253350808744004) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-argon/2122253350808744004/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122253350808744004?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Cute版 サムネで既にかわいい

なお、全部 「Gemini 4 Hydrogen」がやりました！！！
なにがって、わたしが「こんなことやりたい！」以外全てです。ええ、全て。

プロンプトはリプ

Cool版と完全に同じ背景・衣装ルールを保ったまま、ウィンク・猫口（:3）・頬ぷく・星目・全力ジャンプなど、設定画に載っていない可愛い表情＆アクションの振り幅を 16:9 開始フレーム＋30ショットプロンプトで引き出しています。

▼ 技術構成（Cute版）
・Pipeline: ComfyUI video_minimax_h3_i2v (fl2va + 8step Turbo LoRA)
・Quantization: Diffusion int8_convrot / TE nvfp4_awq
・Spec: 1344×768 (768p 16:9) / 24fps / 15.08s / ネイティブ音声付き
・Seed / Time: 420002 / A100 80GB で 14m32s
・工夫点: 設定画のクール表情に引っ張られないよう、先にウィンク＆ロックポーズの Cute 用 16:9 開始フレームを作って I2V 投入
```

### 纯代码生成的TP-7交互录音机

[@FiniYang](https://x.com/FiniYang/status/2122255731411849691) · 0:14 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2122255731411849691/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122255731411849691?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
🔥 Gemini 4 Hydrogen 一句话搓出 TP-7 掌上录音机！（🔊 开声音）
现在是真的喜欢 Cargon 和 Hydrogen 😍

全程零模型、零贴图，纯代码单轮盲测直出
结果连底下的工程刻度垫和橙色螺旋音频线都是它自己加的戏 😂

正中间的金属转盘放着合成器 Lo-Fi 自己会转
鼠标按住直接物理刹停，正反拨动就能搓碟变调，橙色实体键按下去还有清脆咔哒声

Prompt 放评论区了 ⬇️
#Gemini4Hydrogen #Threejs #WebGL #VibeCoding
```

### Three.js交互式3D直流电机

[@analogalok](https://x.com/analogalok/status/2122608311912780243) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2122608311912780243/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122608311912780243?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
bro Gemini 4 Hydrogen (xHigh) is cracked

63 input tokens -> 57,222 output tokens

Gemini 4 Hydrogen just one shotted a full interactive 3D DC motor in Three.js and the physics are actually insane:

- Curved N -> S magnetic field lines + flux pulses
- Gold conventional current arrows (I) going the opposite way
- Real time Lorentz force vectors (F = I·L × B)
- Split ring commutator sparks when breaking contact
- Live oscilloscope plotting Torque, Current & Back EMF

Watch the green force arrows and blue wire rings the exact second the commutator hits the 90° gap.

Prompt: create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn

For comparison with High reasoning, checkout the quoted post.
```

### Three.js科幻机甲组装发射动画

[@alohaproxy](https://x.com/alohaproxy/status/2122609183837049037) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2122609183837049037/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122609183837049037?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen is actually INSANE!!!!!!

I gave it a massive Three.js challenge: build a cinematic sci-fi mech that assembles itself piece by piece, powers up its reactor, and launches into the sky with plasma thrusters, shockwaves, and explosions.

It generated the entire thing in under 5 minutes.

Built with @AiHubMix 

Here's what it cooked, details/prompt below💀👇
```

<a id="motion-graphics"></a>

## 动效

### 鹈鹕骑自行车的SVG动画

[@DrstaOne](https://x.com/DrstaOne/status/2120937028015833193) · 0:31 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2120937028015833193/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2120937028015833193?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen First SVG: 

<<Pelican riding bicycle>>
```

### 从太空连续缩放至自由女神像的动画

[@analogalok](https://x.com/analogalok/status/2120970144885456948) · 0:29 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2120970144885456948/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2120970144885456948?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen is crazy!!! 

Check out this one shot animation. 

Prompt: 

Create a very realistic high quality earth as seen from the space. camea should auto zoom in to the statue of liberty. Make sure the entire zoom is smooth, the earth, clouds, city and the statue is highly detailed and realistic. single html file. use any libs via cdn.

Check out the video in replies for Gemini 4 hydrogen vs Gemini 3.8 flash comparison
```

### 边牧制作手冲咖啡的SVG动画

[@Sin_Yiyao](https://x.com/Sin_Yiyao/status/2121030290369827023) · 0:24 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121030290369827023/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121030290369827023?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen  全程7分钟
帮我做一个 SVG 动画：拟人化的边牧从磨咖啡到手冲咖啡的动画。要精美细腻有特色，
打败了gpt 6.1 sol( 疑似6.2灰度，知道fable)
为啥写这个测试，
- 边牧造型的嘴筒子非常不容易显，特征也容易画错。
- 手的关节动作比骑自行车复杂，并且有大量物品交互
- 需要考虑正确的物品遮挡
```

### 鹈鹕骑自行车的SVG动画测试

[@qingzhoucloud](https://x.com/qingzhoucloud/status/2121068143502397863) · 0:14 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121068143502397863/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121068143502397863?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
不正常的一次Gemini 4 Hydrogen 的鹈鹕测试

我想了半天找到了原因，主要是我在提示词后面加了一句：【尽你最大的能力】就导致不好看了，原本是想要更出色一些，实际上颜色和鹈鹕也不好看了，动作有些变形，可理解为ai过度发力导致.....

提示词：提示词：创建一个 HTML，内容是 SVG 绘制一个鹈鹕骑自行车的 2D 动画，你不需要任何测试，不要有任何限制，【尽你最大的能力】
```

### AI音乐视频Bloom in Color

[@DavidLi36143625](https://x.com/DavidLi36143625/status/2121972204665770012) · 0:57 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121972204665770012/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121972204665770012?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Today's Sharing

Bloom in Color

New Music Video made with @Grok @Imagine

Image: Grok Imagine Image 2.0 (via AI SDK)
Video: Grok Imagine Video 1.5 Lite (via AI SDK)
Scene/Prompt Design: Gemini 4 Hydrogen
Music: Suno
Pipeline Coding: DeepSeek

Each model does one part of the pipeline.
See the full prompt set used in the reply section below.
```

### Little Ember Wings AI音乐视频

[@DavidLi36143625](https://x.com/DavidLi36143625/status/2125918679196107086) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2125918679196107086/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2125918679196107086?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Today's Sharing

Little Ember Wings

New Music Video made with @Grok @Imagine

Story/Prompt Design: Gemini 4 Hydrogen
Image/Video: Grok Imagine (Agent Mode)
Music: Suno

See the full prompt set used in the reply section below.
```

<a id="ui-demo"></a>

## 产品界面

### 使用React生成的健身应用落地页

[@J70427237](https://x.com/J70427237/status/2125547117490102599) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2125547117490102599/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2125547117490102599?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
I generated a landing page for a gym app using Antigravity with its default Gemini 4 Hydrogen model.

Here's the prompt I used:

"Build a landing page for a gym app with React Expo Go."

Here's what I got.

Honestly, I think it looks a little bloated. What do you guys think?
```

<a id="explainer"></a>

## 讲解

### 将枯燥课本转为生动教学视频

[@smalkalbani](https://x.com/smalkalbani/status/2121844887033458954) · 0:20 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121844887033458954/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121844887033458954?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
حول درس إبنك الجامد إلى فيديو مثير للتعلم

استخدمت Gemini 4 hydrogen

الـ Prompt 👇
```

<a id="comparison"></a>

## 测试对比

### 吉卜力风格双人骑行 SVG 生成对比

[@marcthecreatorr](https://x.com/marcthecreatorr/status/2120956699951628637) · 0:28 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2120956699951628637/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2120956699951628637?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen vs Opus 5.5 (Tandem Ride SVG)

same prompt: create an SVG of a girl and her cat on joined bikes, golden hour, ghibli style

• opus 5.5 in claude code:  ~1 hr, ~$18 api cost
• gemini 4 hydrogen in cursor: ~15 mins, ~$0.9 api cost

opus took its time with the detailing (night mode, music) while hydrogen got the whole scene done faster for less than a dollar. 

which model did it better?
```

### 单页面精美创意网页生成对比

[@SaiNemani1](https://x.com/SaiNemani1/status/2120960537639182703) · 1:04 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2120960537639182703/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2120960537639182703?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen is a BIG UPGRADE to Gemini 3.8 Flash in terms of intelligence, and speed!

Left: Gemini 4 Hydrogen HIGH
Right: Gemini 3.8 Flash HIGH

Prompt: "Make a single code page beautiful and creative website."
```

### 狮子骑车抛球杂耍交互式SVG对比

[@SahilPanhotra](https://x.com/SahilPanhotra/status/2120978349967458704) · 0:48 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2120978349967458704/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2120978349967458704?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
GEMINI 4 HYDROGEN VS GEMINI 4 CARBON

same interactive svg prompt: lion biking, juggling across 4 seasons + web audio sfx.

Carbon (bottom) actually nailed the crossing juggling arcs and even added winter breath puffs. 

Hydrogen (top) straight up faked the juggling by floating the balls in place though its season wipes and container clipping are way cleaner.

Carbon for raw detail & physics. Hydrogen for fast UI logic.
```

### 多模型生成可摇晃交互式雪花球对比

[@PokeBenchTV](https://x.com/PokeBenchTV/status/2121108468484460948) · 0:58 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121108468484460948/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121108468484460948?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
I gave Gemini 4 Hydrogen the same prompt as the others. Build a snow globe you can shake.

It finished so fast I could prompt it a few more times to improve it and still be done before the others.

Sol and Opus both built a lighthouse. I didn't tell them what to put inside.

Which one are you keeping on your desk?
```

### 四款 Gemini 模型制作 3D 攻城游戏对比

[@StatsWire](https://x.com/StatsWire/status/2121226579141386285) · 0:45 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121226579141386285/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121226579141386285?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Same prompt. 4 Gemini models. One challenge.

Build a playable 3D Medieval Trebuchet Castle Siege with 300–600+ rigid-body stone blocks.

Here are the results:

Gemini 3.8 Flash (High)
4m 16s | 43.4K output tokens | 2,061 LOC

Gemini 4 Argon (High)
14m 27s | 45.9K output tokens | 2,149 LOC

Gemini 4 Carbon (High)
23m 33s | 83.6K output tokens | 3,049 LOC

Gemini 4 Hydrogen (Extra High)
10m 03s | 76.3K output tokens | 2,780 LOC

Flash was the fastest. Carbon generated the most code. Hydrogen finished in less than half Carbon's time.
```

### 多风格定格小猫奔跑跨模型对比

[@TypingMindApp](https://x.com/TypingMindApp/status/2121228272495419480) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-argon/2121228272495419480/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121228272495419480?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen just dropped...

So we gave it, GPT-6.1 Sol, Claude Sonnet 5.5 and Claude Opus 5.5 the same prompt: stop motion of a cat running in place, every frame drawn in a different art style 🐈

Opus 5.5 is still the best here, but Hydrogen comes surprisingly close for only $0.9.
```

### 火柴人对战光标模型生成效果对比

[@DanielZambrini](https://x.com/DanielZambrini/status/2121289822677483740) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121289822677483740/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121289822677483740?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini Hydrogen 4 vs Fable 5.2 - Stickman Vs Cursor

The objective here is just to show that while being a smaller model, Hydrogen can still produce a fairly good result.

Fable is obviously better, but if I were in a hurry and wanted to save cash, I would still be fine with Hydrogen

Prompt in the first comment
```

### 东京夜景生成模型的性能对比

[@sprinntt](https://x.com/sprinntt/status/2121378834687610966) · 0:19 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121378834687610966/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121378834687610966?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Night Tokyo 04, one prompt, four labs

- Claude Fable 5.2 (medium): $7.11 - 20 min
- GPT-6 Astra (xhigh): $2.11 - 13 min
- Gemini 4 Hydrogen (xhigh): $2.25 - 20 min
- Gemini Orchestrator (Argon + Hydrogen): $1.29 - 14 min

Astra looks plain here but has the most detail up close

Which one would you keep?
```

### 四款AI模型云端视频生成对比

[@EnvolDev](https://x.com/EnvolDev/status/2121701704139956250) · 0:25 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2121701704139956250/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121701704139956250?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Fable 5.2 vs Gemini 4 Hydrogen vs Opus 5.5 vs GPT-6 Astra ☁️

Gemini 4 Hydrogen made the whole film for $6.21. 🤯
But it's the least good of all. 😬

Same prompt: Rio Above the Clouds
Opus 5.5: $60.89 · 2h 19m 35s
Fable 5.2: $76.04 · 1h 59m 11s
Gemini 4 Hydrogen: $6.21 · 1h 33m 48s
GPT-6 Astra: $16.89 · 34m 06s

And this time it ran on Extra High. In my last test, it could only run on High. So no excuses.

I know I can't compare it to frontier models like Fable 5.2 or Opus 5.5.
But the result was not good at all.

GPT-6 Astra cost only $10.68 more, finished almost 1 hour faster, and made a better film.

I'm not impressed at all by Hydrogen on this one. 🤦

What do you guys think? 👀
```

### 多款 Gemini 模型的 Three.js 熔岩效果对比

[@teddyaisi](https://x.com/teddyaisi/status/2121977175612219870) · 0:20 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2121977175612219870/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2121977175612219870?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Carbon vs Gemini 4 Argon vs Gemini 4 Hydrogen

The Three.js task: thick lava swells, splits its dark crust and folds down rock steps in a violet basalt gorge at twilight. 

Which version best conveys the lava’s weight as it bulges and spills over each ledge? 👇
```

### 三种AI模型在地球可视化上的表现对比

[@Dain0x](https://x.com/Dain0x/status/2122075114883690862) · 0:43 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-argon/2122075114883690862/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122075114883690862?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
3 AI MODELS. ONE EARTH. ONE PROMPT
THE DIFFERENCE IS HARD TO IGNORE.

The creator says all three received the same prompt.

→ Top: Gemini 4 Hydrogen
→ Middle: GPT-6.2 Sol
→ Bottom: Claude Fable 5.2

Watch the globe, then watch the details:
the lighting, the camera, the way the interface holds together as the view changes.

For me, Fable wins this visual comparison.
The depth and lighting make the whole scene feel more convincing.

One example doesn’t settle which model is best.
But it does make a good blind test:

Hide the names. Which one would you pick?
```

### 四种AI模型在大教堂提示词下的表现对比

[@EnvolDev](https://x.com/EnvolDev/status/2122105333887934810) · 0:25 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122105333887934810/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122105333887934810?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen vs Gemini 4 Carbon vs GPT-6.1 Sol vs Muse Spark 1.3 🧊

Google vs OpenAI vs Meta. One prompt. 🤯

Same prompt: Cathedral of Ice
Gemini 4 Hydrogen: $4.27 · 1h 23m 40s
Gemini 4 Carbon: $8.83 · 2h 39m 10s
GPT-6.1 Sol: $3.11 · 54m 19s
Muse Spark 1.3: $5.56 · 2h

GPT-6.1 Sol was the cheapest and the fastest of all four. 😱

Almost 3x cheaper and almost 3x faster than Gemini 4 Carbon.

Which one would you pick? 👀
```

### 用于电机模拟的AI模型对比

[@analogalok](https://x.com/analogalok/status/2122221106304352257) · 0:13 · [观看](https://www.sandbase.ai/lab/media/x/qwen4-max/2122221106304352257/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122221106304352257?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Qwen 4 Max Vs Qwen 3.8 Max Vs Gemini 4 Hydrogen

Prompt:
create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn

Gemini 4 Hydrogen did the best overall job on 3D realism and visual clarity, modeling a proper curved horseshoe magnet, detailed commutator, and phase by phase physics explanations without visual clutter. 

Qwen 4 Max offered the richest lab dashboard, adding a physical DC battery, live waveform graph, and friction controls though its dense glowing overlays crowded the center. Qwen 3.8 Max had the simplest 3D scene but stood out for its helpful synchronized 2D schematic view.
```

### 各模型构建Minecraft网页版的性能对比

[@x_Kuro_](https://x.com/x_Kuro_/status/2122345434567905500) · 0:16 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2122345434567905500/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122345434567905500?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Qwen4-Max vs Gemini 4 Hydrogen vs Claude Fable 5.2

same prompt: build Minecraft in a single HTML file. one shot, no edits

Claude and Gemini nailed it. Qwen's whole world rendered black 💀

turns out it was one line. it read its own textures upside down. one fix and its world was actually the prettiest

which one would you trust with your game?
```

### 测试三种AI模型在行走模拟中的表现

[@noclipepe](https://x.com/noclipepe/status/2122349082723176738) · 0:58 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2122349082723176738/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122349082723176738?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
I forced Fable 5.2, Qwen 4 Max and Gemini 4 Hydrogen to learn how to walk

Same prompt. Real neural networks + genetic algorithm.

Gemini beat Fable by 10 cm. On its knees.
Fable is the only one that actually walks.

Fable 5.2
· 29 generations
· best: 7.4 m
· 1h 34m to build

Gemini 4 Hydrogen
· 27 generations
· best: 7.5 m
· 36m 43s to build

Qwen 4 Max
· 32 generations
· best: 6.1 m
· 1h 6m to build
```

### 对比四种AI模型制作动画SVG的表现

[@RezAIT00](https://x.com/RezAIT00/status/2122353119749361808) · 0:18 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2122353119749361808/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122353119749361808?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Qwen 4 Max vs Fable 5.2 vs GPT Astra vs Gemini 4 Hydrogen

Same prompt: an animated SVG of a pelican riding a zebra riding a horse

One took 6 minutes. One took 34.

Can you guess which model made which?

Answers will be revealed ~2 hours :)
```

### 冰之大教堂生成模型的性能对比

[@realdrovex](https://x.com/realdrovex/status/2122424452885717358) · 0:25 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122424452885717358/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122424452885717358?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen vs Gemini 4 Carbon vs GPT-6.1 Sol vs Muse Spark 1.3 🧊

Google vs OpenAI vs Meta. One prompt. 🤯

Same prompt: Cathedral of Ice
Gemini 4 Hydrogen: $4.27 · 1h 23m 40s
Gemini 4 Carbon: $8.83 · 2h 39m 10s
GPT-6.1 Sol: $3.11 · 54m 19s
Muse Spark 1.3: $5.56 · 2h

GPT-6.1 Sol was the cheapest and the fastest of all four. 😱

Almost 3x cheaper and almost 3x faster than Gemini 4 Carbon.

Which one would you pick? 👀
```

### 四款AI模型生成奔马踏水效果对比

[@SamgreyAi](https://x.com/SamgreyAi/status/2122440859891409372) · 0:12 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122440859891409372/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122440859891409372?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen just built a horse out of Minecraft blocks and called it a day 

Same prompt, 4 AI workflows: a horse galloping through water.

Same horse, same lake, but the gap between the results is brutal 

The horse racing department is cooked

🥇 Fable 5.2 → low-poly horse in a low-poly world, huge water splashes and a gallop that actually looks heavy

🥈 Gemini 4 Carbon → warm sunset canyon, smooth horse and a very cinematic look

🥉 GPT-6 Astra → beautiful mountains and forest, but a low-poly horse inside a realistic world

💀 Gemini 4 Hydrogen → somehow a black voxel horse that looks like it escaped from Minecraft

The interesting part isn’t the horse

It’s how the legs, the splashes and the reflections work together

Pretty lighting can’t save you if the water doesn’t react to every hoof

Fable made the whole scene feel like one world, while Astra’s horse and background look like they belong to different games

At this point AI doesn’t need better horses

It needs to learn how water works 

Which horse would you pick?
```

### 四款模型生成Three.js座头鲸跃出海面

[@teddyaisi](https://x.com/teddyaisi/status/2122544449968373997) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-carbon/2122544449968373997/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122544449968373997?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Claude Fable 5.2 vs Gemini 4 Carbon vs GPT-6-Astra vs Gemini 4 Hydrogen

Same prompt. Build a 20-second Three.js humpback whale breach off Icelandic basalt stacks, from bursting out of the swell and rolling mid-air to a broadside slam and final tail lift.

Claude Fable 5.2 (Top left): $19.07 · 71m29s · xhigh
Gemini 4 Carbon (Top right): $13.11 · 163m18s · high
GPT-6-Astra (Bottom left): $11.10 · 72m45s · xhigh
Gemini 4 Hydrogen (Bottom right): $4.27 · 37m27s · xhigh

Fable 5.2 runs 4.5x Hydrogen's API spend for better lighting and a cleaner final beat. 

Which one would you actually pay for?👇
```

### 四款模型生成单缸发动机剖面运转对比

[@kinderlayer](https://x.com/kinderlayer/status/2122651038029086720) · 0:12 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2122651038029086720/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122651038029086720?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
ok this is getting out of hand - four models built the same engine, and one of them costs way more to run than the rest.

same prompt, four models, a single-cylinder engine firing in cross-section. fuel flowing, piston driving, cams spinning.

Claude Fable 5.2 · GPT-6 Astra · Gemini 4 Argon · Gemini 4 Hydrogen

one packed it with detail and fuel spray. one went clean and industrial. one got busy with twin gears up top. one stripped it leaner and sharper.

the catch: the fancier the model, the more it burns to run. I didn’t touch a frame and I’m not telling you which one costs the most - you call it: which engine looks like the one actually worth paying for?

drop your pick
```

### 大鹏展翅Three.js三维动画生成对比

[@vincent_ddup](https://x.com/vincent_ddup/status/2122941884192407650) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2122941884192407650/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2122941884192407650?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
同一个模型为什么差异会这么大？GPT 6.2 到底是什么样的一种存在？

早上做了一版鹕骑自行车海滨浴场版本。
我有一个非常详细的提示词，给到 6.2 Sol 做了一版之后，再稍微调整了一版细节，两版出来的效果就在上一篇帖子发布的录屏。
我觉得非常的惊艳！！！

但是刚刚我用一个同样的很简洁的提示词，让它做一个大鹏展翅的 3D 动画，结果就做成这个样子。
1. 第一版本是用 GPT 6.2 Astra 做的。
2. 第二个版本是用 Gemini 4 Hydrogen 做的。

提示词如下：

给我用 three.js 设计一个大鹏展翅的 3D 动画。并适配手机版本。
```

### 四款模型生成的孔雀舞动画对比

[@CodeByPoonam](https://x.com/CodeByPoonam/status/2123028120483901925) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2123028120483901925/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2123028120483901925?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
$20 CLAUDE OPUS 5.5 VS FREE HY4 FLASH ON MY PEACOCK DANCE TEST

Same prompt. Same settings. One shot.

· Tencent Hy4 flash (WorkBuddy):  free
· Gemini 4 Hydrogen: $1.50/mo
· GPT-6 Astra: $20/mo
· Claude Opus 5.5: $20/mo

Pick your winner.. Full Breakdown with Prompt👇
```

### 三款模型生成电动机原理动画对比

[@isagi1000x](https://x.com/isagi1000x/status/2123166994426220812) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2123166994426220812/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2123166994426220812?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Qwen 4 Max vs Qwen 3.8 Max vs Gemini 4 Hydrogen. 

I gave all three models the exact same prompt:

Prompt:
"Create a very realistic animation showing how an electric motor works. Clearly visualize everything, including magnetic fields, electrons, and the internal components. Deliver it as a single HTML file using any libraries via CDN."

Here's how they compared:

 Gemini 4 Hydrogen — Best Overall

It delivered the strongest combination of 3D realism and visual clarity. A properly curved horseshoe magnet, detailed commutator, and phase-by-phase physics explanations, all without overwhelming the scene with visual clutter.

 Qwen 4 Max — Best Interactive Dashboard

It went all out on the lab experience, adding a physical DC battery, live waveform graph, and friction controls. However, the glowing overlays made the center of the animation feel a little crowded.

 Qwen 3.8 Max — Best Learning Companion

It had the simplest 3D environment, but made up for it with a helpful synchronized 2D schematic that made understanding the motor's operation easier.

My verdict:

- Best 3D realism and clarity: Gemini 4 Hydrogen.
- Richest interactive experience: Qwen 4 Max.
- Best supporting educational view: Qwen 3.8 Max.

Three models. One prompt. Three very different approaches to explaining the same physics.

Which result would you pick?
```

### 雨夜城市街道网页生成效果对比

[@aapakari](https://x.com/aapakari/status/2124623671562273248) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2124623671562273248/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2124623671562273248?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
One prompt, two models: "a rainy city street at night", as one web page.

Gemini 4 Hydrogen (high): 1 min 48 s, $0.20
Grok 4.7 (high): 20 min 14 s, $0.72

Hydrogen was 11x faster at under a third of the price.

Which one would you ship?
```

### 港口摩天轮动画性能表现对比

[@aapakari](https://x.com/aapakari/status/2125196960399303126) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2125196960399303126/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2125196960399303126?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
One prompt: animate a harbor Ferris wheel at night with fireworks and reflections.

Gemini 4 Hydrogen (Antigravity, high) · 1m 29s · $0.17
NEW HungerG stealth model (OpenCode, default) · 2m 25s · currently free

Hydrogen ran 1.6x faster with brighter reflections; HungerG used 6.5x more reasoning tokens. Which wins?
```

### 鱼群穿梭的珊瑚礁网页生成对比

[@aapakari](https://x.com/aapakari/status/2125560102988186051) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2125560102988186051/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2125560102988186051?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
One prompt, two models: "a coral reef with schools of fish", as one web page.

Gemini 4 Hydrogen (high): 1 min 20 s, $0.17
LongCat 2.5 (default setting): 5 min 43 s, $0.036

Hydrogen finished 4 minutes sooner for 13 cents more.

Which one would you ship?
```

### 暴风雨中旋转灯塔的SVG动画对比

[@sergeo_n](https://x.com/sergeo_n/status/2125606026011365475) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2125606026011365475/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2125606026011365475?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen vs Gemini 4 Neon

Same prompt, pure code, no video generation

An animated SVG of a lighthouse in a storm, waves moving, light rotating.

Top: Hydrogen
Bottom: Neon

> Both took 10 minutes.
> Hydrogen cost $1.57 to run.
> Neon cost $1.64 to run.

7 cents and zero minutes between them.
So the only difference is on screen.

Watch both loops and tell me: where did Neon's extra 7 cents go, because I cannot see it.
```

### 松树林营火网页双模型对比

[@aapakari](https://x.com/aapakari/status/2125914972915900424) · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2125914972915900424/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2125914972915900424?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
One prompt, two models: "a campfire in a pine forest at night", as one web page.

Gemini 4 Hydrogen (high): 1 min 21 s, $0.17
MiniMax M3.1 Flash (default setting): 1 min 01 s, $0.014

MiniMax was faster and over 12x cheaper.

Which one would you ship?
```

### Three.js海洋悬索桥模型对比

[@sergeo_n](https://x.com/sergeo_n/status/2125963571548828025) · [观看](https://www.sandbase.ai/lab/media/x/gemini-4-hydrogen/2125963571548828025/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen/2125963571548828025?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen&utm_content=prompt-index)

```text
Gemini 4 Hydrogen vs Gemini 4 Neon, round 2

Same prompt, Three.js only, no skills:
a cinematic 3D suspension bridge over an ocean strait,
30 seconds, sunset into night, live traffic, moving water.

Top: Neon, 13 minutes
Bottom: Hydrogen, 11 minutes

Hydrogen was faster.
And its water actually looks and moves like water.
Could it be the harnes?

Round 1 was a 7 cent draw.
Round 2 is not close.

Watch the ocean in both, then tell me: is Neon losing its edge, or did Hydrogen just get lucky with this prompt?
```
