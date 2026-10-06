// monitor/check.mjs
// 每周抓取官方 docs 页面 → 与本地快照 diff → 有变化用 gh 自动开 Issue。
// 运行环境：GitHub Actions（自带 gh CLI 与 GITHUB_TOKEN）。
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { execSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const SNAP_DIR = path.join(root, 'monitor', 'snapshots');
const TARGETS_FILE = path.join(root, 'monitor', 'targets.json');
const GH_REPO = process.env.GH_REPO;

function slug(url) {
  return url.replace(/[^a-z0-9]/gi, '_').slice(-90);
}

async function fetchText(url) {
  const res = await fetch(url, { headers: { 'User-Agent': 'workbuddy-guide-monitor/1.0' } });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const html = await res.text();
  // 提取 VitePress 正文容器（vp-doc），失败则退而取 <main>
  const m = html.match(/<main[\s\S]*?vp-doc[\s\S]*?<\/main>/i) || html.match(/<main[\s\S]*?<\/main>/i);
  const region = m ? m[0] : html;
  return region
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<[^>]+>/g, '\n')
    .replace(/&[a-z#0-9]+;/gi, ' ')
    .replace(/[ \t]+/g, ' ')
    .split('\n')
    .map((s) => s.trim())
    .filter(Boolean)
    .join('\n');
}

async function createIssue(change) {
  const title = `[官方变更·${change.type}] ${change.title}`;
  const body =
    `## 监控目标\n${change.url}\n\n` +
    `## 变化类型\n${change.type}\n\n` +
    (change.error ? `## 抓取错误\n${change.error}\n\n` : '') +
    `## 待办\n` +
    `1. 打开上方官方页面，对比本教程对应章节。\n` +
    `2. 将官方变化改写成「小白可完成的任务路径」。\n` +
    `3. 更新教程后提交 PR，合并即自动发布。\n\n` +
    `> 请在此粘贴：官方原文摘录 + 你的改写草稿`;
  try {
    execSync(
      `gh issue create --repo "${GH_REPO}" --title ${JSON.stringify(title)} --body ${JSON.stringify(body)} --label monitor`,
      { stdio: 'inherit' }
    );
    console.log('issue created:', title);
  } catch (e) {
    console.error('failed to create issue:', e.message);
  }
}

async function main() {
  const targets = JSON.parse(await readFile(TARGETS_FILE, 'utf8'));
  await mkdir(SNAP_DIR, { recursive: true });
  const changes = [];
  for (const t of targets) {
    let current;
    try {
      current = await fetchText(t.url);
    } catch (e) {
      changes.push({ type: 'UNREACHABLE', url: t.url, title: t.title, error: String(e.message) });
      continue;
    }
    const snapFile = path.join(SNAP_DIR, slug(t.url) + '.txt');
    let previous = '';
    try { previous = await readFile(snapFile, 'utf8'); } catch {}
    if (previous === current) {
      console.log('no change:', t.title);
      continue;
    }
    await writeFile(snapFile, current);
    changes.push({ type: previous ? 'MODIFIED' : 'NEW', url: t.url, title: t.title });
  }

  for (const c of changes) await createIssue(c);

  if (changes.length) {
    try {
      execSync(
        `git add -A monitor/snapshots && git -c user.email="bot@workbuddy-guide" -c user.name="monitor" commit -m "chore: update monitor snapshots" && git push`,
        { stdio: 'inherit' }
      );
    } catch (e) {
      console.error('commit snapshots failed:', e.message);
    }
  }
  console.log(`monitor done. changes=${changes.length}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
