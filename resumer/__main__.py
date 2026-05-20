# from resumer import get_file_vars # import works
# from resumer.constants import get_constants_from_file
import os
from dotenv import load_dotenv
from resumer.llm import LLMClient

load_dotenv("./.env")

API_KEY = os.getenv("LLM_API_KEY")

if __name__ == "__main__":
    client = LLMClient(API_KEY)
    resp = client.prompt("Hi!, This is a test")
    print(resp)
    print(dir(resp))
    print(resp.text)
