from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import CalculationTask
from chat.consumers import channel_publish
import math
import time


@shared_task
def power_calculation(task_id, power):
    task = CalculationTask.objects.get(pk=task_id)
    task.status = '执行中'
    task.save()
    task.result = math.exp(int(power))
    time.sleep(task.result)
    task.status = '已完成'
    task.save()
    channel_publish('demo', {'task_id': task_id, 'result': task.result})
    return task.result

