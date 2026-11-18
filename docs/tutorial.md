# Gemini 4 Hydrogen tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. Gemini 4 Hydrogen writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and Gemini 4 Hydrogen selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to Gemini 4 Hydrogen and run once. Every model gets the same words, and each result shows its cost and time. Creators on launch week ran this kind of head-to-head: 53 of the 148 posts in this collection are tagged as tests and comparisons. It is the quickest way to check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or call the API

Gemini 4 Hydrogen is `google/gemini-4-hydrogen` on SandBase, OpenAI-compatible, with a 1,048,576-token context window.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "google/gemini-4-hydrogen",
  max_tokens: 128000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > gemini-4-hydrogen.html
jq '.usage' response.json
```

- `max_tokens: 128000`: hidden reasoning tokens come out of the same budget as the page itself. A budget that is too small gives you a truncated page, and you still pay for the tokens.
- `--max-time 900`: a long page can take several minutes. Creators reported single runs from about 3 minutes to over an hour.
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for. Input is $1.50 per million tokens, output is $7.50 per million, and cached input reads are billed at 5% of the input rate. Prices are on the [model page][model].

Open `gemini-4-hydrogen.html` in a browser. If it is blank, open the developer console. The usual causes are a truncated file (raise `max_tokens`) or a CDN that did not load (ask for everything inline or from a CDN you trust).

## 4. Turn the page into a video

Most creators screen-record the page. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs gemini-4-hydrogen.html gemini-4-hydrogen.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay camera tour or a fixed-length loop (see [prompt guide §3](prompt-guide.md#3-spell-out-the-motion-in-full-sentences)), so nothing depends on a mouse.

The recording is picture only. Add audio in the edit, or capture the tab audio if the page makes sound and you record it yourself. Do not use a microphone.

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBase Sandbox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention Gemini 4 Hydrogen. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-gemini-4-hydrogen/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-hydrogen&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[model]: https://www.sandbase.ai/model/google/gemini-4-hydrogen?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
