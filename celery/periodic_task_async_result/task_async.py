from __future__ import absolute_import, unicode_literals
from .celery import app

import time


@app.task
def task(duration):
    time.sleep(duration)
    return duration
    # print('async task finished')
