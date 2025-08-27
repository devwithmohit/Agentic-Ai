import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()


class SteamingCallbackHandler(BaseCallbackHandler):
    """Custom callback handler for streaming tokens"""

    def __init__(self):
        self.tokens = {}

    def on__llm_new_token(self, token: str, **kwargs) -> None:
        print(token, end="", flush=True)
        self.tokens.append(token)


class LangChainDeepSeekClient:
    def __init__(self, api_key: str, str=None):
        if not api_key:
            api_key = os.getenv("API_KEY")

        if not api_key:
            raise ValueError(
                "API key is required. Please set API_KEY in your .env file."
            )
        self.llm = ChatOpenAI(
            model="deepseek/deepseek-r1:free",
            openai_api_key=api_key,
            openai_api_base="https://openrouter.ai/api/v1",
            streaming=True,
            callbacks=[SteamingCallbackHandler()],
        )

    def get_completion_streaming(self, messages):
        try:
            langchain_messages = []
            for msg in messages:
                if msg["role"] == "user":
                    langchain_messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "system":
                    langchain_messages.append(HumanMessage(content=msg["content"]))
            # Stream the response
            response = self.llm(langchain_messages)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"

    def get_completion_streaming_generator(self, message):
        try:
            langchain_messages = []
            for msg in message:
                if msg["role"] == "user":
                    langchain_messages.append(HumanMessage(content=msg["content"]))
                elif msg["role"] == "system":
                    langchain_messages.append(SystemMessage(content=msg["content"]))
            for chunk in self.llm.stream(langchain_messages):
                yield chunk.content
        except Exception as e:
            yield f"Error: {str(e)}"
