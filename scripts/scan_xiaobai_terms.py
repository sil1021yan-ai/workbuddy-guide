import re, pathlib, collections, json

BASE = pathlib.Path("C:/Users/47910/Documents/Yan_Project/codexproject/knowledgebuilding/workbuddy-guide")

files = []
for pat in ["docs/bluebook/*/*/index.md", "paid-content/*/*/index.md"]:
    files += list(BASE.glob(pat))

ENTRY = re.compile(r"^\*\*(.+?)\*\*\s*$", re.M)
# 第二/三/四篇多用引用块格式：> **术语**：解释
ENTRY_QUOTE = re.compile(r"^>\s*\*\*(.+?)\*\*\s*[:：]", re.M)
HEADER = re.compile(r"^##\s*小白说明书\s*$", re.M)
NEXT_H2 = re.compile(r"^##\s", re.M)

rows = []
counter = collections.Counter()
detail = {}

for p in sorted(set(files)):
    t = p.read_text(encoding="utf-8")
    m = HEADER.search(t)
    if not m:
        continue
    seg = t[m.end():]
    nxt = NEXT_H2.search(seg)
    if nxt:
        seg = seg[:nxt.start()]
    terms = [re.sub(r"[`*]", "", x).strip() for x in ENTRY.findall(seg)]
    quoted = [re.sub(r"[`*]", "", x).strip() for x in ENTRY_QUOTE.findall(seg)]
    seen = set(terms)
    terms += [x for x in quoted if x not in seen and not seen.add(x)]
    rel = str(p.relative_to(BASE)).replace("\\", "/")
    rows.append((rel, len(terms)))
    detail[rel] = terms
    for x in terms:
        counter[x] += 1

print("=== 各章小白说明书条目数 ===")
for r, n in rows:
    print(f"{n:>3}  {r}")

total = sum(n for _, n in rows)
print(f"\n章节数: {len(rows)}   总条目(含重复): {total}   唯一术语: {len(counter)}")

dups = {k: v for k, v in counter.items() if v >= 2}
print(f"\n重复术语数(>=2次): {len(dups)}  涉及条目: {sum(dups.values())}")
print("\n=== 重复术语明细 ===")
for k, v in sorted(dups.items(), key=lambda x: (-x[1], x[0])):
    print(f"{v}x  {k}")

(BASE / "scripts" / "_xiaobai_terms.json").write_text(
    json.dumps({"detail": detail, "counter": counter}, ensure_ascii=False, indent=1),
    encoding="utf-8")
print("\n-> scripts/_xiaobai_terms.json")