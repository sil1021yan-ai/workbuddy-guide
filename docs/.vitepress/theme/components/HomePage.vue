<script setup lang="ts">
import PixelIcon from "./PixelIcon.vue";
import PixelIconSprite from "./PixelIconSprite.vue";
</script>

<template>
  <main class="wb-home">
    <PixelIconSprite />
    <section class="wb-hero" aria-labelledby="wb-hero-title">
      <div class="wb-hero__stage">
        <div class="wb-hero__copy">
          <p class="wb-pixel-label">OPEN-SOURCE · 28 CHAPTERS · 2026</p>
          <h1 id="wb-hero-title" class="wb-hero__title--bluebook">WorkBuddy小白实战指南</h1>
          <p class="wb-hero__summary">
            WorkBuddy能干嘛？一套以真实工作为主线的WorkBuddy实践路径。带你从0到1先用起来，再从1到100把每次成功沉淀为可复用的工作系统，真正把AI变成生产力！本指南为第三方非官方整理，内容基于官方指南改写。
          </p>
          <div class="wb-hero__actions">
            <a class="wb-button wb-button--primary" href="/workbuddy-guide/bluebook/">
              <span>开始阅读</span>
              <PixelIcon name="arrow-right" />
            </a>
            <a class="wb-button wb-button--outline" href="/workbuddy-guide/attributions">版权与署名</a>
          </div>
        </div>

        <div class="wb-hero__art" aria-label="WorkBuddy 像素图标组合">
          <span class="wb-hero__monogram">WB_</span>
          <span class="wb-icon-card wb-icon-card--buddy">
            <PixelIcon name="face-grin" />
          </span>
          <span class="wb-icon-card wb-icon-card--book">
            <PixelIcon name="book" />
          </span>
          <span class="wb-icon-card wb-icon-card--flow">
            <PixelIcon name="sitemap" />
          </span>
          <span class="wb-icon-card wb-icon-card--work">
            <PixelIcon name="briefcase" />
          </span>
          <div class="wb-hero__metrics" aria-label="指南内容规模">
            <span><b>28</b> CHAPTERS</span>
            <span><b>4</b> PARTS</span>
            <span><b>∞</b> WORKFLOWS</span>
          </div>
        </div>
      </div>

      <div class="wb-value-strip" aria-label="指南价值">
        <div class="wb-value-strip__item">
          <PixelIcon name="check-box" />
          <span><b>真实任务</b><small>REAL TASKS</small></span>
        </div>
        <div class="wb-value-strip__item">
          <PixelIcon name="refresh" />
          <span><b>可复现</b><small>REPRODUCIBLE</small></span>
        </div>
        <div class="wb-value-strip__item">
          <PixelIcon name="handshake" />
          <span><b>官方改写</b><small>OFFICIAL-BASED</small></span>
        </div>
        <div class="wb-value-strip__item">
          <PixelIcon name="grid" />
          <span><b>系统沉淀</b><small>WORK SYSTEM</small></span>
        </div>
      </div>
    </section>

    <section class="wb-section wb-reading" aria-labelledby="wb-reading-title">
      <div class="wb-section__heading">
        <div>
          <p class="wb-pixel-label">READING PATH / 01—04</p>
          <h2 id="wb-reading-title">四段路径，按你的目标进入</h2>
        </div>
        <p>从个人上手到组织落地，循序渐进，构建你的 WorkBuddy 工作系统。</p>
      </div>

      <div class="wb-reading-grid">
        <a class="wb-reading-card" href="/workbuddy-guide/bluebook/第一篇%20使用手册：先把%20WorkBuddy%20用起来/">
          <span class="wb-reading-card__icon"><PixelIcon name="user" /></span>
          <span class="wb-reading-card__content">
            <small>PART 01 · CH. 01—11</small>
            <strong>从 0 到 1：先把 WorkBuddy 用起来</strong>
            <span>安装、界面、第一个任务、Skill、连接器、API 与自动化。</span>
            <em><b>新手推荐</b><b>先完成一项任务</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/workbuddy-guide/bluebook/第二篇%20案例篇：从一项任务到一支%20AI%20团队/">
          <span class="wb-reading-card__icon"><PixelIcon name="briefcase" /></span>
          <span class="wb-reading-card__content">
            <small>PART 02 · CH. 12—22</small>
            <strong>进入真实案例：让任务开始流动</strong>
            <span>办公、文件、远程、资讯、知识、会议、投资和内容增长。</span>
            <em><b>11 个案例</b><b>任务驱动</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/workbuddy-guide/bluebook/第三篇%20进阶篇：把案例变成自己的工作系统/">
          <span class="wb-reading-card__icon"><PixelIcon name="sitemap" /></span>
          <span class="wb-reading-card__content">
            <small>PART 03 · CH. 23—26</small>
            <strong>把案例变成可复用的工作系统</strong>
            <span>打造 Skill、多 Agent 系统设计与可靠的自动化工作流。</span>
            <em><b>系统进阶</b><b>可靠自动化</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/workbuddy-guide/bluebook/第四篇%20岗位与行业落地/">
          <span class="wb-reading-card__icon"><PixelIcon name="users" /></span>
          <span class="wb-reading-card__content">
            <small>PART 04 · CH. 27—28</small>
            <strong>落到岗位与行业，组建 AI 团队</strong>
            <span>从通用能力出发，设计适合不同岗位和行业的工作流。</span>
            <em><b>团队落地</b><b>行业路线</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>
      </div>
    </section>

    <section class="wb-section wb-task-index" aria-labelledby="wb-task-index-title">
      <div class="wb-section__heading wb-section__heading--compact">
        <div>
          <p class="wb-pixel-label">START WITH A REAL TASK</p>
          <h2 id="wb-task-index-title">你现在想让 AI 帮你做什么？</h2>
        </div>
        <p>不必从头读。带着问题进来，先跑通一个能验收的结果。</p>
      </div>

      <div class="wb-task-grid">
        <a href="/workbuddy-guide/bluebook/第二篇%20案例篇：从一项任务到一支%20AI%20团队/">
          <PixelIcon name="briefcase" /><strong>办公文档</strong><span>Word · Excel · PPT</span>
        </a>
        <a href="/workbuddy-guide/bluebook/第二篇%20案例篇：从一项任务到一支%20AI%20团队/">
          <PixelIcon name="folder-open" /><strong>文件与远程</strong><span>整理 · 查找 · 执行</span>
        </a>
        <a href="/workbuddy-guide/bluebook/第二篇%20案例篇：从一项任务到一支%20AI%20团队/">
          <PixelIcon name="newspaper" /><strong>资讯与知识</strong><span>收集 · 筛选 · 复用</span>
        </a>
        <a href="/workbuddy-guide/bluebook/第三篇%20进阶篇：把案例变成自己的工作系统/">
          <PixelIcon name="robot" /><strong>AI 工作系统</strong><span>Skill · Agent · 自动化</span>
        </a>
      </div>
    </section>

    <section class="wb-section wb-system" aria-labelledby="wb-system-title">
      <div class="wb-system__intro">
        <p class="wb-pixel-label">FROM TASK TO TEAM</p>
        <h2 id="wb-system-title">一次成功，不该只发生一次。</h2>
        <p>本指南真正关心的不是“AI 会什么”，而是如何把一个结果沉淀成稳定、可协作、可复用的工作系统。</p>
      </div>
      <ol class="wb-system__steps">
        <li><b>01</b><strong>TASK</strong><span>完成一个真实任务</span></li>
        <li><b>02</b><strong>CASE</strong><span>复盘成可复现案例</span></li>
        <li><b>03</b><strong>WORKFLOW</strong><span>沉淀 Skill 与自动化</span></li>
        <li><b>04</b><strong>AI TEAM</strong><span>组合成协作团队</span></li>
      </ol>
    </section>

    <section class="wb-community" aria-labelledby="wb-community-title">
      <div>
        <p class="wb-pixel-label">OPEN SOURCE · 基于官方指南改写</p>
        <h2 id="wb-community-title">这本指南，也可以由你继续写下去。</h2>
      </div>
      <div class="wb-community__actions">
        <a class="wb-button wb-button--acid" href="/workbuddy-guide/attributions">版权与署名</a>
        <a class="wb-button wb-button--dark-outline" href="https://github.com/sili021yan-ai/workbuddy-guide">前往 GitHub</a>
      </div>
      <PixelIcon name="book" class="wb-community__icon" />
    </section>
  </main>
</template>
