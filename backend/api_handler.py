import os
import httpx
from typing import Optional

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "demo-key")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "demo-key")

class LLMClient:
    def __init__(self, provider: str = "openai"):
        self.provider = provider.lower()

    async def query(self, prompt: str, model: Optional[str] = None) -> str:
        """
        Send a query to the selected LLM provider.
        """
        if self.provider == "openai":
            return await self._query_openai(prompt, model or "gpt-4o-mini")
        elif self.provider == "gemini":
            return await self._query_gemini(prompt, model or "gemini-pro")
        else:
            return f"[LLM:{self.provider}] {prompt[:50]}..."

    async def _query_openai(self, prompt: str, model: str) -> str:
        """
        OpenAI query (replace with real endpoint later).
        """
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        }
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                return data["choices"][0]["message"]["content"]
            return f"Error: {resp.text}"

    async def _query_gemini(self, prompt: str, model: str) -> str:
        """
        Gemini query (replace with real endpoint later).
        """
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.post(url, headers=headers, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            return f"Error: {resp.text}"
