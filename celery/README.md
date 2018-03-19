# Example1: running periodic task along with async tasks

## Use case

You need to schedule a periodic task in which a lot of async tasks need to be executed
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


# Example2: running periodic task along with async tasks with multiple queues

## Use case

An extension of the above use case where multiple periodic tasks need to be scheduled.
Each periodic task and its associated async task are routed to a dedicated queue. Especially,
in async task2, a group of async tasks 3 are executed.

## How to run

### Start celery beat service

```bash
celery -A periodic_task_async beat
```

### Start celery worker1 for queue `async1`

```bash
celery -A periodic_task_async_multiqueue worker -n worker1@%h -Q async1 -P eventlet -c 1000
```

### Start celery worker2 for queue `async2`

```bash
celery -A periodic_task_async_multiqueue worker -n worker2@%h -Q async2 -P eventlet -c 1000
```