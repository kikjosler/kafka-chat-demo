from fastapi import FastAPI
from kafka import KafkaProducer
import json
from pydantic import BaseModel

app = FastAPI(title="Kafka Chat API")

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',  # Имя сервиса в Docker
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

class Message(BaseModel):
    text: str
    user: str

@app.post("/send-message")
async def send_message(msg: Message):
    data = msg.dict()
    producer.send('chat-topic', data)
    producer.flush()  # Отправь сразу
    return {"status": "sent", "message": data}

@app.get("/")
def root():
    return {"msg": "FastAPI + Kafka готов! POST на /send-message"}
