
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from tts.speech_engine import falar
from openai import OpenAI

load_dotenv()

client = OpenAI()

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/falar")
async def gerar_resposta(request: PromptRequest, x_webhook_token: str = Header(None)):
    webhook_token_secreto = os.getenv("WEBHOOK_SECRET", "token_padrao")

    if x_webhook_token != webhook_token_secreto:
        raise HTTPException(status_code=403, detail="Token do webhook inválido.")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": request.prompt}]
    )
    resposta = response.choices[0].message.content
    falar(resposta)
    return {"resposta": resposta}
