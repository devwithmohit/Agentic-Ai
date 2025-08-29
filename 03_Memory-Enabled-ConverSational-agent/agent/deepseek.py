import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

class DeepSeekClient:
    def __init__(self, api_key: str = API_KEY, model: str = "deepseek/deepseek-r1:free"):
        if not api_key:
            raise ValueError("API key is required. Please set API_KEY in your .env file.")
        self.api_key = api_key
        self.model = model
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    def get_completion(self, messages):
        """
        Send a conversation (list of messages) to DeepSeek via OpenRouter API.

        Args:
            messages (list): [{"role": "user"/"assistant"/"system", "content": str}, ...]

        Returns:
            str: The model's response content, or error message.
        """
        payload = {
            "model": self.model,
            "messages": messages
        }
        try:
            response = requests.post(API_URL, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    client = DeepSeekClient()
    messages = [
        {"role": "user", "content": "Hello, what can you do?"},
    ]
    print(client.get_completion(messages))