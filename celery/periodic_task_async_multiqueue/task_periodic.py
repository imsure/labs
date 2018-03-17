from __future__ import absolute_import, unicode_literals
from celery import group
from .celery import app
from . import task_async

import time


@app.task
def task1():
    print('periodic task1 triggered')
    job = group(task_async.task1.s(i/1000) for i in range(100, 2000, 100))
    res = job.apply_async()
    while not res.ready():  # wait until all async tasks have completed
        # print('status: {}'.format(res.ready()))
        time.sleep(0.5)
    print('all async tasks have completed')


@app.task
def task2():
    print('periodic task2 triggered')
    job = group(task_async.task2.s(i/1000) for i in range(100, 2000, 100))
    res = job.apply_async()
    while not res.ready():  # wait until all async tasks have completed
        # print('status: {}'.format(res.ready()))
        time.sleep(0.5)
    print('all async tasks have completed')
