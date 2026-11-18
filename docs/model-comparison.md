# Gemini 4 Hydrogen vs Claude Opus 5.5, Fable 5.2, Gemini 4 Carbon and others

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result. Small samples, but the same conditions for everyone.
2. **What creators reported.** Same-prompt runs posted on X, with their own prompts, costs and times. Useful context, not verified by us.

Gemini 4 Hydrogen was announced on November 12, 2026. The list below is built from the launch data, and no measured row for the model existed in it when the list shipped. The creator side is large because the model was new and people ran the same prompts against it.

## What we measured: Lab Evals boards and Pelican Test

**There is no Gemini 4 Hydrogen row on the Lab Evals boards or the Pelican Test leaderboard in the data this list was built from.** Until one exists, nothing measured on this page places Gemini 4 Hydrogen against other models. The rows below are rivals from the snapshots recorded in the sibling [MiniMax M3.1 Flash list](https://github.com/sandbase-lab/awesome-minimax-m3-1-flash/blob/main/docs/model-comparison.md) (Artificial Analysis snapshot 2026-10-19; Pelican Test read 2026-10-20). They are not Gemini 4 Hydrogen results. Check the [live boards][evals] for updates.

| Model (row on the board) | Intelligence Index (2026-10-19) | Cost per task (2026-10-19) |
|---|---|---|
| **Gemini 4 Hydrogen** | **not on the board** | — |
| Claude Opus 5.5 (Max) | 57.6 (#1) | $5.98 (#188) |
| Gemini 4 Argon (High) | 52.6 (#9) | $1.99 (#158) |
| GPT-6.1 Sol (Max) | 51.8 (#13) | $0.724 (#112) |
| DeepSeek V4.1 Flash 1017 (Max) | 45.1 (#36) | $0.262 (#74) |
| Claude Haiku 5.5 (Max) | 43.4 (#46) | $0.213 (#67) |

| Model (row on the leaderboard) | Score (2026-10-20) | Avg cost |
|---|---|---|
| **Gemini 4 Hydrogen** | **not on the leaderboard** | — |
| openai/gpt-6.1-sol | 3.79 | $0.026 |
| google/gemini-4-argon | 3.75 | $0.150 |
| anthropic/claude-opus-5.5 | 3.46 | $0.223 |
| deepseek/deepseek-v4.1-flash | 3.44 | $0.017 |

What this says, and what it doesn't:

- **No measured score for Gemini 4 Hydrogen.** Creators' price claims below cannot be checked against a board yet.
- **The price range on the boards is wide.** Cost per task runs from $0.213 to $5.98 among the rivals above, so a same-prompt cost gap of several times is plausible before any measurement exists. It is still a creator's single run.

## What creators reported

Same-prompt comparisons posted on X. Numbers are as the creator stated them. Tools, reasoning settings and runs differ, often one run each. Click through to watch both results. Costs are the creators' own figures, not our measurement.

| Creator | Task | Gemini 4 Hydrogen | Rival | Creator's verdict |
|---|---|---|---|---|
| [@marcthecreatorr][bikes] | SVG girl and cat on joined bikes, golden hour | ~15 min, ~$0.9 API cost (in Cursor) | Opus 5.5 in Claude Code: ~1 hr, ~$18 API cost | Opus took longer on detail (night mode, music); Hydrogen "got the whole scene done faster for less than a dollar" |
| [@EnvolDev][rio] | "Rio Above the Clouds" film, one prompt | $6.21 · 1h 33m 48s | Opus 5.5: $60.89 · 2h 19m 35s · Fable 5.2: $76.04 · 1h 59m 11s · GPT-6 Astra: $16.89 · 34m 06s | "Gemini 4 Hydrogen made the whole film for $6.21… But it's the least good of all." |
| [@EnvolDev][cathedral] | "Cathedral of Ice" scene | $4.27 · 1h 23m 40s | Gemini 4 Carbon: $8.83 · 2h 39m 10s · GPT-6.1 Sol: $3.11 · 54m 19s · Muse Spark 1.3: $5.56 · 2h | GPT-6.1 Sol "was the cheapest and the fastest of all four" |
| [@SidraMiconi][mito] | Mitochondrial motor simulation, one app | ~$0.36 · 201 s, one call plus one camera fix | — | Own build; no rival |
| [@noclipepe][walk] | Walking creatures, neural nets and a genetic algorithm | 27 generations · best 7.5 m · 36m 43s | Fable 5.2: 29 generations · best 7.4 m · 1h 34m · Qwen 4 Max: 32 generations · best 6.1 m · 1h 6m | "Gemini beat Fable by 10 cm. On its knees. Fable is the only one that actually walks." |
| [@DanielZambrini][daniel] | Stickman vs cursor, against Fable 5.2 | Smaller model, "still produce a fairly good result" | Fable 5.2 | "Fable is obviously better, but if I were in a hurry and wanted to save cash, I would still be fine with Hydrogen" |
| [@analogalok][motor] | Electric motor animation, single HTML file | — | Qwen 4 Max, Qwen 3.8 Max | Hydrogen "did the best overall job on 3D realism and visual clarity" |
| [@Aki_LIG][aki] | Three.js pelican riding a bicycle, same prompt as an earlier model | — | An earlier model (6.1 Terra) | "Never seen anything like this on the pelican test" (translated); "the output is completely different" |
| [@SahilPanhotra][lion] | Lion juggling across four seasons, interactive SVG with sound | — | Gemini 4 Carbon | Carbon "for raw detail & physics"; Hydrogen's season wipes and container clipping "are way cleaner", but it faked the juggling |
| [@Dain0x][globe] | Three-model globe comparison | — | GPT-6.2 Sol · Fable 5.2 | "For me, Fable wins this visual comparison." |

Read the table with the caveats the creators themselves gave:

- Costs are creators' figures. The Rio post says its setting changed between tests (Extra High in this run, High in an earlier one), so the runs are not strictly like for like ([@EnvolDev][rio]).
- Quality was split. Hydrogen was preferred on 3D realism and on the walking race, and the Rio film and the globe comparison went to other models on quality.
- One post credits Hydrogen with the whole result, but the creator's technical notes describe a ComfyUI image-to-video pipeline built on a different model. Treat it as outside the HTML-page comparison ([@nyapan_mohy][nyapan]).

The pattern across creators: on cost, Hydrogen was among the cheapest runs on the frontier rivals in these posts, around a tenth of Opus 5.5's cost on the Rio film and about half of Carbon's on the cathedral scene, by our arithmetic from the figures above. On quality the picture is mixed, and no measured board supports either side yet.

## Rerun before you trust a comparison

Results move a lot with the setup. Run the same prompt yourself: paste it into the [Lab text arena][arena] with two or three models selected, or see the [tutorial](tutorial.md).

## More measurements

- [Lab Evals boards][evals]: check for a Gemini 4 Hydrogen row, and re-check this page when one appears.
- [Lab Pelican Test][pelican]: same prompt on every model, scored the same way, with the drawings on screen.
- [All AI video collections on SandBase Lab][collections]: the same list for other models.

---

Lab data: [Evals boards][evals] (Artificial Analysis, snapshot 2026-10-19) and [Pelican Test][pelican] (read 2026-10-20), as recorded in the sibling list; neither has a Gemini 4 Hydrogen row. Creator data: their posts, linked; not independently verified.

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
