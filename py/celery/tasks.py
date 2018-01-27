# How to run a celery task:
# 1. make sure RabbitMQ is running in the background
# 2. $ celery -A tasks worker --loglevel=info

from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='pyamqp://guest@localhost//')
app.conf.beat_schedule = {
    'add-every-second': {
        'task': 'tasks.add',
        'schedule': 2.0,
        'args': (16, 16)
    },
    'add-every-2-seconds': {
        'task': 'tasks.multiply',
        'schedule': 2.0,
        'args': (4, 6)
    },
}
app.conf.timezone = 'UTC'


@app.task
def add(x, y):
    print('{} + {} = {}'.format(x, y, x + y))
    return x + y


@app.task
def multiply(x, y):
    print('{} * {} = {}'.format(x, y, x * y))
