# Vue 示例代码

网站：https://liyangting.github.io/vue-examples/

根目录及子目录中的 `.vue`、`.ts` 文件会自动加入示例阅读站，按文件名显示。源码只作阅读展示，不执行代码片段。

## 发布

1. 提交并推送本仓库改动到 main。
2. 在 Settings → Pages → Source 中选择 GitHub Actions。
3. 在 Actions 中运行 Deploy examples to GitHub Pages，等待 build 和 deploy 成功。

之后推送到 main 会自动更新网站。

## 本地构建

```sh
python3 scripts/build.py
python3 -m http.server 4174 --directory dist
```

访问 http://localhost:4174/ 。无需安装额外依赖。
