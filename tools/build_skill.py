"""把本文件夹打包成可安装的 skill：只含 SKILL.md、README.md、workflow/、references/。

用法：python -X utf8 tools/build_skill.py [输出目录]
默认输出到 dist/top-researcher/。安装时把该目录复制到 ~/.claude/skills/top-researcher/。
"""
import shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist" / "top-researcher"
INCLUDE = ["SKILL.md", "README.md", "workflow", "references"]

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)
for name in INCLUDE:
    src = ROOT / name
    if src.is_dir():
        shutil.copytree(src, OUT / name, ignore=shutil.ignore_patterns("*.pdf", "__pycache__"))
    else:
        shutil.copy2(src, OUT / name)
n = sum(1 for p in OUT.rglob("*") if p.is_file())
print(f"built {OUT} ({n} files)")
