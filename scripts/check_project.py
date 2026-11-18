#!/usr/bin/env python3
"""Check current file/claim/reference integrity, not mathematical truth or TeX compilation."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md", "README.md", ".latexmkrc", ".vscode/settings.json", "papers/nc-p1123.tex",
    "research/plan_ja.tex", "research/notes_ja.tex", "research/indexed_z_algebra.tex", "research/BASELINE.md",
    "research/STATE.json", "research/validation.json", "computations/weighted_baseline.py",
    "computations/baseline_certificate.json", "computations/README.md", "scripts/build_bundle.py",
    
     "computations/verify_skew_ore.py", "requirements-symbolic.txt",
)


def check():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f"Missing file: {name}")
    if errors:
        return errors
    state = json.loads((ROOT / "research/STATE.json").read_text())
    validation = json.loads((ROOT / "research/validation.json").read_text())
    json.loads((ROOT / ".vscode/settings.json").read_text())
    json.loads((ROOT / "computations/baseline_certificate.json").read_text())
    if (state["date"], state["version"]) != (validation["date"], validation["version"]):
        errors.append("State/validation version mismatch")
    if state["classification_complete"] or validation["mathematics"]["complete_classification"]:
        errors.append("Initial project must not claim a complete classification")

    tex_labels = {}
    for name in ("papers/nc-p1123.tex", "research/plan_ja.tex", "research/notes_ja.tex", "research/indexed_z_algebra.tex"):
        content = (ROOT / name).read_text()
        labels = re.findall(r"\\label\{([^}]+)\}", content)
        if len(labels) != len(set(labels)):
            errors.append(f"Duplicate TeX labels in {name}")
        tex_labels[name] = set(labels)
        for ref in re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", content):
            if ref not in tex_labels[name]:
                errors.append(f"Unresolved local TeX reference {name}:{ref}")
        bibitems = set(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", content))
        for group in re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", content):
            for key in group.split(","):
                if key.strip() not in bibitems:
                    errors.append(f"Unresolved citation {name}:{key}")
        stack = []
        for action, environment in re.findall(r"\\(begin|end)\{([^}]+)\}", content):
            if action == "begin":
                stack.append(environment)
            elif not stack or stack.pop() != environment:
                errors.append(f"Mismatched TeX environment in {name}: {environment}")
        if stack:
            errors.append(f"Unclosed TeX environment in {name}: {stack}")
        if "\\author{}" not in content:
            errors.append(f"Author field not empty in {name}")

    seen = set()
    for claim in state["claims"]:
        if claim["id"] in seen:
            errors.append(f"Duplicate claim id {claim['id']}")
        seen.add(claim["id"])
        filename, _, label = claim["proof"].partition("#")
        if not (ROOT / filename).is_file():
            errors.append(f"Missing proof file {filename}")
        if label and label not in tex_labels.get(filename, set()):
            errors.append(f"Missing proof label {filename}:{label}")
    for filename in state["resume_point"]["read"]:
        if not (ROOT / filename).is_file():
            errors.append(f"Missing resume input {filename}")
    for filename in ROOT.rglob("*.md"):
        if ".git" in filename.parts:
            continue
        for target in re.findall(r"\]\(([^)]+)\)", filename.read_text()):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if not (filename.parent / path).exists():
                errors.append(f"Broken Markdown link {filename.relative_to(ROOT)}:{target}")
    return errors


if __name__ == "__main__":
    issues = check()
    if issues:
        print("\n".join(issues), file=sys.stderr)
        raise SystemExit(1)
    print("PASS: current files, TeX labels/citations/environments, claim references, and resume inputs. This is not a TeX compilation or a mathematical proof.")
