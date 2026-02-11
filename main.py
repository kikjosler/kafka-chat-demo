from fastapi import FastAPI
from pydantic import BaseModel
import json
import time
from kafka import KafkaProducer
from fastapi.responses import JSONResponse

app = FastAPI(title="Kafka Chat")

producer = None

def get_producer():
    global producer
    if producer is None:
        time.sleep(5)  # Ждём Kafka
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    return producer

class Message(BaseModel):
    text: str
    user: str

@app.post("/send-message")
async def send_message(msg: Message):
    try:
        prod = get_producer()
        data = msg.dict()
        prod.send('chat-topic', data)
        prod.flush()
        return {"status": "sent", "message": data}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/")
def root():
    return {"msg": "FastAPI + Kafka готов! POST /send-message"}
