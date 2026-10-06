<template>
  <main class="wb-home">
    <!-- ================= Hero ================= -->
    <section class="wb-hero" aria-labelledby="wb-hero-title">
      <div class="wb-hero__inner">
        <div class="wb-hero__copy">
          <p class="wb-kicker">THE GUIDE · 28 CHAPTERS · 2026</p>
          <h1 id="wb-hero-title" class="wb-hero__title">
            先把 WorkBuddy<br />
            <em>用起来再说</em>
          </h1>
          <p class="wb-hero__summary">
            WorkBuddy 能干嘛？这是一套以真实工作为主线的实践路径。带你从 0 到 1
            先用起来，再从 1 到 100 把每次成功沉淀为可复用的工作系统，真正把 AI
            变成生产力。本指南为第三方非官方整理，内容基于官方指南改写。
          </p>
          <div class="wb-hero__trust">
            <span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5" /></svg>
              零基础可上手
            </span>
            <span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5" /></svg>
              每章都能验收
            </span>
            <span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5" /></svg>
              基于官方改写
            </span>
          </div>
          <div class="wb-hero__actions">
            <a class="wb-btn wb-btn--primary" href="/workbuddy-guide/bluebook/">
              开始阅读
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <a class="wb-btn wb-btn--ghost" href="/workbuddy-guide/attributions">版权与署名</a>
          </div>
        </div>

        <!-- 明信片 -->
        <div class="wb-postcard" aria-label="指南概览">
          <div class="wb-postcard__glow" aria-hidden="true" />
          <figure>
            <div class="wb-postcard__scene">
              <!-- 自绘：终端 + 任务卡流 -->
              <svg viewBox="0 0 400 300" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%">
                <defs>
                  <linearGradient id="wbSky" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#f6d9c4" />
                    <stop offset="42%" stop-color="#e8a878" />
                    <stop offset="100%" stop-color="#8a4a2c" />
                  </linearGradient>
                </defs>
                <rect width="400" height="300" fill="url(#wbSky)" />
                <circle class="wb-float" cx="300" cy="72" r="34" fill="#fff3e0" opacity="0.75" />
                <circle class="wb-float-slow" cx="86" cy="188" r="12" fill="#fff3e0" opacity="0.35" />
                <!-- 远山 -->
                <path d="M0,214 L64,168 L128,210 L196,160 L262,206 L330,172 L400,204 L400,300 L0,300 Z" fill="#a2593a" opacity="0.55" />
                <!-- 终端窗口 -->
                <g>
                  <rect x="46" y="52" width="230" height="150" fill="#2a2018" opacity="0.94" />
                  <rect x="46" y="52" width="230" height="22" fill="#c2571b" />
                  <circle cx="60" cy="63" r="3.4" fill="#f6f1e7" opacity="0.85" />
                  <circle cx="72" cy="63" r="3.4" fill="#f6f1e7" opacity="0.55" />
                  <circle cx="84" cy="63" r="3.4" fill="#f6f1e7" opacity="0.35" />
                  <g font-family="monospace" font-size="9.5" fill="#f6f1e7">
                    <text x="60" y="94" opacity="0.55">$ workbuddy run</text>
                    <text x="60" y="112" opacity="0.9">▸ 读取任务清单</text>
                    <text x="60" y="130" opacity="0.9">▸ 调用 Skill ×3</text>
                    <text x="60" y="148" opacity="0.9">▸ 汇总为报告</text>
                    <text x="60" y="172" fill="#e08b4c">✓ 任务完成 · 2.4s</text>
                  </g>
                  <rect class="wb-float-slow" x="252" y="118" width="104" height="12" fill="#e08b4c" opacity="0.75" />
                  <rect x="252" y="140" width="82" height="12" fill="#f6f1e7" opacity="0.4" />
                </g>
                <!-- 悬浮卡片 -->
                <g>
                  <rect class="wb-float" x="240" y="196" width="126" height="58" fill="#fbf8f1" opacity="0.95" />
                  <rect x="252" y="208" width="42" height="7" fill="#c2571b" />
                  <rect x="252" y="222" width="98" height="6" fill="#2a2018" opacity="0.3" />
                  <rect x="252" y="234" width="72" height="6" fill="#2a2018" opacity="0.18" />
                </g>
                <!-- 地面 -->
                <path d="M0,268 L400,258 L400,300 L0,300 Z" fill="#6b3a22" />
              </svg>
              <span class="wb-postcard__coords">22.54 N / 114.05 E</span>
            </div>
            <figcaption class="wb-postcard__cap">
              <div>
                <h2>第一章 · 初识 WorkBuddy</h2>
                <p>从装好到跑通第一个任务</p>
              </div>
              <div class="wb-postcard__price">
                <b>28</b>
                <span>chapters</span>
              </div>
            </figcaption>
          </figure>
        </div>
      </div>

      <!-- 价值条 -->
      <div class="wb-values" aria-label="指南价值">
        <div class="wb-value">
          <span class="wb-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5" /></svg></span>
          <span><b>真实任务</b><small>REAL TASKS</small></span>
        </div>
        <div class="wb-value">
          <span class="wb-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7M21 4v5h-5" /></svg></span>
          <span><b>可复现</b><small>REPRODUCIBLE</small></span>
        </div>
        <div class="wb-value">
          <span class="wb-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l2.4 7.4H22l-6 4.4 2.3 7.2L12 17l-6.3 4 2.3-7.2-6-4.4h7.6z" /></svg></span>
          <span><b>官方改写</b><small>OFFICIAL-BASED</small></span>
        </div>
        <div class="wb-value">
          <span class="wb-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1" /><rect x="14" y="3" width="7" height="7" rx="1" /><rect x="3" y="14" width="7" height="7" rx="1" /><rect x="14" y="14" width="7" height="7" rx="1" /></svg></span>
          <span><b>系统沉淀</b><small>WORK SYSTEM</small></span>
        </div>
      </div>
    </section>

    <!-- ================= 阅读路径 ================= -->
    <section aria-labelledby="wb-reading-title">
      <div class="wb-section__head">
        <p class="wb-kicker">01 / READING PATH</p>
        <h2 id="wb-reading-title">四段路径，<em>按你的目标进入</em></h2>
        <p>从个人上手到组织落地，循序渐进，构建属于你的 WorkBuddy 工作系统。</p>
      </div>

      <div class="wb-cards">
        <a class="wb-card" href="/workbuddy-guide/bluebook/第一篇%20使用手册：先把%20WorkBuddy%20用起来/">
          <div class="wb-card__top">
            <span class="wb-card__no">01</span>
            <span class="wb-card__ch">CH. 01—11</span>
          </div>
          <div class="wb-card__body">
            <strong>从 0 到 1：先把 WorkBuddy 用起来</strong>
            <span>安装、界面、第一个任务、Skill、连接器、API 与自动化。</span>
            <div class="wb-card__foot">
              <span class="wb-card__tags"><em>新手推荐</em><em>先完成一项任务</em></span>
              <span class="wb-card__go">进入
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M9 7h8v8" /></svg>
              </span>
            </div>
          </div>
        </a>

        <a class="wb-card" href="/workbuddy-guide/bluebook/第二篇%20案例篇：从一项任务到一支%20AI%20团队/">
          <div class="wb-card__top">
            <span class="wb-card__no">02</span>
            <span class="wb-card__ch">CH. 12—22</span>
          </div>
          <div class="wb-card__body">
            <strong>进入真实案例：让任务开始流动</strong>
            <span>办公、文件、远程、资讯、知识、会议、投资和内容增长。</span>
            <div class="wb-card__foot">
              <span class="wb-card__tags"><em>11 个案例</em><em>任务驱动</em></span>
              <span class="wb-card__go">进入
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M9 7h8v8" /></svg>
              </span>
            </div>
          </div>
        </a>

        <a class="wb-card" href="/workbuddy-guide/bluebook/第三篇%20进阶篇：把案例变成自己的工作系统/">
          <div class="wb-card__top">
            <span class="wb-card__no">03</span>
            <span class="wb-card__ch">CH. 23—26</span>
          </div>
          <div class="wb-card__body">
            <strong>把案例变成可复用的工作系统</strong>
            <span>打造 Skill、多 Agent 系统设计与可靠的自动化工作流。</span>
            <div class="wb-card__foot">
              <span class="wb-card__tags"><em>系统进阶</em><em>可靠自动化</em></span>
              <span class="wb-card__go">进入
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M9 7h8v8" /></svg>
              </span>
            </div>
          </div>
        </a>

        <a class="wb-card" href="/workbuddy-guide/bluebook/第四篇%20岗位与行业落地/">
          <div class="wb-card__top">
            <span class="wb-card__no">04</span>
            <span class="wb-card__ch">CH. 27—28</span>
          </div>
          <div class="wb-card__body">
            <strong>落到岗位与行业，组建 AI 团队</strong>
            <span>从通用能力出发，设计适合不同岗位和行业的工作流。</span>
            <div class="wb-card__foot">
              <span class="wb-card__tags"><em>团队落地</em><em>行业路线</em></span>
              <span class="wb-card__go">进入
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M9 7h8v8" /></svg>
              </span>
            </div>
          </div>
        </a>
      </div>
    </section>

    <!-- ================= 任务入口 ================= -->
    <section aria-labelledby="wb-task-title">
      <div class="wb-section__head">
        <p class="wb-kicker">02 / START WITH A REAL TASK</p>
        <h2 id="wb-task-title">你现在想让 AI <em>帮你做什么？</em></h2>
        <p>不必从头读。带着问题进来，先跑通一个能验收的结果。</p>
      </div>

      <div class="wb-tasks">
        <a class="wb-task" href="/workbuddy-guide/bluebook/第二篇%20案例篇：从一项任务到一支%20AI%20团队/">
          <span class="wb-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="2" /><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" /></svg></span>
          <strong>办公文档</strong><span>Word · Excel · PPT</span>
        </a>
        <a class="wb-task" href="/workbuddy-guide/bluebook/第二篇%20案例篇：从一项任务到一支%20AI%20团队/">
          <span class="wb-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" /></svg></span>
          <strong>文件与远程</strong><span>整理 · 查找 · 执行</span>
        </a>
        <a class="wb-task" href="/workbuddy-guide/bluebook/第二篇%20案例篇：从一项任务到一支%20AI%20团队/">
          <span class="wb-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16v14H4z" /><path d="M8 9h8M8 13h5" /></svg></span>
          <strong>资讯与知识</strong><span>收集 · 筛选 · 复用</span>
        </a>
        <a class="wb-task" href="/workbuddy-guide/bluebook/第三篇%20进阶篇：把案例变成自己的工作系统/">
          <span class="wb-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="7" width="14" height="12" rx="2" /><path d="M12 7V4M9 13h.01M15 13h.01M9 16h6" /></svg></span>
          <strong>AI 工作系统</strong><span>Skill · Agent · 自动化</span>
        </a>
      </div>
    </section>

    <!-- ================= 四步路线图 ================= -->
    <section class="wb-system" aria-labelledby="wb-system-title">
      <div>
        <p class="wb-kicker">03 / FROM TASK TO TEAM</p>
        <div class="wb-system__head">
          <h2 id="wb-system-title">一次成功，<em>不该只发生一次。</em></h2>
          <p>
            本指南真正关心的不是「AI 会什么」，而是如何把一个结果沉淀成稳定、可协作、可复用的工作系统。
          </p>
        </div>

        <!-- 路线图 -->
        <div class="wb-map">
          <div class="wb-map__bar">
            <span>PROGRESS MAP</span>
            <span><i class="wb-map__dot" />4 STAGES OPEN</span>
          </div>
          <svg viewBox="0 0 800 300" role="img" aria-label="从任务到团队的四阶段路线图">
            <!-- 同心圆 -->
            <circle cx="400" cy="150" r="72" fill="none" stroke="#f6f1e7" stroke-opacity="0.1" />
            <circle cx="400" cy="150" r="124" fill="none" stroke="#f6f1e7" stroke-opacity="0.06" />
            <!-- 基准线 -->
            <line x1="60" y1="150" x2="740" y2="150" stroke="#f6f1e7" stroke-opacity="0.08" stroke-dasharray="2 8" />

            <!-- 四条弧线 -->
            <path class="wb-flow" d="M400,150 Q340,66 268,84" fill="none" stroke="#e08b4c" stroke-width="1.6" />
            <path class="wb-flow" d="M400,150 Q462,62 540,92" fill="none" stroke="#e08b4c" stroke-width="1.6" />
            <path class="wb-flow" d="M400,150 Q336,236 262,214" fill="none" stroke="#e08b4c" stroke-width="1.6" />
            <path class="wb-flow" d="M400,150 Q466,232 546,206" fill="none" stroke="#e08b4c" stroke-width="1.6" />

            <!-- 四个节点 -->
            <g>
              <circle cx="268" cy="84" r="14" fill="#c2571b" fill-opacity="0.2" />
              <circle cx="268" cy="84" r="5" fill="#e08b4c" />
              <text x="268" y="58" text-anchor="middle" font-family="monospace" font-size="13" fill="#f6f1e7" fill-opacity="0.75">01</text>
            </g>
            <g>
              <circle cx="540" cy="92" r="14" fill="#c2571b" fill-opacity="0.2" />
              <circle cx="540" cy="92" r="5" fill="#e08b4c" />
              <text x="540" y="66" text-anchor="middle" font-family="monospace" font-size="13" fill="#f6f1e7" fill-opacity="0.75">02</text>
            </g>
            <g>
              <circle cx="262" cy="214" r="14" fill="#c2571b" fill-opacity="0.2" />
              <circle cx="262" cy="214" r="5" fill="#e08b4c" />
              <text x="262" y="242" text-anchor="middle" font-family="monospace" font-size="13" fill="#f6f1e7" fill-opacity="0.75">03</text>
            </g>
            <g>
              <circle cx="546" cy="206" r="14" fill="#c2571b" fill-opacity="0.2" />
              <circle cx="546" cy="206" r="5" fill="#e08b4c" />
              <text x="546" y="234" text-anchor="middle" font-family="monospace" font-size="13" fill="#f6f1e7" fill-opacity="0.75">04</text>
            </g>

            <!-- 中心枢纽 -->
            <circle cx="400" cy="150" r="6" fill="#f6f1e7" />
            <circle cx="400" cy="150" r="13" fill="none" stroke="#f6f1e7" stroke-opacity="0.4" />
            <text x="400" y="182" text-anchor="middle" font-family="monospace" font-size="13" fill="#f6f1e7">RESULT</text>
          </svg>
        </div>

        <div class="wb-steps">
          <div class="wb-step"><b>01</b><strong>TASK</strong><span>完成一个真实任务</span></div>
          <div class="wb-step"><b>02</b><strong>CASE</strong><span>复盘成可复现案例</span></div>
          <div class="wb-step"><b>03</b><strong>WORKFLOW</strong><span>沉淀 Skill 与自动化</span></div>
          <div class="wb-step"><b>04</b><strong>AI TEAM</strong><span>组合成协作团队</span></div>
        </div>
      </div>
    </section>

    <!-- ================= 支持 / 跟进 ================= -->
    <section aria-labelledby="wb-cta-title">
      <div class="wb-news">
        <div>
          <p class="wb-kicker">OPEN SOURCE</p>
          <h2 id="wb-cta-title">这本指南，<em>也可以由你继续写下去。</em></h2>
          <p>
            内容基于官方指南改写，遵循开放协作精神。仓库每周监测官方文档变更，发现差异会自动开 Issue；
            版权勘误、内容补充都可以提 PR。
          </p>
        </div>
        <div class="wb-news__actions">
          <a
            class="wb-news__btn wb-news__btn--solid"
            href="https://github.com/sil1021yan-ai/workbuddy-guide"
            target="_blank"
            rel="noreferrer"
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.6 5.3 5.9.9-4.2 4.1 1 5.8-5.3-2.8-5.3 2.8 1-5.8L3.5 9.2l5.9-.9z" /></svg>
            Star 仓库
          </a>
          <a
            class="wb-news__btn"
            href="https://github.com/sil1021yan-ai/workbuddy-guide/stargazers"
            target="_blank"
            rel="noreferrer"
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12z" /><circle cx="12" cy="12" r="2.8" /></svg>
            Watch 更新
          </a>
          <p class="wb-news__note">
            Star 或 Watch 后，仓库有新提交与新 Issue 时你会收到 GitHub 通知。
          </p>
        </div>
      </div>
    </section>
  </main>
</template>
