# Kafka Chat Demo

**Микросервисный чат: FastAPI → Kafka → Kafka UI**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-blue)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-green)](https://docs.docker.com/compose/)
[![Kafka](https://img.shields.io/badge/Kafka-Production-orange)](https://kafka.apache.org/)
[![CI/CD](https://github.com/iosifkikriasvili/kafka-chat-demo/actions/workflows/loadtest.yml/badge.svg)](https://github.com/iosifkikriasvili/kafka-chat-demo/actions)


### Запуск

docker compose up -d


### Отправка сообщения

curl -X POST "http://localhost:8000/send-message" \
     -H "Content-Type: application/json" \
     -d '{"text": "Привет!", "user": "QA"}'


### Как посмотреть сообщения в Kafka UI
http://localhost:8081
Clusters → chat-topic → Messages
