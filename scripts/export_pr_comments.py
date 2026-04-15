"""
Eksport komentarzy z PR-ów GitHub do plików JSON.

Użycie:
    python scripts/export_pr_comments.py
"""

import json
import subprocess
import os

REPO = "ewakaaaa/LawAsACode"
OUTPUT_DIR = "data/pr_comments"

PR_MAP = {
    3: {
        "ministerstwo": "Minister Zdrowia",
        "data_pisma": "14.06.2022",
        "dokument_zrodlowy": "dokument564010",
    },
    4: {
        "ministerstwo": "Minister Sportu i Turystyki",
        "data_pisma": "14.06.2022",
        "dokument_zrodlowy": "dokument564013",
    },
    6: {
        "ministerstwo": "Minister Rodziny i Polityki Spolecznej",
        "data_pisma": "~21.06.2022",
        "dokument_zrodlowy": "dokument563986",
    },
    7: {
        "ministerstwo": "Minister Infrastruktury",
        "data_pisma": "16.06.2022",
        "dokument_zrodlowy": "dokument564008",
    },
    9: {
        "ministerstwo": "Rzadowe Centrum Legislacji",
        "data_pisma": "19.06.2022",
        "dokument_zrodlowy": "dokument564014",
    },
    10: {
        "ministerstwo": "Minister Sprawiedliwosci",
        "data_pisma": "21.06.2022",
        "dokument_zrodlowy": "dokument564012",
    },
    11: {
        "ministerstwo": "Minister Edukacji i Nauki",
        "data_pisma": "28.06.2022",
        "dokument_zrodlowy": "dokument564005",
    },
    12: {
        "ministerstwo": "Minister ds. Unii Europejskiej",
        "data_pisma": "01.07.2022",
        "dokument_zrodlowy": "dokument564009",
    },
    13: {
        "ministerstwo": "Minister Spraw Wewnetrznych i Administracji",
        "data_pisma": "b.d.",
        "dokument_zrodlowy": "dokument564086",
    },
}


def gh_api(endpoint):
    result = subprocess.run(
        ["gh", "api", f"repos/{REPO}/{endpoint}", "--paginate"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return []
    return json.loads(result.stdout)


def export_pr(pr_number, meta):
    print(f"Eksportuję PR #{pr_number} ({meta['ministerstwo']})...")

    review_comments = gh_api(f"pulls/{pr_number}/comments")
    issue_comments = gh_api(f"issues/{pr_number}/comments")

    uwagi = []

    for rc in review_comments:
        uwagi.append(
            {
                "typ": "review_comment",
                "linia": rc.get("line") or rc.get("original_line"),
                "strona": rc.get("side", "RIGHT"),
                "sciezka": rc.get("path", ""),
                "tresc": rc.get("body", ""),
            }
        )

    for ic in issue_comments:
        uwagi.append(
            {
                "typ": "issue_comment",
                "linia": None,
                "strona": None,
                "sciezka": None,
                "tresc": ic.get("body", ""),
            }
        )

    data = {
        "pr_number": pr_number,
        "ministerstwo": meta["ministerstwo"],
        "data_pisma": meta["data_pisma"],
        "dokument_zrodlowy": meta["dokument_zrodlowy"],
        "liczba_review_comments": len(review_comments),
        "liczba_issue_comments": len(issue_comments),
        "uwagi": uwagi,
    }

    output_path = os.path.join(OUTPUT_DIR, f"{meta['dokument_zrodlowy']}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"  → {output_path} ({len(uwagi)} uwag)")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for pr_number, meta in sorted(PR_MAP.items()):
        export_pr(pr_number, meta)
    print("Gotowe!")


if __name__ == "__main__":
    main()
