"""Build a dependency-free, static source browser for GitHub Pages."""
from pathlib import Path
from html import escape
from urllib.parse import quote


root = Path(__file__).resolve().parent.parent
out = root / 'dist'
out.mkdir(exist_ok=True)
files = sorted(p for p in root.rglob('*') if p.suffix in {'.vue', '.ts'} and not any(part.startswith('.') or part in {'node_modules', 'dist'} for part in p.relative_to(root).parts))
def page_name(path):
    # Keep the source extension to distinguish foo.vue from foo.ts.
    return path.relative_to(root).as_posix() + '.html'


def navigation(current, prefix):
    links = []
    for path in files:
        active = ' aria-current="page"' if path == current else ''
        href = prefix + quote(page_name(path), safe='/')
        label = escape(path.relative_to(root).with_suffix('').as_posix())
        links.append(f'<a href="{href}"{active}>{label}</a>')
    return ''.join(links)


nav = '__NAVIGATION__'
articles = '__CONTENT__'
page = '''<!doctype html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>__TITLE__</title><meta name="description" content="Vue 与 TypeScript 开发示例代码"><style>
:root{color-scheme:light dark;--bg:#fff;--fg:#242936;--muted:#606775;--line:#e2e5eb;--panel:#f6f8fa;--link:#3451b2}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.75 system-ui,sans-serif}a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}a:focus-visible{outline:2px solid var(--link);outline-offset:4px}header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:18px 5%;display:flex;justify-content:space-between;gap:20px;z-index:1}header nav{display:flex;gap:24px}.layout{max-width:1400px;margin:auto;display:grid;grid-template-columns:260px minmax(0,1fr)}aside{position:sticky;top:80px;align-self:start;padding:30px 24px;max-height:calc(100vh - 80px);overflow:auto}aside a[aria-current="page"]{color:var(--link);font-weight:700}aside a{display:block;padding:8px 0;color:var(--fg)}main{min-width:0;border-left:1px solid var(--line);padding:32px 48px}h1{font-size:30px}h2{font-size:24px}article{padding:20px 0 36px;border-top:1px solid var(--line)}.path{font-size:14px;color:var(--muted)}pre{padding:20px;background:var(--panel);border:1px solid var(--line);border-radius:8px;overflow:auto;font:14px/1.8 ui-monospace,monospace}@media(prefers-color-scheme:dark){:root{--bg:#1b1b1f;--fg:#e3e3e8;--muted:#aaaab4;--line:#34343b;--panel:#242429;--link:#a8b8ff}}@media(max-width:760px){header{position:static;flex-wrap:wrap}.layout{display:block}aside{position:static;max-height:none;padding:20px}main{border:0;padding:20px}header nav{gap:18px}}
</style></head><body><header><strong>Vue 示例代码</strong><nav aria-label="主导航"><a href="https://liyangting.github.io/share-files/">面试</a><a href="__HOME__">demo示例</a><a href="https://github.com/liyangting/vue-examples">GitHub</a></nav></header><div class="layout"><aside aria-label="示例目录"><strong>示例目录</strong>''' + nav + '''</aside><main>''' + articles + '''</main></div></body></html>'''
def render(title, nav_html, content, home):
    # Single substitution pass keeps placeholder-like text inside source intact.
    import re
    values = {'__TITLE__': escape(title), '__NAVIGATION__': nav_html,
              '__CONTENT__': content, '__HOME__': home}
    return re.sub('|'.join(values), lambda match: values[match.group()], page)


home_content = '<h1>Vue 与 TypeScript 示例</h1><p>从目录选择一个示例，进入独立页面查看源码。代码片段供阅读和复用，尚未提供在线运行环境。</p>'
(out / 'index.html').write_text(render('Vue 示例代码', navigation(None, './'), home_content, './'), encoding='utf-8')
for source in files:
    relative = source.relative_to(root)
    prefix = '../' * len(relative.parent.parts) or './'
    content = (f'<article><h1>{escape(source.stem)}</h1>'
               f'<p class="path">{escape(relative.as_posix())}</p>'
               f'<pre><code>{escape(source.read_text(encoding="utf-8"))}</code></pre></article>')
    target = out / page_name(source)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(source.stem + ' | Vue 示例代码', navigation(source, prefix), content, prefix), encoding='utf-8')
(out / '.nojekyll').touch()
print(f'Built home page and {len(files)} independent example pages → dist/')
