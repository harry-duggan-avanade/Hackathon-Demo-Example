import openai
from fastapi import FastAPI

openai.api_type = "azure"
openai.api_base = ""
openai.api_version = "2023-07-01-preview"
openai.api_key = ""

app = FastAPI()

@app.post("/")
def use_chatbot(messages: list[dict]):
    
    response = openai.ChatCompletion.create(
        engine= "gpt-35-turbo-16k",
        messages = messages,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    return response.choices[0].message

