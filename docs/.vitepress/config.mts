import { defineConfig } from "vitepress";

import { siteSidebar } from "./sidebar";
import { configureMermaidMarkdown } from "./mermaid-markdown";
import { createPageDescription, createSeoHead } from "./seo";

const siteUrl =
  process.env.VITEPRESS_SITE_URL ||
  "https://sili021yan-ai.github.io/workbuddy-guide";

export default defineConfig({
  base: "/workbuddy-guide/",
  lang: "zh-CN",
  title: "WorkBuddy 小白实战指南",
  titleTemplate: ":title · WorkBuddy 小白实战指南",
  description:
    "以真实任务为主线的 WorkBuddy 中文使用手册：从安装入门到 AI 工作系统。",
  cleanUrls: true,
  lastUpdated: true,
  srcExclude: ["**/source.md", "plans/**"],
  sitemap: {
    hostname: siteUrl,
  },
  transformPageData: (pageData, { siteConfig }) => {
    return {
      description: createPageDescription(siteConfig.srcDir, pageData),
    };
  },
  transformHead: (context) => createSeoHead(siteUrl, context),
  head: [
    ["link", { rel: "icon", type: "image/svg+xml", href: "/favicon.svg" }],
    ["meta", { name: "theme-color", content: "#d8f238" }],
    ["meta", { name: "author", content: "sili021yan-ai" }],
    [
      "meta",
      {
        name: "keywords",
        content:
          "WorkBuddy,WorkBuddy 教程,AI Agent,AI 工作系统,Skills,连接器,自动化,多智能体,职场 AI",
      },
    ],
    // 统计：Cloudflare Web Analytics。把下面的 token 换成你在 Cloudflare 创建的
    // Web Analytics 站点的 token 即可开始收集数据（无 token 时不影响访问）。
    [
      "script",
      {
        defer: "",
        src: "https://static.cloudflareinsights.com/beacon.min.js",
        "data-cf-beacon":
          '{"token":"REPLACE_WITH_YOUR_CF_WEB_ANALYTICS_TOKEN"}',
      },
    ],
  ],
  markdown: {
    config: configureMermaidMarkdown,
    image: {
      lazyLoading: true,
    },
    theme: {
      light: "github-light",
      dark: "github-dark",
    },
  },
  themeConfig: {
    siteTitle: "WorkBuddy Guide",
    nav: [
      { text: "首页", link: "/" },
      { text: "开始阅读", link: "/bluebook/" },
      { text: "版权与署名", link: "/attributions" },
    ],
    sidebar: siteSidebar,
    socialLinks: [
      { icon: "github", link: "https://github.com/sili021yan-ai/workbuddy-guide" },
    ],
    search: {
      provider: "local",
    },
    outline: {
      level: [2, 3],
      label: "本页目录",
    },
    docFooter: {
      prev: "上一篇",
      next: "下一篇",
    },
    lastUpdated: {
      text: "最后更新",
      formatOptions: {
        dateStyle: "medium",
        timeStyle: "short",
      },
    },
    editLink: {
      pattern:
        "https://github.com/sili021yan-ai/workbuddy-guide/edit/main/docs/:path",
      text: "在 GitHub 上改进此页",
    },
    footer: {
      message:
        "本站为第三方非官方整理 · 代码基于 WorkBuddyGuide（MIT）· 教程内容 © sili021yan-ai 保留所有权利",
      copyright: "Copyright © 2026 sili021yan-ai",
    },
  },
});
