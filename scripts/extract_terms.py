"""抽取全站「小白说明书」段落为结构化 JSON。

- 第一篇 11 章：术语解释型（**术语**\\n释义 / > **术语**：释义）
- 第 23/26 章：操作要点型（> - 要点）
输出：paid-content/_feishu/terms.json
"""
import re, pathlib, json, collections

BASE = pathlib.Path("C:/Users/47910/Documents/Yan_Project/codexproject/knowledgebuilding/workbuddy-guide")
P1 = "第一篇 使用手册：先把 WorkBuddy 用起来"

HEADER = re.compile(r"^##\s*(?:[一二三四五六七]、)?小白说明书\s*$", re.M)
NEXT_H2 = re.compile(r"^##\s", re.M)

# 术语解释型：`**术语**` 独占一行，下一段是释义
ENTRY_BOLD = re.compile(r"^\*\*(.+?)\*\*\s*$")
# 术语解释型：引用块内 `> **术语**：释义`
ENTRY_QUOTE = re.compile(r"^>\s*\*\*(.+?)\*\*\s*[:：]\s*(.+)$")
# 操作要点型：引用块内 `> - 要点`
TIP_QUOTE = re.compile(r"^>\s*-\s+(.+)$")


def strip_md(s: str) -> str:
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return re.sub(r"\s+", " ", s).strip()


def extract(path: pathlib.Path):
    t = path.read_text(encoding="utf-8")
    m = HEADER.search(t)
    if not m:
        return None
    seg = t[m.end():]
    nxt = NEXT_H2.search(seg)
    if nxt:
        seg = seg[:nxt.start()]

    terms, tips = [], []
    lines = seg.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        # 引用块格式：术语 + 同行释义
        mq = ENTRY_QUOTE.match(ln)
        if mq:
            body = mq.group(2).strip()
            # 释义可能跨行（续行也是 > 开头）
            j = i + 1
            while j < len(lines) and re.match(r"^>\s+\S", lines[j]) and not ENTRY_QUOTE.match(lines[j]):
                body += " " + lines[j].lstrip("> ").strip()
                j += 1
            terms.append({"term": mq.group(1).strip(), "def": strip_md(body)})
            i = j
            continue
        # 引用块格式：操作要点
        mt = TIP_QUOTE.match(ln)
        if mt:
            tips.append(strip_md(mt.group(1)))
            i += 1
            continue
        # 独占一行格式：**术语** + 后续缩进段落
        mb = ENTRY_BOLD.match(ln)
        if mb:
            body_parts = []
            j = i + 1
            while j < len(lines) and lines[j].strip() and not ENTRY_BOLD.match(lines[j]) \
                    and not lines[j].startswith("**") and not lines[j].startswith("##"):
                body_parts.append(lines[j].strip())
                j += 1
            body = " ".join(body_parts)
            if body:
                terms.append({"term": mb.group(1).strip(), "def": strip_md(body)})
            i = j
            continue
        i += 1

    chap = path.parent.name
    return {"chapter": chap, "part": "第一篇" if P1 in str(path) else "其他",
            "terms": terms, "tips": tips}


files = sorted(BASE.glob("docs/bluebook/第一篇*/*/index.md"))
out = {"part1": [], "other": []}
for f in files:
    r = extract(f)
    if not r:
        print("[skip]", f.name)
        continue
    out["part1"].append(r)
    print(f"[part1] {r['chapter']}: {len(r['terms'])} 术语, {len(r['tips'])} 要点")

# 第 23/26 章操作要点
for pat in ["paid-content/第三篇-完整版/第 23 章*/index.md", "paid-content/第四篇-完整版/第 26 章*/index.md"]:
    for f in BASE.glob(pat):
        r = extract(f)
        if r:
            out["other"].append({"chapter": r["chapter"], "tips": r["tips"]})
            print(f"[tips ] {r['chapter']}: {len(r['tips'])} 要点")

all_terms = [t for c in out["part1"] for t in c["terms"]]
print(f"\n第一篇术语总数: {len(all_terms)}   唯一: {len({t['term'] for t in all_terms})}")

(BASE / "paid-content" / "_feishu").mkdir(parents=True, exist_ok=True)
(BASE / "paid-content" / "_feishu" / "terms.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("-> paid-content/_feishu/terms.json")

print("\n=== 第一篇全部术语清单 ===")
for t in all_terms:
    print(f"- {t['term']} :: {t['def'][:60]}")