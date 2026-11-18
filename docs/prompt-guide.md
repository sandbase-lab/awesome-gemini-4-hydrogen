# Gemini 4 Hydrogen prompt guide: how to prompt Gemini 4 Hydrogen for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

Gemini 4 Hydrogen doesn't output video. It writes code: a self-contained HTML page with Three.js or SVG animation, or a single SVG file. The creator records that output playing. The patterns below come from the prompts creators posted with their videos, and each one links to the post it came from. The collection is young, so this guide has seven patterns and grows as more prompts are shared.

## 1. Ask for one file, and say how libraries load

Name the deliverable and the loading rule in the first lines. The motor-animation prompt did exactly that:

- "create a very realistic animation of how an electric motor works showing everything clearly even the magnetic field, electrons etc. single html file. use any libs via cdn" ([@analogalok][motor]). The creator wrote that Hydrogen "did the best overall job on 3D realism and visual clarity", with a curved horseshoe magnet and a detailed commutator.

A single HTML file with CDN libraries is the format most of the prompts here use, and it records without a build step.

## 2. Name the renderer, and say what has to physically happen

The renderer decides how the page looks and what can break. Naming it, and stating the physical behavior you want, makes the result easier to check:

- SVG for a scene with no JavaScript: "create an SVG of a girl and her cat on joined bikes, golden hour, ghibli style" ([@marcthecreatorr][bikes]). The creator reported about 15 minutes and about $0.9 of API cost, in Cursor.
- Interactive SVG with sound: a lion biking and juggling across four seasons, with web audio effects ([@SahilPanhotra][lion]). The creator found the juggling was faked, with the balls floating in place. A line such as "each ball follows an arc through the crossing" (our suggestion, not the creator's prompt) asks for the motion directly.
- Three.js for a 3D scene, with the material and light you want: "thick lava swells, splits its dark crust and folds down rock steps in a violet basalt gorge at twilight" ([@teddyaisi][lava]).

## 3. Spell out the motion, in full sentences

The most detailed prompt in the set describes how a character should move, not only what it looks like. The creator reused it from an earlier test, and it asks for a pelican that actually rides:

> 「Three.jsを使って3Dシーンを作成：ペリカンが自転車に乗って海岸沿いの道路を進む。ペリカンが本当に自転車に乗って、両足でペダルを漕ぎ、翼でハンドルを操り、車輪が漕ぐのに合わせて回転する。」

Translation by us: "Create a 3D scene with Three.js: a pelican rides a bicycle along a coastal road. It really rides the bicycle, pedaling with both feet, steering the handlebars with its wings, with the wheels turning as it pedals." The creator said the output looked completely different from what the earlier model gave for the same prompt ([@Aki_LIG][pelican]).

## 4. Set the thinking level, and ask for the whole app in one call

One creator built a mitochondrial motor simulation at a high thinking level. The model wrote the whole app in one call from one prompt, using real cryo-EM coordinates for the shape and simplified motion. The creator made one small camera fix afterwards. The run took 201 seconds and about 36 cents ([@SidraMiconi][mito]). Choose the level on purpose, and record it: another creator's comparison notes that the run used Extra High, and that an earlier run could only go as high as High ([@EnvolDev][rio]).

## 5. Ask for something you can measure

Simulation briefs are easy to compare when the page reports a number. A creator who evolved walking creatures with a neural network and a genetic algorithm compared three models by generation count and best distance. Hydrogen reached 7.5 m in 27 generations and 36 minutes, against 7.4 m in 29 generations and 1h 34m for Fable 5.2 ([@noclipepe][walk]). These are the creator's figures.

## 6. Give the scene a name, a place and a finish

A title with a place and a time gives the model a clear target. Two prompts from the same creator name their scenes this way: "Rio Above the Clouds" and "Cathedral of Ice" ([@EnvolDev][rio], [@EnvolDev][cathedral]). Say what the last frame should show, so the result can be checked against it. The lava prompt in §2 does this with its "spills over each ledge" image.

## 7. Decide your budget before you run it

Cost and time varied widely on the same prompt. For the Rio film, one creator reported $6.21 for Hydrogen, against $60.89 for Opus 5.5 and $76.04 for Fable 5.2 ([@EnvolDev][rio]). For the cathedral scene, Hydrogen came in at $4.27, against $8.83 for Gemini 4 Carbon and $3.11 for GPT-6.1 Sol ([@EnvolDev][cathedral]). Leave room in `max_tokens` for hidden reasoning (the API example asks for 128,000), and check `usage` after each run.

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file that opens directly from disk.

Look: [style, e.g. low-poly / cinematic / neon], [mood, lighting, palette].
Motion: [what moves and how, in full sentences]. Autoplay a [10]-second camera tour on load, then loop.
Interaction: [drag = …, scroll = …, click = …, keys = …].
Physics and rules: [what must be true: counts, speeds, collisions, gear ratios].

Technical:
- Load libraries from a CDN with no build step. Use Three.js if the scene is 3D.
- No external images, fonts or audio: generate textures in code, sound with Web Audio.
- Fill the viewport, no scrolling, 60 fps on a laptop.
- Before you finish, check that the page loads with zero console errors and that every control works.
- Return only the complete HTML, from <!DOCTYPE html> to </html>. Do not abbreviate.
```

Try it on the [Lab text arena][arena] to run it on Gemini 4 Hydrogen and other models side by side, or with the API in the [tutorial](tutorial.md).

## Settings

- **Thinking level.** Creators used high for a one-call app ([@SidraMiconi][mito]) and Extra High for a comparison ([@EnvolDev][rio]). Pick the level, and note it with the result.
- **Output budget.** Reasoning counts against `max_tokens` and bills at the output rate. The API example in the [tutorial](tutorial.md) uses 128,000.
- **One shot vs. iteration.** Note which you did. One creator's app came from one call plus one camera fix ([@SidraMiconi][mito]), and the cost and time change with each extra turn.

---

Quotes are short excerpts credited to their authors; follow the links for full prompts and videos. Translations from Japanese are ours.

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
