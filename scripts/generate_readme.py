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


TABLE_HEADER_EN = "| # | Company / Product | Plan | Price/mo | Coding Models | Context Window | Rate Limits & Window | Usage Control |"
TABLE_SEPARATOR = "|---|-------------------|------|----------|---------------|----------------|----------------------|---------------|"

TABLE_HEADER_ES = "| # | Empresa / Producto | Plan | Precio/mes | Modelos de Código | Ventana de Contexto | Límites y Ventana | Control de Uso |"


def build_rows(entries: list, lang: str) -> list:
    rows = []
    for i, e in enumerate(entries, 1):
        company_product = f"**{e['company']}**<br>{e['product']}"
        plan = e["plan"]
        if e["price_monthly"] == 0:
            price = "Free"
        elif e["price_annual"]:
            price = f"${e['price_monthly']}/mo<br>(${e['price_annual']}/yr)"
        else:
            price = f"${e['price_monthly']}/mo"
        models = "<br>".join(e["models"])
        ctx = e["token_context"]
        limits = f"{e['rate_limit']}<br><br>*{e['rate_window']}*"
        control = e["usage_control"]

        row = f"| {i} | {company_product} | {plan} | {price} | {models} | {ctx} | {limits} | {control} |"
        rows.append(row)
    return rows


TABLE_HEADERS = {
    "en": TABLE_HEADER_EN,
    "es": TABLE_HEADER_ES,
}

TEMPLATES = {
    "en": """# 💰 awesome-ai-subscriptions

> AI coding subscriptions compared — plans, models, rate limits, and pricing at a glance.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of **AI coding subscription plans** from major providers. Compare pricing, supported models, rate limits, context windows, and usage control mechanisms across ChatGPT, Claude, Copilot, Cursor, Gemini Code Assist, Amazon Q, Command Code, Z.ai, Xiaomi MiMo, and more.

📖 [Versión en español →](README.es.md)

---

## 📊 The List

> Ordered by price ascending within each company. Updated automatically.

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
  "models": ["Model A", "Model B"],
  "token_context": "128K",
  "rate_limit": "80 msgs/3h",
  "rate_window": "3h rolling",
  "usage_control": "Message-based rate limits",
  "coding_features": ["Feature 1", "Feature 2"],
  "url": "https://example.com",
  "notes": "Optional notes"
}}
```

**The table is auto-generated** — no need to edit README.md directly.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details.

---

## 📐 Columns Explained

| Column | Description |
|--------|-------------|
| **Coding Models** | AI models available for code generation, editing, and reasoning in each plan |
| **Context Window** | Theoretical maximum tokens (input) the model can process in one request |
| **Rate Limits & Window** | Practical usage caps (messages, requests, credits, prompts) and the time window they reset |
| **Usage Control** | How the provider meters and limits usage (credits, messages, tokens, prompts) |

---

## 🏷️ Key Concepts

### Rate Limit Windows
- **3h / 5h rolling**: Limit resets continuously over a sliding window (e.g., "80 messages in the last 3 hours")
- **Daily**: Resets at midnight or 24h after first request
- **Weekly**: Resets every 7 days from first use
- **Monthly**: Resets on the 1st of each month or billing date

### Usage Control Mechanisms
- **Message-based**: Counts each conversation turn (ChatGPT, Claude)
- **Request-based**: Counts each model invocation (Copilot premium requests, Amazon Q)
- **Credit-based**: Dollar-denominated pool consumed at API rates (Command Code, Cursor)
- **Prompt-based**: Counts high-level prompts, each ~15-20 model calls (Z.ai)
- **Token-based**: Direct per-token billing (API plans, Enterprise)

---

## 🤖 Automation

The README is generated from [`data/subscriptions.json`](data/subscriptions.json) via [`scripts/generate_readme.py`](scripts/generate_readme.py) and auto-committed by a [GitHub Action](.github/workflows/update-readme.yml).

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

> Suscripciones de IA para programar comparadas — planes, modelos, límites y precios de un vistazo.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

Una lista curada de **planes de suscripción de IA para programar** de los principales proveedores. Compara precios, modelos soportados, límites de uso, ventanas de contexto y mecanismos de control entre ChatGPT, Claude, Copilot, Cursor, Gemini Code Assist, Amazon Q, Command Code, Z.ai, Xiaomi MiMo y más.

📖 [English version →](README.md)

---

## 📊 La Lista

> Ordenada por precio ascendente dentro de cada empresa. Actualizada automáticamente.

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
  "models": ["Modelo A", "Modelo B"],
  "token_context": "128K",
  "rate_limit": "80 msgs/3h",
  "rate_window": "Ventana de 3h",
  "usage_control": "Límites basados en mensajes",
  "coding_features": ["Función 1", "Función 2"],
  "url": "https://example.com",
  "notes": "Notas opcionales"
}}
```

**La tabla se genera automáticamente** — no es necesario editar README.md directamente.

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.

---

## 📐 Columnas Explicadas

| Columna | Descripción |
|---------|-------------|
| **Modelos de Código** | Modelos de IA disponibles para generar, editar y razonar código en cada plan |
| **Ventana de Contexto** | Tokens máximos teóricos (entrada) que el modelo puede procesar en una solicitud |
| **Límites y Ventana** | Límites prácticos de uso (mensajes, solicitudes, créditos, prompts) y la ventana de tiempo en que se reinician |
| **Control de Uso** | Cómo el proveedor mide y limita el uso (créditos, mensajes, tokens, prompts) |

---

## 🏷️ Conceptos Clave

### Ventanas de Límite
- **3h / 5h continuas**: El límite se reinicia continuamente en una ventana deslizante
- **Diario**: Se reinicia a medianoche o 24h después de la primera solicitud
- **Semanal**: Se reinicia cada 7 días desde el primer uso
- **Mensual**: Se reinicia el día 1 de cada mes o en la fecha de facturación

### Mecanismos de Control de Uso
- **Por mensajes**: Cuenta cada turno de conversación (ChatGPT, Claude)
- **Por solicitudes**: Cuenta cada invocación al modelo (Copilot, Amazon Q)
- **Por créditos**: Pool en dólares consumido a tarifas de API (Command Code, Cursor)
- **Por prompts**: Cuenta prompts de alto nivel, cada uno ≈15-20 llamadas al modelo (Z.ai)
- **Por tokens**: Facturación directa por token (planes API, Enterprise)

---

## 🤖 Automatización

El README se genera desde [`data/subscriptions.json`](data/subscriptions.json) mediante [`scripts/generate_readme.py`](scripts/generate_readme.py) y se actualiza automáticamente con un [GitHub Action](.github/workflows/update-readme.yml).

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
