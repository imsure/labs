from __future__ import absolute_import, unicode_literals
from .celery import app

import time


@app.task
def task1(duration):
    time.sleep(duration)
    # print('async task finished')


@app.task
def task2(duration):
    time.sleep(duration)
    # print('async task finished')
