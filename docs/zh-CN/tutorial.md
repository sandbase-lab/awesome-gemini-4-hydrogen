# Gemini 4 Hydrogen 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成 MP4。Gemini 4 Hydrogen 写网页，你来播放并录制。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，以及作者公开的提示词（如果有）。点 **复刻**，Lab 会打开文本竞技场，自动填好帖子内容并选中 Gemini 4 Hydrogen。登录后运行，就能拿到 HTML，并带实时预览。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

在[文本竞技场][arena]里，在 Gemini 4 Hydrogen 旁边再加一两个模型，跑一次。所有模型拿到同样的文字，每个结果都显示花费和耗时。发布之初，作者们就是这样做对比的：本合集 148 条帖子里有 53 条被标为测试与对比。这也是在你自己任务上验证[对比页](model-comparison.md)结论的最快方式。

## 3. 或者直接调用 API

Gemini 4 Hydrogen 在 SandBase 上的模型 ID 是 `google/gemini-4-hydrogen`，兼容 OpenAI，上下文窗口 1,048,576 token。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=sk-sb-...`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

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

- `max_tokens: 128000`：隐藏的推理 token 和页面本身占用同一份额度。额度给小了，你会拿到被截断的页面，而且照样为这些 token 付费。
- `--max-time 900`：长页面要跑好几分钟。作者报告的单次运行从约 3 分钟到超过 1 小时都有。
- `sed '/^```/d'` 去掉模型可能加上的 Markdown 代码围栏。
- `usage` 显示计费的 token。输入每百万 $1.50，输出每百万 $7.50，缓存的输入读取按输入价的 5% 计费。价格见[模型页][model]。

用浏览器打开 `gemini-4-hydrogen.html`。如果一片空白，打开开发者工具：常见原因是被截断的文件（加大 `max_tokens`）或 CDN 没加载（要求所有资源内联，或使用你信任的 CDN）。

## 4. 把页面录成视频

大多数作者是直接录屏。想每次得到一样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs) 无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或使用本机 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs gemini-4-hydrogen.html gemini-4-hydrogen.mp4 12 1920 1080   # 12 秒，1080p
```

它按你给的尺寸打开页面，录指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的效果，就在提示词里要求自动镜头巡游或定长循环（见[提示词写法 §3](prompt-guide.md#3-把动作写完整用完整的句子)），让整个画面不依赖鼠标。

录制本身只有画面。需要声音的话，在剪辑时加入；如果页面自带声音并由你自己录制，就捕获标签页的音频，不要用麦克风。

## 安全运行生成的代码

这段 HTML 是你没读过的代码。单文件页面从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。对于不完全信任的内容，或者要批量运行很多页面，请使用 [SandBase Sandbox][sandbox]：一个有时限、接触不到你的文件和 Key 的隔离环境。

## 分享

把视频发到 X，附上提示词并 @ Gemini 4 Hydrogen。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-gemini-4-hydrogen/issues/new?template=submit-video.yml)；通过后会先进入 Lab 合集，下一次每日同步时出现在本列表。

[lab]: https://www.sandbase.ai/lab/ai-videos/gemini-4-hydrogen?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[arena]: https://www.sandbase.ai/arena/text?models=google%2Fgemini-4-hydrogen&utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[model]: https://www.sandbase.ai/model/google/gemini-4-hydrogen?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-gemini-4-hydrogen
