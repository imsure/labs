from __future__ import absolute_import, unicode_literals
from celery import group
from .celery import app
from . import task_async

import time


@app.task
def task():
    print('periodic task triggered')
    job = group(task_async.task.s(i/1000) for i in range(100, 2000, 100))
    res = job.apply_async()
    while not res.ready():  # wait until all async tasks have completed
        time.sleep(0.5)
    print('all async tasks have completed')
