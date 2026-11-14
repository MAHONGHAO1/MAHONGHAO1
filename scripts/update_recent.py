"""Rewrite the RECENT_UPDATES block in the profile README from live GitHub data.

Run by .github/workflows/update-readme.yml on a schedule. Safe to run locally:

    python scripts/update_recent.py

It only rewrites the text between the markers, so hand-written sections survive.
"""

from __future__ import annotations

import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPOS = [
    "MAHONGHAO1/Embodied-AI-Data-Processing-Platform",
    "MAHONGHAO1/AI-Fund-Management-Platform",
]
START = "<!-- RECENT_UPDATES:START -->"
END = "<!-- RECENT_UPDATES:END -->"
README = Path(__file__).resolve().parent.parent / "README.md"


def fetch(url: str, token: str | None = None) -> object:
    request = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-recent-updates",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def first_line(text: str, limit: int = 90) -> str:
    for line in (text or "").splitlines():
        line = line.strip().lstrip("#").strip()
        if line and not line.startswith("[!"):
            return line[:limit] + ("…" if len(line) > limit else "")
    return ""


def build_block(token: str | None = None) -> str:
    lines: list[str] = []
    for repo in REPOS:
        short = repo.split("/", 1)[1]
        try:
            releases = fetch(f"https://api.github.com/repos/{repo}/releases?per_page=3", token)
            commits = fetch(f"https://api.github.com/repos/{repo}/commits?per_page=3", token)
        except Exception as exc:  # 任一来源取不到就写明，不留空表
            lines.append(f"- `{short}` 取数失败：{exc}")
            continue

        if releases:
            for item in releases[:2]:
                published = (item.get("published_at") or "")[:10]
                note = first_line(item.get("body", ""))
                suffix = f" — {note}" if note else ""
                lines.append(f"- {published} · [{short} {item.get('tag_name')}]"
                             f"({item.get('html_url')}){suffix}")
        else:
            lines.append(f"- `{short}` 还没有发布过 release")

        for item in commits[:2]:
            detail = (item.get("commit") or {})
            date = (detail.get("author") or {}).get("date", "")[:10]
            message = first_line(detail.get("message", ""), 80)
            lines.append(f"  - {date} · [{message}]({item.get('html_url')})")

    lines.append("")
    lines.append(f"（{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} 自动刷新；"
                 f"刷新脚本 `scripts/update_recent.py`）")
    return "\n".join(lines)


def main() -> int:
    import os
    token = os.environ.get("GITHUB_TOKEN") or None
    block = build_block(token)
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"README 缺少标记 {START} / {END}")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    updated = pattern.sub(f"{START}\n{block}\n{END}", text, count=1)
    if updated == text:
        print("内容没有变化")
        return 0
    README.write_text(updated, encoding="utf-8")
    print(f"已更新 RECENT_UPDATES，共 {len(block.splitlines())} 行")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
