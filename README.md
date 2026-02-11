# Kafka Chat Demo 🚀

**Микросервисный чат: FastAPI → Kafka → Kafka UI**

[![FastAPI](https://img.shields.io/badge/FastAPI-REST-blue)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-green)](https://docs.docker.com/compose/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-orange)](https://kafka.apache.org/)

## 🎯 Демо

**Отправить сообщение:**
```bash
curl -X POST "http://localhost:8000/send-message" \
     -H "Content-Type: application/json" \
     -d '{"text": "Привет!", "user": "QA"}'
