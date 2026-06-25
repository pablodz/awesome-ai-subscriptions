# Contributing to awesome-ai-subscriptions

Thanks for helping grow this list! Here's how to add a subscription plan.

## 🚀 Quick Start

1. **Fork** this repo
2. **Add** your entry to [`data/subscriptions.json`](data/subscriptions.json)
3. **Run** `python3 scripts/generate_readme.py` to regenerate READMEs
4. **Open a Pull Request**

## 📋 JSON Template

```json
{
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
}
```

## ✅ Guidelines

### Company & Product
- Use the official company name (e.g., "OpenAI", "Anthropic", "GitHub / Microsoft")
- `product` is the subscription product name (e.g., "ChatGPT", "Claude", "Copilot")

### Plan
- Use the official plan name (e.g., "Plus", "Max 5×", "Pro+")
- Include pricing tier indicators as shown on the provider's pricing page

### Pricing
- `price_monthly`: Monthly price in USD (0 for free plans)
- `price_annual`: Annual price in USD, or `null` if not available
- Use the standard monthly rate (not promotional/sale pricing)

### Models
- List all **coding-relevant** models included in the plan
- Use official model names (e.g., "Claude Sonnet 4", not "Sonnet")
- Note if a model is limited or unlimited access in parentheses

### Token Context
- State the maximum theoretical context window per model
- Use format: "128K", "200K", "1M"
- If multiple models have different windows, summarize like "128K (GPT-4o) / 200K (Claude) / 1M (Gemini)"

### Rate Limits
- Describe the **practical usage cap** in clear terms
- Include approximate numbers when exact limits aren't published
- Specify the unit: messages, requests, credits, prompts, tokens

### Rate Window
- How often limits reset: "3h rolling", "5h session", "daily", "weekly", "monthly"
- If multiple windows exist, include all: "5h / weekly / monthly (MCP)"

### Usage Control
- Describe **how** the provider meters usage (credit-based, message-based, request-based, etc.)
- Include key aspects like overage costs, pool sizes, multipliers

### Coding Features
- List 3-6 key coding-specific features using emoji prefixes for scannability
- Common emoji:
  - 🤖 Agent mode / autonomous · 🧠 Reasoning · ⚡ Fast completions
  - 🔌 Multi-model · 🛠 MCP · 💻 CLI · 🌐 Web search
  - 🔒 Privacy · 🏠 Local models · 📊 Analytics
  - 🌳 Git integration · 📝 PR reviews · 🧪 Test generation
  - 🖥 IDE integration · 📱 Multi-platform

### URL
- Link to the official pricing or product page

### Notes
- Add any important caveats, limitations, or unique aspects
- Keep under 80 characters

## 📊 What Qualifies

A subscription plan must:
1. Be a **paid or free subscription** for AI coding assistance
2. Have clearly defined **rate limits, models, and pricing**
3. Be **publicly available** (not closed beta or invite-only unless widely known)
4. Focus primarily on **coding/software development** use cases

## 🌐 Multi-language

- The README is auto-generated in both English and Spanish
- Descriptions and features are currently English-only in the data; translations welcome!
- To add a new language, create `README.xx.md` and update the generation script

## 📬 Submitting

1. Ensure your JSON is valid (test with `python3 -m json.tool data/subscriptions.json`)
2. Run `python3 scripts/generate_readme.py` and verify the output
3. Open a PR with a descriptive title like: `Add [Company] - [Plan]`
4. In the PR body, link to the official pricing page as a source

Thank you! 🎉
