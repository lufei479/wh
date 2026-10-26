---
name: wh-push-github
description: 将 d:\gjwy 整个项目 commit 并 push 到 GitHub 仓库 lufei479/wh（SSH 方式）。Use when the user asks to 提交 / 上传 / 推送 / 同步 / 备份 项目到 GitHub 或 lufei479/wh。Do not use for pushing to other repositories.
---

# WH 推送 GitHub

把当前工作区（d:\gjwy）提交并推送到 GitHub 仓库 `lufei479/wh`。

## 远程配置

- 仓库地址（SSH 443 端口）：`ssh://git@ssh.github.com:443/lufei479/wh.git`（22 端口被网络封锁，且 hosts 将 github.com 指向 127.0.0.1，故必须用 ssh.github.com:443）
- 推送使用的远程名固定为 `github`（`origin` 保留给 Gitee，不得改动或删除）
- 若 `git remote get-url github` 报错不存在，先执行：
  `git remote add github ssh://git@ssh.github.com:443/lufei479/wh.git`
- 仓库级 sshCommand 必须指向 Windows 系统自带 OpenSSH（Git 自带的 MSYS OpenSSH 无法解析中文用户路径 `C:\Users\王赫`，会找不到私钥）：
  `git config core.sshCommand "C:/WINDOWS/System32/OpenSSH/ssh.exe -o UserKnownHostsFile=D:/gjwy/.git/wh_known_hosts -o StrictHostKeyChecking=yes"`
- `D:\gjwy\.git\wh_known_hosts` 已存有 GitHub 官方 Ed25519 主机密钥（指纹已核验为 SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU），勿删
- SSH 公钥已配置于 GitHub（本地 `~/.ssh/id_ed25519`，指纹 SHA256：M6Ug8Kw2TNXeftQJPkwtAhECw04O5yHULOby9Va2euY）

## 操作步骤

1. 按 gjwy-page-rules 规则，先向 `wang_prompt.md` 追加本次提示词记录
2. `git status --short` 查看变更；`git add` 逐个添加相关文件（整个项目同步时用 `git add -A`）
3. 提交信息用中文一句话概括本次变更（参照仓库已有提交风格）
4. `git push github master` 推送；被拒绝时先 `git pull github master --rebase` 再推，禁止 force push

## 注意事项

- 每次提交前必须确认 `git user.name` 与 `git user.email` 已配置，缺省时报告用户而不是修改 git config
- 推送前不要提交 `.env`、密钥等敏感文件；`id_ed25519` 等私钥位于用户目录，不在本仓库内，无需处理
