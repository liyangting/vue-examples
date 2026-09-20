"""Build a dependency-free, static source browser for GitHub Pages."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import shutil

root = Path(__file__).resolve().parent.parent
out = root / 'dist'
out.mkdir(exist_ok=True)
files = sorted(p for p in root.rglob('*') if p.suffix in {'.vue', '.ts'} and not any(part.startswith('.') or part in {'node_modules', 'dist'} for part in p.relative_to(root).parts))
nav = ''.join(f'<a href="#{quote(p.relative_to(root).as_posix(), safe="")}">{escape(p.relative_to(root).with_suffix("").as_posix())}</a>' for p in files)
articles = ''.join(f'<article id="{quote(p.relative_to(root).as_posix(), safe="")}"><h2>{escape(p.stem)}</h2><p class="path">{escape(p.relative_to(root).as_posix())}</p><pre><code>{escape(p.read_text())}</code></pre></article>' for p in files)
page = '''<!doctype html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Vue 示例代码</title><meta name="description" content="Vue 与 TypeScript 开发示例代码"><style>
:root{color-scheme:light dark;--bg:#fff;--fg:#242936;--muted:#606775;--line:#e2e5eb;--panel:#f6f8fa;--link:#3451b2}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.75 system-ui,sans-serif}a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}a:focus-visible{outline:2px solid var(--link);outline-offset:4px}header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:18px 5%;display:flex;justify-content:space-between;gap:20px;z-index:1}header nav{display:flex;gap:24px}.layout{max-width:1400px;margin:auto;display:grid;grid-template-columns:260px minmax(0,1fr)}aside{position:sticky;top:80px;align-self:start;padding:30px 24px;max-height:calc(100vh - 80px);overflow:auto}aside a{display:block;padding:8px 0;color:var(--fg)}main{min-width:0;border-left:1px solid var(--line);padding:32px 48px}h1{font-size:30px}h2{font-size:24px}article{padding:20px 0 36px;border-top:1px solid var(--line)}.path{font-size:14px;color:var(--muted)}pre{padding:20px;background:var(--panel);border:1px solid var(--line);border-radius:8px;overflow:auto;font:14px/1.8 ui-monospace,monospace}@media(prefers-color-scheme:dark){:root{--bg:#1b1b1f;--fg:#e3e3e8;--muted:#aaaab4;--line:#34343b;--panel:#242429;--link:#a8b8ff}}@media(max-width:760px){header{position:static;flex-wrap:wrap}.layout{display:block}aside{position:static;max-height:none;padding:20px}main{border:0;padding:20px}header nav{gap:18px}}
</style></head><body><header><strong>Vue 示例代码</strong><nav aria-label="主导航"><a href="https://liyangting.github.io/share-files/">面试</a><a href="./" aria-current="page">demo示例</a><a href="https://github.com/liyangting/vue-examples">GitHub</a></nav></header><div class="layout"><aside aria-label="示例目录"><strong>示例目录</strong>''' + nav + '''</aside><main><h1>Vue 与 TypeScript 示例</h1><p>按文件浏览开发笔记与代码片段。示例源码供阅读和复用，尚未提供在线运行环境。</p>''' + articles + '''</main></div></body></html>'''
(out / 'index.html').write_text(page)
(out / '.nojekyll').touch()
print(f'Built {len(files)} examples → dist/index.html')
