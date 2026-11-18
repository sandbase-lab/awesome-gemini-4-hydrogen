"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'gemini-4-hydrogen'
REPO = 'sandbase-lab/awesome-gemini-4-hydrogen'

CFG = dict(
    slug=SLUG,
    kind='code',
    name='Gemini 4 Hydrogen',
    short='Gemini 4 Hydrogen',  # how the prose refers to the model after the first mention
    vendor='Google',
    model_id='google/gemini-4-hydrogen',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-gemini-4-hydrogen',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/google/gemini-4-hydrogen',
    arena=f'{SITE}/arena/text?models=google%2Fgemini-4-hydrogen',
    evals=f'{SITE}/leaderboards',
    pelican=f'{SITE}/arena/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-gemini-4-hydrogen-sync/1.0 (+https://github.com/{REPO})',
    html_out='gemini-4-hydrogen.html',
    # Output limit for the curl example. Gemini 4 Hydrogen's hidden reasoning comes out of
    # max_tokens, and creators report runs of several minutes, so the example asks for 128,000.
    max_tokens=128000,
    max_tokens_limit=None,  # output cap not in the launch data; fill from `sandbase inspect`
    context_length=1048576,
    guide_patterns=7,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome Gemini 4 Hydrogen',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'gemini', 'opus', 'claude',
                 'sonnet', 'haiku', 'fable', 'gpt', 'argon', 'carbon', 'deepseek', 'kimi', 'grok', 'qwen',
                 'glm', 'muse', 'astra'),
    not_affiliated={'en': 'Not affiliated with or endorsed by Google.', 'zh-CN': '与 Google 无隶属或背书关系。'},
    # No SandBase blog post on this model is in the launch data, so the reading section stays off.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: `sandbase inspect google/gemini-4-hydrogen` (pricing and context), the
# Lab collection's own posts (linked to X), and the creator posts quoted in the comparison doc.
# No Lab Evals row or Pelican Test row for this model existed when the list shipped.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **Gemini 4 Hydrogen examples**: videos, prompts and demos made with Google\'s Gemini 4 Hydrogen, announced on November 12, 2026. Three.js 3D scenes, SVG and canvas animation, motion graphics, product UI and playable browser games, most of them written as one self-contained HTML or SVG file from a prompt, each one credited to its creator and linked to the original post.',
        'alt': 'Awesome Gemini 4 Hydrogen: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API and a recording script'),
            ('Pick a model', '[Gemini 4 Hydrogen against the creator reports and the Lab measurements](docs/model-comparison.md)'),
            ('Try it now', '[Run Gemini 4 Hydrogen in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible). Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. The call above asks for `max_tokens` of 128,000 because hidden reasoning counts against that budget. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is Gemini 4 Hydrogen?', 'Gemini 4 Hydrogen is a Google model on SandBase, announced on November 12, 2026. It has a 1,048,576-token context window, and it is priced at $1.50 per million input tokens and $7.50 per million output tokens, with cached input reads at 5% of the input rate. On SandBase it is `{model_id}`. Source: `sandbase inspect google/gemini-4-hydrogen`.'),
            ('How are these Gemini 4 Hydrogen videos made?', 'The model doesn\'t render video. It writes a web page or an SVG (Three.js, canvas, CSS or SVG animation), and the creator records the page playing. Creators describe one-call runs and multi-step runs in their own posts. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good Gemini 4 Hydrogen prompt?', 'Name one self-contained file and the renderer you want, spell out the motion and the physics you expect, and say how the result should be checked. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the Gemini 4 Hydrogen API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint. One key works for every model. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is Gemini 4 Hydrogen better than Gemini 4 Carbon, Claude Opus 5.5 or Fable 5.2?', 'Creators disagree, and the measured side is empty. Creator runs put it cheaper than Opus 5.5 and Fable 5.2 on the same prompt ($6.21 against $60.89 and $76.04 for one film), and cheaper than Gemini 4 Carbon on a cathedral scene ($4.27 against $8.83). On quality it is split: one creator rated it best on 3D realism against Qwen models, another found Carbon better at physics and detail, and another said Fable is better but Hydrogen is fine when cost matters. The data behind this list has no Gemini 4 Hydrogen row on the Lab [Evals boards]({evals}) or the [Pelican Test]({pelican}) yet. Details: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'Creators report about $0.90 for an SVG scene in Cursor, $0.36 for a one-prompt app, $4.27 for a cathedral scene and $6.21 for a film. List prices are on the [model page]({model_page}), and reasoning tokens bill as output.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a Gemini 4 Hydrogen creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'Gemini 4 Hydrogen prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} Gemini 4 Hydrogen videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **Gemini 4 Hydrogen 案例**合集：用谷歌的 Gemini 4 Hydrogen（2026 年 11 月 12 日公布）做出的视频、提示词和演示。包括 Three.js 3D 场景、SVG 与 Canvas 动画、动效、产品界面和可在浏览器里玩的游戏，大多是模型根据提示词写成的单文件 HTML 或 SVG，均注明作者并链接原帖。',
        'alt': 'Awesome Gemini 4 Hydrogen：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API 调用和录屏脚本'),
            ('选模型', '[Gemini 4 Hydrogen 对照创作者报告与 Lab 实测](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 Gemini 4 Hydrogen]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI）。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。上面的示例把 `max_tokens` 设为 128000，因为隐藏的推理 token 也占用这份额度。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('Gemini 4 Hydrogen 是什么？', 'Gemini 4 Hydrogen 是谷歌的模型，2026 年 11 月 12 日公布，在 SandBase 上可用。上下文窗口 1,048,576 token，标价为每百万输入 token $1.50、每百万输出 token $7.50，缓存的输入读取按输入价的 5% 计费。在 SandBase 上它是 `{model_id}`。来源：`sandbase inspect google/gemini-4-hydrogen`。'),
            ('这些 Gemini 4 Hydrogen 视频是怎么做出来的？', '模型并不直接渲染视频。它写出网页或 SVG（Three.js、Canvas、CSS 或 SVG 动画），作者再把页面播放过程录下来。作者在自己的帖子里既描述过一次调用完成的情况，也描述过多步完成的情况。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 Gemini 4 Hydrogen 提示词？', '指定输出一个独立文件和你要的渲染方式，写清楚期望的动作和物理效果，并说明怎样检查结果。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 Gemini 4 Hydrogen API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口，一个 Key 调用所有模型。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('Gemini 4 Hydrogen 比 Gemini 4 Carbon、Claude Opus 5.5 或 Fable 5.2 更强吗？', '创作者的看法不一，而实测一侧目前是空的。同一提示词下，创作者的运行结果显示它比 Opus 5.5 和 Fable 5.2 便宜（一部影片 $6.21 对 $60.89 和 $76.04），在一个大教堂场景里也比 Gemini 4 Carbon 便宜（$4.27 对 $8.83）。效果上则是分裂的：一位在 3D 写实度上把它排在 Qwen 模型之前，另一位认为 Carbon 的物理和细节更好，还有一位说 Fable 更好，但在意成本时 Hydrogen 够用。Lab [Evals 榜单]({evals}) 和 [Pelican Test]({pelican}) 所依据的数据里还没有 Gemini 4 Hydrogen 的行。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '创作者报告的花费：Cursor 里一个 SVG 场景约 $0.9，一次提示词做出的应用 $0.36，大教堂场景 $4.27，一部影片 $6.21。标价见 [模型页]({model_page})，推理 token 按输出计费。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 Gemini 4 Hydrogen 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'Gemini 4 Hydrogen 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 Gemini 4 Hydrogen 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
