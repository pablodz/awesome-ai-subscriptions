#!/usr/bin/env python3
"""Generate README.md from data/subscriptions.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "subscriptions.json"
README_EN = ROOT / "README.md"


def load_data() -> list:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data["subscriptions"]


def fmt_price(entry: dict) -> str:
    if entry["price_monthly"] == 0:
        return "Free"
    if entry["price_annual"]:
        return f"${entry['price_monthly']}/mo<br>(${entry['price_annual']}/yr)"
    return f"${entry['price_monthly']}/mo"


def fmt_models(entry: dict) -> str:
    lines = []
    for m in entry["models"]:
        line = m["name"]
        if "context" in m and m["context"]:
            line += f" · {m['context']}"
        if "note" in m and m["note"]:
            line += f" *({m['note']})*"
        lines.append(line)
    return "<br>".join(lines)


TABLE_HEADER = "| # | Company / Product | Plan | Price/mo | Models & Context |"
TABLE_SEPARATOR = "|---|-------------------|------|----------|------------------|"


def build_rows(entries: list) -> list:
    rows = []
    for i, e in enumerate(entries, 1):
        company_product = f"**{e['company']}**<br>{e['product']}"
        plan = e["plan"]
        price = fmt_price(e)
        models = fmt_models(e)

        row = f"| {i} | {company_product} | {plan} | {price} | {models} |"
        rows.append(row)
    return rows


TEMPLATE = """# 💰 awesome-ai-subscriptions

> AI coding subscriptions compared — plans, models, and context windows at a glance.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of **AI coding subscription plans** from major providers. Compare pricing, supported models, and context windows across ChatGPT, Claude, Copilot, Cursor, Gemini Code Assist, Amazon Q, Command Code, Z.ai, Windsurf, Xiaomi MiMo, and more.

---

## 📊 The List

> Ordered by provider. Updated automatically on every push to main.

{stars_table}

---

## 📋 Template — Add a new subscription

Want to contribute? Add your entry to [`data/subscriptions.json`](data/subscriptions.json) and open a PR:

```json
{{
  "company": "Company Name",
  "product": "Product Name",
  "plan": "Plan Name",
  "price_monthly": 20,
  "price_annual": null,
  "models": [
    {{ "name": "Model A", "context": "200K" }},
    {{ "name": "Model B", "context": "128K", "note": "limited" }}
  ],
  "coding_features": ["Feature 1", "Feature 2"],
  "url": "https://example.com",
  "notes": "Optional notes"
}}
```

- `context` is the max input context window (tokens). Use `—` if unknown.
- `note` is optional — shown in *italics* inline. Use for access level, multipliers, deals.
- Only include models from the current generation (last ~year). Skip deprecated/legacy models.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details.

---

## 📐 Columns Explained

| Column | Description |
|--------|-------------|
| **Models & Context** | Current-gen coding models available in the plan, each with context window and optional note in *italics*. |

---

## 🤖 Automation

The README is generated from [`data/subscriptions.json`](data/subscriptions.json) via [`scripts/generate_readme.py`](scripts/generate_readme.py) and auto-committed on push to main by a [GitHub Action](.github/workflows/update-readme.yml).

---

## 🙌 Credits

Curated with ❤️ by the open-source community. Inspired by the [awesome](https://github.com/sindresorhus/awesome) list tradition.
"""


def main():
    entries = load_data()
    rows = build_rows(entries)
    table = "\n".join([TABLE_HEADER, TABLE_SEPARATOR] + rows)
    content = TEMPLATE.format(stars_table=table)

    with open(README_EN, "w") as f:
        f.write(content)
    print(f"✓ Generated {README_EN}")


if __name__ == "__main__":
    main()
