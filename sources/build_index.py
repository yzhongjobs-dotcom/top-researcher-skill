"""Build a deduplicated index of candidate papers across the local source folders."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOTS = [
    Path(r"D:\桌面\正文writing skill\文献资料"),
    Path(r"D:\桌面\科研Agent Harness设计\impedance-control-e2e\source-materials"),
    Path(r"E:\github_project\scan-impedance-update\literature"),
    HERE / "pdfs",
]
CITATIONS = Path(r"D:\桌面\科研Agent Harness设计\impedance-control-e2e\FULLTEXT_DOWNLOAD_BATCH_V2.md")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def load_citations():
    out = {}
    if not CITATIONS.exists():
        return out
    pat = re.compile(r"\*\*(.+?)\*\* — (.*?)\((\d{4}), (.*?)\).*?citations at retrieval: (\d+)")
    for line in CITATIONS.read_text(encoding="utf-8").splitlines():
        m = pat.search(line)
        if m:
            title, authors, year, venue, cites = m.groups()
            out[norm(title)] = {"title": title, "authors": authors.strip(), "year": int(year),
                                "venue": venue, "citations_at_retrieval": int(cites)}
    return out


def main():
    cites = load_citations()
    entries = {}
    for root in ROOTS:
        if not root.exists():
            continue
        for pdf in root.rglob("*"):
            if pdf.suffix.lower() != ".pdf" or not pdf.is_file():
                continue
            data = pdf.read_bytes()
            if not data.startswith(b"%PDF"):
                continue
            h = hashlib.sha256(data).hexdigest()
            e = entries.setdefault(h, {"sha256": h, "filename": pdf.name, "paths": []})
            e["paths"].append(str(pdf))
    for e in entries.values():
        key = norm(Path(e["filename"]).stem.replace("_", " "))
        for k, v in cites.items():
            if k and (k in key or key in k):
                e["citation_record"] = v
                break
    rows = sorted(entries.values(), key=lambda e: e["filename"].lower())
    (HERE / "index.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    matched = sum("citation_record" in e for e in rows)
    print(f"{len(rows)} unique PDFs, {matched} with citation records")


if __name__ == "__main__":
    main()
