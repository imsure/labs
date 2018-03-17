from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('periodic_task_async_multiqueue',
             broker='amqp://',
             backend='rpc://',
             include=['periodic_task_async_multiqueue.task_periodic',
                      'periodic_task_async_multiqueue.task_async'])

app.conf.task_routes = {'periodic_task_async_multiqueue.task_async.task1': {'queue': 'async1'},
                        'periodic_task_async_multiqueue.task_async.task2': {'queue': 'async2'}}

app.conf.beat_schedule = {
    'task-periodic-1': {
        'task': 'periodic_task_async_multiqueue.task_periodic.task1',
        'schedule': 5,  # execute every 5 seconds
        'options': {'queue': 'async1'},
    },
    'task-periodic-2': {
        'task': 'periodic_task_async_multiqueue.task_periodic.task2',
        'schedule': 10,  # execute every 10 seconds
        'options': {'queue': 'async2'},
    },
}
app.conf.timezone = 'UTC'

if __name__ == '__main__':
    app.start()
