# openai-agents
openai SDK agents
# 🤖 OpenAI Agent with `openai-agents`

This project is a simple implementation of an **OpenAI agent** built using the [`openai-agents`](https://github.com/openai/openai-agents) SDK. It uses `AsyncOpenAI` as the model backend, with support for models like `gpt-4`, or even Google's `gemini-2.0-flash` via OpenAI-compatible endpoints.

---

## 🚀 Features

- Uses `openai-agents` Runner + Agent structure
- Compatible with OpenAI or Gemini (via base URL override)
- Asynchronous message handling with `asyncio`
- Chain-of-thought reasoning
- Can run in console or integrate with `Chainlit` for UI

---

## 🛠️ Tech Stack

- Python 3.10+
- [openai-agents](https://github.com/openai/openai-agents)
- `asyncio` for async event loop
- `.env` for secure API key storage
- Optional: Chainlit (for UI frontend)


