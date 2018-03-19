from __future__ import absolute_import, unicode_literals
from celery import group

from .celery import app

import time


@app.task
def task1(duration):
    time.sleep(duration)
    # print('async task1 finished')


@app.task
def task2(duration):
    # print('async task 2 triggered')
    job = group(task3.s(2 * duration) for i in range(0, 10))
    res = job.apply_async()
    while not res.ready():  # wait until all async tasks have completed
        # print('status: {}'.format(res.ready()))
        time.sleep(0.2)
    # print('async task 2 finished')


@app.task
def task3(duration):
    time.sleep(duration)
