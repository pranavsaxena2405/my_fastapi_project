import pandas as pd
from fastapi import UploadFile
from io import StringIO
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("LLM_API_KEY")

def process_csv(file: UploadFile):
    content = file.file.read().decode("utf-8")
    csv_data = StringIO(content)
    df = pd.read_csv(csv_data)
    return df

def classify_company(description: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Is the following company a technology company? Answer Yes or No.\n\n{description}",
        max_tokens=10
    )
    answer = response.choices[0].text.strip()
    return "Yes" if "yes" in answer.lower() else "No"
