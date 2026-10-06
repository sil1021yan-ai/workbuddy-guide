# WorkBuddy 小白实战指南

> 第三方非官方 · 基于 WorkBuddy 官方指南改写 · © 作者保留所有权利

一个以真实任务为主线的 WorkBuddy 中文使用手册。从下载安装和第一个任务开始，
再到 Skill、连接器、自动化与多智能体，最终把一次成功沉淀为可复用的工作系统。

本仓库由 [AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)
（MIT）的 VitePress 脚手架改造而来，**代码保留 MIT 许可与原作者署名**；
**教程正文为作者原创改写，版权归作者所有（All Rights Reserved）**。详见
[ATTRIBUTIONS.md](./ATTRIBUTIONS.md) 与 [CONTENT_LICENSE.md](./CONTENT_LICENSE.md)。

## 技术栈
- [VitePress](https://vitepress.dev/) 静态站点
- 部署：GitHub Pages（通过 `.github/workflows/deploy.yml` 自动构建并发布到 `gh-pages`）
- 维护：`.github/workflows/monitor.yml` 每周抓取官方文档变化，自动开 Issue

## 本地开发
```bash
npm install
npm run docs:dev      # 本地预览 http://127.0.0.1:5173/workbuddy-guide/
npm run docs:build    # 构建到 docs/.vitepress/dist
```

## 内容维护流程
1. 每周一，monitor.yml 检查 `monitor/targets.json` 中的官方页面是否有变化。
2. 有变化 → 自动开 Issue（标注 新增/修改/不可达）。
3. 人工将官方变化改写为「小白可完成的任务路径」，更新 `docs/bluebook/` 下对应章节。
4. 合并到 `main` → 自动构建并发布。

## 版权
- 教程正文：© 作者，All Rights Reserved（见 `CONTENT_LICENSE.md`）。
- 网站代码：MIT，原作者 AlephAITech（见 `LICENSE`）。
- 官方文档版权归腾讯，本指南仅作学习整理，非官方作品。
