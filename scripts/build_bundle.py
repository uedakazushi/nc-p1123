#!/usr/bin/env python3
"""Package only the current, committed research sources and regenerated PDFs.

No Git history, external-paper PDFs, logs, caches or old bundles are included.
Run after verification and a clean source commit.  This does not upload files.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import datetime as dt
import json
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PDFS = ("plan_ja.pdf", "nc-p1123.pdf", "notes_ja.pdf",
        "weighted_ore_strata.pdf", "graded_ore_classification.pdf")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT).decode().strip()


def build(source_only=False):
    if git("status", "--porcelain", "--untracked-files=no"):
        raise SystemExit("Commit the verified current source before packaging; tracked changes remain.")
    state = json.loads((ROOT / "research/STATE.json").read_text())
    paths = [p for p in git("ls-files", "-z").split("\0") if p]
    if not source_only:
        for name in PDFS:
            if not (ROOT / name).is_file():
                raise SystemExit(f"Missing current PDF: {name}. Compile first or explicitly use --source-only.")
        paths.extend(PDFS)
    paths = sorted(set(paths))
    payloads = {}
    for name in paths:
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise SystemExit(f"Unsupported/missing source: {name}")
        if any(part in {".git", "build", "tmp", "__pycache__", "output"} for part in path.relative_to(ROOT).parts):
            raise SystemExit(f"Generated/history path must not be tracked: {name}")
        if path.suffix in {".zip", ".log", ".aux"}:
            raise SystemExit(f"Archive/intermediate must not be tracked: {name}")
        payloads[name] = path.read_bytes()
    manifest = {
        "project": state["project"], "date": state["date"], "version": state["version"],
        "source_commit": git("rev-parse", "HEAD"), "source_tree": git("rev-parse", "HEAD^{tree}"),
        "read_first": "research/plan_ja.tex",
        "pdfs_included": not source_only,
        "scope": "Current research only. Source generation, mathematical checks, typesetting and remote saving have separate statuses in research/validation.json.",
        "files": {name: {"bytes": len(data), "sha256": sha256(data).hexdigest()}
                  for name, data in payloads.items()},
    }
    payloads["BUNDLE.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    date = dt.date.fromisoformat(state["date"])
    target = ROOT / "output" / f"nc-p1123-{state['date']}-v{state['version']}.zip"
    target.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payloads.items()):
            info = zipfile.ZipInfo("nc-p1123/" + name, (date.year, date.month, date.day, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise SystemExit("ZIP CRC check failed")
        for name, data in payloads.items():
            if archive.read("nc-p1123/" + name) != data:
                raise SystemExit(f"ZIP byte mismatch: {name}")
    print(json.dumps({"file": str(target), "entries": len(payloads),
                      "bytes": target.stat().st_size, "pdfs_included": not source_only,
                      "crc_and_content_verified": True}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-only", action="store_true", help="Explicitly omit all PDFs.")
    build(parser.parse_args().source_only)
