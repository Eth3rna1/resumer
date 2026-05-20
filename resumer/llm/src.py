from google import genai

DEFAULT_MODEL = "gemini-2.5-flash"  # free model


class LLMClient:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
        self.model = DEFAULT_MODEL

    def set_model(self, model: str):
        self.model = model

    def prompt(self, prompt) -> str:
        resp = self.client.models.generate_content(model=self.model, contents=prompt)

        return resp.text
