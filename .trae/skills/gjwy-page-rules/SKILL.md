---
name: gjwy-page-rules
description: 王赫高级网页设计作品集项目的页面创建与编辑规则。Use when creating or modifying any HTML, CSS or JS file in the gjwy workspace — enforces wh_ naming prefix, prompt logging to wang_prompt.md, index.html card and back-link, signature comment and code style. Do not use for files outside this workspace.
---

# GJWY 页面规则

本工作区是王赫《高级网页设计》课堂实践作品集。创建或修改页面时执行以下规则。

## 技术栈与资源

- 仅使用原生 HTML、CSS 和 JavaScript，禁止第三方库和 CDN
- 图标统一使用项目内 iconfont 图标（`fond/download/font_5244711_*` 目录），本地引入 `iconfont.css` 或 `iconfont.js`

## 执行任务前

先向 `wang_prompt.md` 追加一条记录，只追加不覆盖，格式：

```markdown
## yyyy-MM-dd HH:mm:ss
- 模型: 当前模型名
- 提示词: 用户原始提示词
```

## 命名规范

- 所有 CSS 类名、ID 名、JS 变量必须以 `wh_` 开头

## 新建页面

1. 在 `index.html` 首页作品集中添加对应该页面的卡片
2. 页面内添加指向 `index.html` 的「返回首页」超链接

## 代码风格

- 以 doctype、`lang="zh-CN"`、viewport meta 开头
- 使用 `* { box-sizing: border-box }` 重置
- 字体使用 `system-ui, sans-serif`（或 Microsoft YaHei）
- 每次新建 HTML 文件时，必须在 `<head>` 内紧跟 charset 之后插入署名注释：
  `<!-- 姓名：王赫，建立时间：yyyy-MM-dd HH:mm，模型：所使用的大模型名称，功能：页面功能名称 -->`
- 除署名注释外，不写任何代码注释
