from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('periodic_task_async',
             broker='amqp://',
             backend='rpc://',
             include=['periodic_task_async.task_periodic', 'periodic_task_async.task_async'])

app.conf.beat_schedule = {
    'task-periodic': {
        'task': 'periodic_task_async.task_periodic.task',
        'schedule': 5,  # execute every 5 seconds
    },
}
app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()
