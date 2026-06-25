#!/usr/bin/env python3
"""Generate README.md and README.es.md from data/subscriptions.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "subscriptions.json"
README_EN = ROOT / "README.md"
README_ES = ROOT / "README.es.md"


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


def fmt_price_val(v: float) -> str:
    """Format a dollar price, using more decimals if under $0.10."""
    if v < 0.10:
        return f"${v:.4f}".rstrip("0").rstrip(".")
    return f"${v:.2f}"


def fmt_pricing(entry: dict) -> str:
    """Format per-token pricing for models that have it."""
    lines = []
    for m in entry["models"]:
        has_pricing = any(k in m for k in ("input_price", "output_price", "cache_price"))
        if not has_pricing:
            continue
        parts = [m["name"]]
        prices = []
        if "input_price" in m:
            prices.append(f"in {fmt_price_val(m['input_price'])}")
        if "cache_price" in m:
            prices.append(f"cache {fmt_price_val(m['cache_price'])}")
        if "output_price" in m:
            prices.append(f"out {fmt_price_val(m['output_price'])}")
        if prices:
            parts.append(" · ".join(prices))
        lines.append(" · ".join(parts))
    if not lines:
        return "included in plan"
    return "<br>".join(lines)


TABLE_HEADER_EN = "| # | Company / Product | Plan | Price/mo | Models & Context | Token Pricing ($/1M) |"
TABLE_SEPARATOR = "|---|-------------------|------|----------|------------------|---------------------|"

TABLE_HEADER_ES = "| # | Empresa / Producto | Plan | Precio/mes | Modelos y Contexto | Precio por Token ($/1M) |"


def build_rows(entries: list, lang: str) -> list:
    rows = []
    for i, e in enumerate(entries, 1):
        company_product = f"**{e['company']}**<br>{e['product']}"
        plan = e["plan"]
        price = fmt_price(e)
        models = fmt_models(e)
        pricing = fmt_pricing(e)

        row = f"| {i} | {company_product} | {plan} | {price} | {models} | {pricing} |"
        rows.append(row)
    return rows


TABLE_HEADERS = {
    "en": TABLE_HEADER_EN,
    "es": TABLE_HEADER_ES,
}

TEMPLATES = {
    "en": """# 💰 awesome-ai-subscriptions

> AI coding subscriptions compared — plans, models, context windows, and per-token pricing.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of **AI coding subscription plans** from major providers. Compare pricing, supported models, context windows, and per-token costs across ChatGPT, Claude, Copilot, Cursor, Gemini Code Assist, Amazon Q, Command Code, Z.ai, Windsurf, Xiaomi MiMo, and more.

