from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from kafka import KafkaProducer
import time
import os

app = FastAPI(title="Kafka Chat")

class Message(BaseModel):
    text: str
    user: str

def create_producer():
    """Создаёт producer только при необходимости"""
    return KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        client_id='fastapi-producer'
    )

@app.post("/send-message")
async def send_message(msg: Message):
    try:
        # Ждём Kafka 10 секунд если нужно
        for i in range(10):
            try:
                producer = create_producer()
                data = msg.dict()
                producer.send('chat-topic', data)
                producer.flush()
                producer.close()
                return {"status": "sent", "message": data}
            except:
                time.sleep(1)
                continue
        raise Exception("Kafka не доступна")
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Kafka недоступна: {str(e)}")

@app.get("/")
def root():
    return {"message": "FastAPI работает! POST /send-message для Kafka"}

@app.get("/health")
def health():
    return {"status": "healthy"}
