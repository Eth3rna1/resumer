from google import genai
from google.genai import types
from .exceptions import MaxTokensExceededException


DEFAULT_MODEL = "gemini-2.5-flash"  # free model


class LLMClient:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.model = DEFAULT_MODEL

    def set_model(self, model: str):
        self.model = model

    def prompt(self, prompt) -> str:
        resp = self.client.models.generate_content(model=self.model, contents=prompt)

        if any(
            candidate.finish_reason == types.FinishReason.MAX_TOKENS
            for candidate in resp.candidates
        ):
            raise MaxTokensExceededException(
                "Max token use exceeded. Response may have been truncated."
            )

        return resp.text
