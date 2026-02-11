from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kafka import KafkaProducer
import json

app = FastAPI(title="Kafka Chat")

class Message(BaseModel):
    text: str
    user: str

@app.post("/send-message")
async def send_message(msg: Message):
    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        retries=0,  # Без повторов
        max_block_ms=5000  # Быстрый таймаут
    )
    try:
        producer.send('chat-topic', msg.dict())
        producer.flush(timeout=5)
        return {"status": "sent", "message": msg.dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Kafka error: {str(e)}")
    finally:
        producer.close()

@app.get("/")
def root():
    return {"message": "FastAPI готов! Отправляй POST /send-message"}
