import os
import openai
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()


@app.post("/")
def use_chatbot(messages: list[dict]):
    
    response = openai.ChatCompletion.create(
        engine= os.getenv("OPENAI_MODEL"),
        messages = messages,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    return response.choices[0].message

