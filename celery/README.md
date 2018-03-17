# Example running periodic task along with async tasks

## Use case

You need to schedule some periodic tasks in which a lot of async tasks need to be executed
in parallel, e.g., querying databases, making HTTP requests, etc.

## Pre-requisites

- Python 3.4
- Celery 4.1
- eventlet
- RabbitMQ

## How to run

### Start celery beat service

```bash
celery -A periodic_task_async beat
```

### Start celery worker

```bash
celery -A periodic_task_async worker -P eventlet -c 1000
```