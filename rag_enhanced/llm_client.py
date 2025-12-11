import os

class LLMClient:
    """Base class for LLM clients."""
    def generate(self, prompt: str, system_prompt: str = None, **kwargs) -> str:
        raise NotImplementedError

class OpenRouterLLMClient(LLMClient):
    """Client for OpenRouter API."""
    def __init__(self, api_key: str = None, model: str = "openai/gpt-4.1", base_url: str = "https://openrouter.ai/api/v1"):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.model = model
        self.base_url = base_url
        
        if not self.api_key:
            print("[WARNING] No OPENROUTER_API_KEY provided. Calls may fail.")

    def generate(self, prompt: str, system_prompt: str = None, **kwargs) -> str:
        import time
        max_retries = 5
        base_delay = 10
        
        for attempt in range(max_retries):
            try:
                from openai import OpenAI
                client = OpenAI(api_key=self.api_key, base_url=self.base_url)
                
                messages = []
                if system_prompt:
                    messages.append({"role": "system", "content": system_prompt})
                messages.append({"role": "user", "content": prompt})
                
                # Default extra_body for reasoning if not provided, as per user example
                extra_body = kwargs.pop("extra_body", None)
                
                response = client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    extra_body=extra_body,
                    **kwargs
                )
                return response.choices[0].message.content
            except Exception as e:
                error_msg = str(e)
                if "404" in error_msg and "data policy" in error_msg:
                    print("\n[CRITICAL ERROR] OpenRouter Data Policy Error.")
                    print("You are using a free model which requires enabling 'Allow data collection'.")
                    print("Please visit: https://openrouter.ai/settings/privacy to enable it.")
                    print("The script cannot proceed without this setting or a paid model.\n")
                    raise e
                elif "429" in error_msg:
                     if "per-day" in error_msg:
                         print(f"\n[CRITICAL ERROR] Daily Rate limit exceeded: {e}.")
                         print("You have hit the daily free limit. Processing cannot continue.")
                         raise e
                     else:
                         # Transient rate limit (per-minute or temporary)
                         wait_time = base_delay * (2 ** attempt)
                         print(f"\n[WARN] Rate limit hit (attempt {attempt+1}/{max_retries}). Waiting {wait_time}s...")
                         time.sleep(wait_time)
                         continue
                else:
                    print(f"[ERROR] OpenRouter API Error: {e}")
                    raise e
        
        raise Exception("Max retries exceeded for rate limit.")

def get_llm_client(provider: str = "openrouter", **kwargs) -> LLMClient:
    return OpenRouterLLMClient(**kwargs)