📖 [Versión en español →](README.es.md)

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
    {{ "name": "Model A", "context": "200K", "input_price": 3.00, "output_price": 15.00 }},
    {{ "name": "Model B", "context": "128K" }}
  ],
  "coding_features": ["Feature 1", "Feature 2"],
  "url": "https://example.com",
  "notes": "Optional notes"
}}
```

- `input_price` / `output_price` / `cache_price` are **per 1M tokens** in USD. Omit for subscription plans where per-token pricing isn't exposed (the column will show "included in plan").
- Only include models from the current generation (last ~year). Skip deprecated/legacy models.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details.

---

## 📐 Columns Explained

| Column | Description |
|--------|-------------|
| **Models & Context** | Current-gen coding models and their context window (max input tokens). Notes in *italics*. |
| **Token Pricing ($/1M)** | Per-token cost at API rates: input / cache read / output per 1M tokens. Shows "included in plan" for subscription-only plans. |

---

## 🏷️ Pricing Notes

- **Subscription plans** (ChatGPT Plus/Pro, Claude Pro/Max, Copilot, Cursor) include model access in the monthly fee. Per-token pricing shown is the underlying API rate where applicable.
- **Credit-based plans** (Command Code) charge per token at model-specific rates, drawn from a monthly credit pool. Deals (e.g., "4× usage") mean every $1 of credit goes 4× further on that model.
- **Prompt-based plans** (Z.ai) meter by prompt count, not tokens. Per-token rates are reference API prices.
- **API-only** (Xiaomi MiMo) charge per token with no subscription, or offer open-weight models for free self-hosting.
- Prices are in USD. Verify on official pricing pages — rates change frequently.

---

## 🤖 Automation

The README is generated from [`data/subscriptions.json`](data/subscriptions.json) via [`scripts/generate_readme.py`](scripts/generate_readme.py) and auto-committed on push to main by a [GitHub Action](.github/workflows/update-readme.yml).

---

## 🌍 Multi-language

| Language | File |
|----------|------|
| English  | [`README.md`](README.md) |
| Español  | [`README.es.md`](README.es.md) |

---

## 🙌 Credits

Curated with ❤️ by the open-source community. Inspired by the [awesome](https://github.com/sindresorhus/awesome) list tradition.
""",
    "es": """# 💰 awesome-ai-subscriptions

> Suscripciones de IA para programar comparadas — planes, modelos, ventanas de contexto y precio por token.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

Una lista curada de **planes de suscripción de IA para programar** de los principales proveedores. Compara precios, modelos soportados, ventanas de contexto y costos por token entre ChatGPT, Claude, Copilot, Cursor, Gemini Code Assist, Amazon Q, Command Code, Z.ai, Windsurf, Xiaomi MiMo y más.

📖 [English version →](README.md)

---

## 📊 La Lista

> Ordenada por proveedor. Actualizada automáticamente en cada push a main.

{stars_table}

---

## 📋 Plantilla — Añadir una nueva suscripción

¿Quieres contribuir? Añade tu entrada en [`data/subscriptions.json`](data/subscriptions.json) y abre un PR:

```json
{{
  "company": "Nombre Empresa",
  "product": "Nombre Producto",
  "plan": "Nombre Plan",
  "price_monthly": 20,
  "price_annual": null,
  "models": [
    {{ "name": "Modelo A", "context": "200K", "input_price": 3.00, "output_price": 15.00 }},
    {{ "name": "Modelo B", "context": "128K" }}
  ],
  "coding_features": ["Función 1", "Función 2"],
  "url": "https://example.com",
  "notes": "Notas opcionales"
}}
```

- `input_price` / `output_price` / `cache_price` son **por 1M tokens** en USD. Omite para planes de suscripción sin precio por token (la columna mostrará "incluido en el plan").
- Solo incluye modelos de la generación actual (~último año). Omite modelos obsoletos/legacy.

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

---

## 📐 Columnas Explicadas

| Columna | Descripción |
|---------|-------------|
| **Modelos y Contexto** | Modelos de código de generación actual y su ventana de contexto (tokens máx. de entrada). Notas en *cursiva*. |
| **Precio por Token ($/1M)** | Costo por token a tarifas de API: entrada / caché / salida por 1M tokens. Muestra "incluido en el plan" para suscripciones sin precio por token. |

---

## 🏷️ Notas de Precios

- **Planes de suscripción** (ChatGPT Plus/Pro, Claude Pro/Max, Copilot, Cursor) incluyen acceso a modelos en la tarifa mensual. El precio por token mostrado es la tarifa API subyacente cuando aplica.
- **Planes por créditos** (Command Code) cobran por token a tarifas específicas del modelo, consumidas de un pool mensual. Ofertas (ej. "4× uso") significan que cada $1 de crédito rinde 4× más en ese modelo.
- **Planes por prompts** (Z.ai) miden por cantidad de prompts, no por tokens. Las tarifas por token son precios API de referencia.
- **Solo API** (Xiaomi MiMo) cobran por token sin suscripción, u ofrecen modelos open-weight para self-hosting gratuito.
- Precios en USD. Verifica en las páginas oficiales — las tarifas cambian con frecuencia.

---

## 🤖 Automatización

El README se genera desde [`data/subscriptions.json`](data/subscriptions.json) mediante [`scripts/generate_readme.py`](scripts/generate_readme.py) y se actualiza automáticamente en cada push a main con un [GitHub Action](.github/workflows/update-readme.yml).

---

## 🌍 Multi-idioma

| Idioma | Archivo |
|--------|---------|
| English | [`README.md`](README.md) |
| Español | [`README.es.md`](README.es.md) |

---

## 🙌 Créditos

Curado con ❤️ por la comunidad open-source. Inspirado en la tradición de listas [awesome](https://github.com/sindresorhus/awesome).
""",
}


def main():
    entries = load_data()

    for lang in ("en", "es"):
        header = TABLE_HEADERS[lang]
        rows = build_rows(entries, lang)
        table = "\n".join([header, TABLE_SEPARATOR] + rows)
        content = TEMPLATES[lang].format(stars_table=table)

        out_path = README_EN if lang == "en" else README_ES
        with open(out_path, "w") as f:
            f.write(content)
        print(f"✓ Generated {out_path}")


if __name__ == "__main__":
    main()
