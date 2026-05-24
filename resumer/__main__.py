# from resumer import get_file_vars # import works
# from resumer.constants import get_constants_from_file
import os
from dotenv import load_dotenv
from resumer.llm import LLMClient
from resumer.resume_handle import ResumeHandler
from resumer.llm.exceptions import MaxTokensExceededException

load_dotenv("./.env")

API_KEY = os.getenv("LLM_API_KEY")

if __name__ == "__main__":
    client = LLMClient(API_KEY)
    resp = client.prompt("Hi!, This is a test")
    print(f'Gemini: "{resp}"')
