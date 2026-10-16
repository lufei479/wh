# AGENTS.md

## 项目简介
王赫《高级网页设计》课堂实践作品集。纯原生 HTML/CSS，不使用 CDN 和外部库。

## 命名规范
- 所有 CSS 类名、ID 名、JS 变量必须以 `wang_` 开头

## 提示词记录
- 每次执行任务前，先追加写入 `wang_prompt.md`
- 每条记录包含：时间（yyyy-MM-dd HH:mm:ss）、模型、提示词内容
- 只追加，不覆盖已有内容

## 文件组织
- `index.html` 为首页，含所有页面的作品集卡片
- 新建页面必须：① 在首页作品集添加对应卡片；② 页内添加「返回首页」指向 index.html 的超链接

## 代码风格
- doctype + `lang="zh-CN"` + viewport meta
- `* { box-sizing: border-box }` 重置
- 字体 `system-ui, sans-serif`（或 Microsoft YaHei）
- 不写代码注释
