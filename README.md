# Kafka Chat Demo

Микросервисная система чата: **FastAPI → Kafka → Kafka UI**

## Стек технологий
- Docker Compose (4 контейнера)
- Apache Kafka + Zookeeper (wurstmeister)
- FastAPI REST API (producer)
- Kafka UI (мониторинг сообщений)
- GitHub Actions (CI/CD ready)

## Запуск
```bash
docker compose up -d
