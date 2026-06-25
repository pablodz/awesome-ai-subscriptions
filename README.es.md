# 💰 awesome-ai-subscriptions

> Suscripciones de IA para programar comparadas — planes, modelos, límites y precios de un vistazo.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

Una lista curada de **planes de suscripción de IA para programar** de los principales proveedores. Compara precios, modelos soportados, límites de uso, ventanas de contexto y mecanismos de control entre ChatGPT, Claude, Copilot, Cursor, Gemini Code Assist, Amazon Q, Command Code, Z.ai, Xiaomi MiMo y más.

📖 [English version →](README.md)

---

## 📊 La Lista

> Ordenada por precio ascendente dentro de cada empresa. Actualizada automáticamente.

| # | Empresa / Producto | Plan | Precio/mes | Modelos de Código | Ventana de Contexto | Límites y Ventana | Control de Uso |
|---|-------------------|------|----------|---------------|----------------|----------------------|---------------|
| 1 | **OpenAI**<br>ChatGPT | Free | Free | GPT-4o mini<br>GPT-4o (limited) | 128K (GPT-4o) | Limited GPT-4o messages; GPT-4o mini unrestricted<br><br>*Per session (3h rolling)* | Message-based rate limits |
| 2 | **OpenAI**<br>ChatGPT | Plus | $20/mo | GPT-4o<br>o1<br>o3<br>o4-mini<br>Codex (codex-1)<br>GPT-4.5 (1M ctx) | 128K (GPT-4o) / 200K (o1,o3) / 1M (GPT-4.5) | ~80 msgs/3h (GPT-4o); ~50 msgs/week (o1); limited o3/o4-mini; Codex limited<br><br>*3h (GPT-4o) / weekly (o1,o3) / monthly (Codex)* | Message-based rate limits per time window |
| 3 | **OpenAI**<br>ChatGPT | Pro | $200/mo | GPT-4o (unlimited)<br>o1 pro mode<br>o1 (unlimited)<br>o3 (unlimited)<br>o4-mini (unlimited)<br>Codex (codex-1) | 128K (GPT-4o) / 200K (o1,o3) / 1M (GPT-4.5) | Unlimited GPT-4o, o1, o1-pro, o3, o4-mini; Codex full access<br><br>*N/A (unlimited for main models)* | Unlimited access to all models; Codex free during preview |
| 4 | **OpenAI**<br>ChatGPT | Team | $25/mo<br>($300/yr) | GPT-4o<br>o1<br>o3<br>o4-mini<br>Codex (codex-1)<br>GPT-4.5 | 128K (GPT-4o) / 200K (o1,o3) / 1M (GPT-4.5) | Higher than Plus; ~100+ msgs/3h GPT-4o; full Codex access<br><br>*3h / weekly* | Message-based limits per seat; admin console |
| 5 | **OpenAI**<br>ChatGPT | Enterprise | $60/mo<br>($720/yr) | GPT-4o<br>o1<br>o3<br>o4-mini<br>Codex (codex-1)<br>GPT-4.5 | 128K (GPT-4o) / 200K (o1,o3) / 1M (GPT-4.5) | Highest limits; unlimited for most models<br><br>*Custom / unlimited* | Enterprise-grade rate limits; SSO; audit logs; SOC 2 |
| 6 | **Anthropic**<br>Claude | Free | Free | Claude Sonnet<br>Claude Haiku | 200K | Baseline access; limited messages per 5h session<br><br>*5h session / weekly* | Session-based (5h rolling); varies with demand |
| 7 | **Anthropic**<br>Claude | Pro | $20/mo<br>($200/yr) | Claude Sonnet<br>Claude Opus<br>Claude Haiku | 200K | 5x Free tier; ~45+ msgs/5h (varies by model)<br><br>*5h session / weekly* | Session-based (5h rolling); usage credits available |
| 8 | **Anthropic**<br>Claude | Max 5× | $100/mo | Claude Sonnet<br>Claude Opus<br>Claude Haiku | 200K | 5x Pro (25x Free); higher output limits; priority access<br><br>*5h session / weekly (two caps: all-models + Sonnet-only)* | Two-tier session caps (5h + weekly); usage credits available |
| 9 | **Anthropic**<br>Claude | Max 20× | $200/mo | Claude Sonnet<br>Claude Opus<br>Claude Haiku | 200K | 20x Pro (100x Free); highest output limits; top priority<br><br>*5h session / weekly (two caps: all-models + Sonnet-only)* | Two-tier session caps (5h + weekly); usage credits available |
| 10 | **Anthropic**<br>Claude | Team Standard | $25/mo<br>($240/yr) | Claude Sonnet<br>Claude Opus<br>Claude Haiku | 200K | 1.25x Pro per seat; higher than Pro<br><br>*5h session / one weekly cap (all models)* | Per-member limits; usage credits available; admin console |
| 11 | **Anthropic**<br>Claude | Enterprise | $20/mo<br>($240/yr) | Claude Sonnet<br>Claude Opus<br>Claude Haiku | Up to 500K | No per-seat caps; unlimited via API-rate billing<br><br>*N/A (pay-per-token, no caps)* | Pay-per-token at API rates; admin-set spend limits |
| 12 | **GitHub / Microsoft**<br>Copilot | Free | Free | GPT-4o<br>GPT-4.1 (base)<br>Claude Sonnet 3.5 (limited) | 128K (GPT-4o) / 200K (Claude Sonnet) | 2,000 code completions/month; 50 premium requests/month<br><br>*Monthly reset* | Premium request quotas (50/mo); base models free |
| 13 | **GitHub / Microsoft**<br>Copilot | Pro | $10/mo<br>($100/yr) | GPT-4o<br>GPT-4.1 (base, unlimited)<br>Claude Sonnet 3.5/3.7/4<br>o3-mini<br>o4-mini<br>Gemini 2.0 Flash<br>Gemini 2.5 Pro<br>GPT-4.5 | 128K (GPT-4o) / 200K (Claude) / 1M (Gemini 2.5 Pro) | Unlimited base models; 300 premium requests/month + $0.04/req overage<br><br>*Monthly reset (premium requests)* | Premium request quotas; different model multipliers (Opus=10x, GPT-4.5=50x) |
| 14 | **GitHub / Microsoft**<br>Copilot | Pro+ | $39/mo | GPT-4o<br>GPT-4.1 (base, unlimited)<br>Claude Sonnet/Opus<br>o3-mini<br>o4-mini<br>Gemini 2.0 Flash/2.5 Pro<br>GPT-4.5 | 128K (GPT-4o) / 200K (Claude) / 1M (Gemini 2.5 Pro) | Unlimited base models; 1,500 premium requests/month + $0.04/req overage<br><br>*Monthly reset (premium requests)* | Premium request quotas (1,500/mo); model multipliers apply |
| 15 | **GitHub / Microsoft**<br>Copilot | Business | $19/mo | GPT-4o<br>GPT-4.1 (base, unlimited)<br>Claude Sonnet/Opus<br>o3-mini<br>o4-mini<br>Gemini 2.0 Flash/2.5 Pro<br>GPT-4.5 | 128K (GPT-4o) / 200K (Claude) / 1M (Gemini 2.5 Pro) | Unlimited base models; 300 premium requests/user/month + $0.04/req overage<br><br>*Monthly reset* | Premium request quotas per user; org-wide policy management |
| 16 | **GitHub / Microsoft**<br>Copilot | Enterprise | $39/mo | GPT-4o<br>GPT-4.1 (base, unlimited)<br>Claude Sonnet/Opus<br>o3-mini<br>o4-mini<br>Gemini<br>GPT-4.5<br>All premium models | 128K (GPT-4o) / 200K (Claude) / 1M (Gemini) | Unlimited base models; 1,000 premium requests/user/month + $0.04/req overage<br><br>*Monthly reset* | Premium request quotas; full enterprise governance |
| 17 | **Cursor**<br>Cursor IDE | Hobby | Free | Cheetah (tab)<br>GPT-4o mini<br>Claude Sonnet (limited) | 200K | Limited agent requests; 50 fast requests/month<br><br>*Monthly* | Request-based (limited); Auto Mode not available for premium models |
| 18 | **Cursor**<br>Cursor IDE | Pro | $20/mo<br>($192/yr) | Claude Sonnet<br>Claude Opus<br>GPT-4o<br>o3-mini<br>Gemini 2.5 Pro<br>Cheetah (tab) | 200K (standard) / 1M (Max Mode, Gemini/GPT-4.1) | Auto Mode unlimited; $20 credit pool (~225 Sonnet requests); overage at API rates<br><br>*Monthly credit reset* | Credit-based ($20/mo pool); Auto Mode free & unlimited; premium model selection costs credits |
| 19 | **Cursor**<br>Cursor IDE | Pro+ | $60/mo<br>($576/yr) | All Pro models + higher access | 200K (standard) / 1M (Max Mode) | Auto Mode unlimited; $70 credit pool (~790 Sonnet requests); overage at API rates<br><br>*Monthly credit reset* | Credit-based ($70/mo pool); 3.5x Pro credits |
| 20 | **Cursor**<br>Cursor IDE | Ultra | $200/mo<br>($1920/yr) | All Pro models + highest access | 200K (standard) / 1M (Max Mode) | Auto Mode unlimited; $400 credit pool (~4,500 Sonnet requests); priority<br><br>*Monthly credit reset* | Credit-based ($400/mo pool); 20x Pro credits |
| 21 | **Cursor**<br>Cursor IDE | Teams | $40/mo<br>($384/yr) | All Pro models | 200K (standard) / 1M (Max Mode) | Per-user credit pool; admin-managed<br><br>*Monthly* | Credit-based per user; central admin; SSO |
| 22 | **Google**<br>Gemini Code Assist | Individual (Free) | Free | Gemini 2.5 Flash (auto)<br>Gemini 2.5 Pro (auto) | 1M (codebase awareness) / 128K (chat) | 60 RPM; 1,000 RPD (agent/CLI); 6,000 code completions/day; 960 chat/day<br><br>*Per minute / daily* | Requests per minute/day for agent/CLI; separate IDE limits |
| 23 | **Google**<br>Gemini Code Assist | AI Pro (Individual) | $20/mo | Gemini 2.5 Flash<br>Gemini 2.5 Pro<br>Gemini 3 (preview) | 1M (codebase) / 128K+ (chat) | Higher RPM/RPD than free; ~1,500+ RPD agent/CLI<br><br>*Per minute / daily* | Higher request quotas; includes Google AI Pro benefits |
| 24 | **Google**<br>Gemini Code Assist | Standard (Teams) | $22.8/mo<br>($228/yr) | Gemini 2.5 Flash<br>Gemini 2.5 Pro<br>Gemini 3 (preview) | 1M | 120 RPM; 1,500 RPD<br><br>*Per minute / daily* | Request quotas; admin-controlled; code customization with private repos |
| 25 | **Google**<br>Gemini Code Assist | Enterprise | $54/mo<br>($540/yr) | Gemini 2.5 Flash<br>Gemini 2.5 Pro<br>Gemini 3 (preview) | 1M | 120 RPM; 2,000 RPD<br><br>*Per minute / daily* | Request quotas; enterprise governance; pay-as-you-go API option |
| 26 | **Amazon**<br>Q Developer | Free | Free | Claude Sonnet 4 (default)<br>Claude Sonnet 3.5/3.7 | 200K | 50 agentic requests/month; 1,000 LOC/month (code transformation)<br><br>*Monthly reset* | Agentic request quotas (50/mo); separate code transformation quotas |
| 27 | **Amazon**<br>Q Developer | Pro | $19/mo | Claude Sonnet 4 (default)<br>Claude Sonnet 3.5/3.7 | 200K | ~1,000 agentic requests/month (10K inference calls); 4,000 LOC/month code transformation<br><br>*Monthly reset* | Agentic request quotas per user; IP indemnity; admin dashboard |
| 28 | **CommandCode AI**<br>Command Code | Go | $1/mo | DeepSeek V4 Pro/Flash<br>Kimi K2 series<br>GLM 5/5.1/5.2<br>MiniMax M2/M3<br>MiMo V2.5 Pro<br>Qwen 3.6/3.7<br>Nemotron 3 Ultra<br>Step 3.5/3.7 Flash | Up to 1M | $10 credits/mo (~15K requests); 5h: $3, weekly: $6<br><br>*5h (30% of monthly) / weekly (60%)* | Credit-based ($10/mo); rolling 5h/weekly windows; open-source models only |
| 29 | **CommandCode AI**<br>Command Code | Pro | $15/mo | All Go models + Claude Opus/Sonnet/Haiku/Fable<br>GPT-5.3/5.4/5.5<br>Gemini 3.1/3.5 Flash<br>Fugu Ultra | Up to 1M | $30 credits/mo (~25K requests); 5h: $9, weekly: $18<br><br>*5h (30% of monthly) / weekly (60%)* | Credit-based ($30/mo); rolling 5h/weekly windows; all premium + open-source models |
| 30 | **CommandCode AI**<br>Command Code | Max 10× | $100/mo | All Pro models | Up to 1M | $150 credits/mo (~110K requests); 5h: $45, weekly: $90<br><br>*5h (30% of monthly) / weekly (60%)* | Credit-based ($150/mo); higher rolling windows; priority support |
| 31 | **CommandCode AI**<br>Command Code | Max 20× | $200/mo | All Pro models | Up to 1M | $300 credits/mo (~200K requests); 5h: $90, weekly: $180<br><br>*5h (30% of monthly) / weekly (60%)* | Credit-based ($300/mo); highest rolling windows; top priority support |
| 32 | **Z.ai (Zhipu AI)**<br>GLM Coding Plan | Lite | $18/mo | GLM-5.2<br>GLM-5-Turbo<br>GLM-4.7 | 1M (GLM-5.2) / 131K output tokens | ~80 prompts/5h; ~400 prompts/week; 100 MCP calls/month<br><br>*5h / weekly / monthly (MCP)* | Prompt-based (1 prompt ≈ 15-20 model invocations); quota multipliers for advanced models |
| 33 | **Z.ai (Zhipu AI)**<br>GLM Coding Plan | Pro | $72/mo | GLM-5.2<br>GLM-5-Turbo<br>GLM-4.7 | 1M (GLM-5.2) / 131K output tokens | ~400 prompts/5h; ~2,000 prompts/week; 1,000 MCP calls/month<br><br>*5h / weekly / monthly (MCP)* | Prompt-based; 5x Lite limits; recommend 1-2 concurrent projects |
| 34 | **Z.ai (Zhipu AI)**<br>GLM Coding Plan | Max | $160/mo | GLM-5.2<br>GLM-5-Turbo<br>GLM-4.7 | 1M (GLM-5.2) / 131K output tokens | ~1,600 prompts/5h; ~8,000 prompts/week; 4,000 MCP calls/month<br><br>*5h / weekly / monthly (MCP)* | Prompt-based; 20x Lite limits; 2+ concurrent projects; highest concurrency |
| 35 | **Xiaomi**<br>MiMo | Open-Source / API | Free | MiMo-7B (MIT, 32K ctx)<br>MiMo-V2-Flash (309B MoE, MIT, 256K ctx)<br>MiMo-V2-Pro (1T params, API-only, 1M ctx)<br>MiMo-V2.5-Pro (1T+, 1M ctx) | 32K (MiMo-7B) / 256K (V2-Flash) / 1M (V2-Pro, V2.5-Pro) | No subscription caps (pay-per-token API); MiMo Code: authentication required<br><br>*N/A (API-based)* | Pay-per-token API (~$0.1/M input, ~$0.3/M output for V2-Flash); open-source models are free self-hosted |
| 36 | **Replit**<br>Replit AI | Core | $25/mo<br>($240/yr) | Replit Agent (custom)<br>Claude Sonnet<br>GPT-4o | 200K | Unlimited Agent usage; cloud compute limits apply<br><br>*Monthly (compute-based)* | Compute-based (CPU/RAM hours); Agent usage unlimited |
| 37 | **Perplexity**<br>Perplexity Pro | Pro | $20/mo<br>($200/yr) | Claude Sonnet/Opus<br>GPT-4o<br>o3-mini<br>Sonar (custom)<br>Gemini 2.5 Pro | 200K | ~600 Pro searches/day; unlimited quick searches<br><br>*Daily* | Search-based (600 Pro searches/day); model switching unlimited |
| 38 | **Tabnine**<br>Tabnine | Free | Free | Tabnine proprietary | Limited (proprietary) | Basic code completions; limited chat<br><br>*N/A* | Feature-gated (no chat/agent on Free) |
| 39 | **Tabnine**<br>Tabnine | Pro | $12/mo<br>($144/yr) | Tabnine proprietary<br>Claude Sonnet<br>GPT-4o<br>Gemini | Variable (10K-100K+) | Unlimited completions; chat & agent limits vary<br><br>*Monthly* | Usage-based; chat credits; agent mode limited |

---

## 📋 Plantilla — Añadir una nueva suscripción

¿Quieres contribuir? Añade tu entrada en [`data/subscriptions.json`](data/subscriptions.json) y abre un PR:

```json
{
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
}
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
