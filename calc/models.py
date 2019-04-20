import uuid
from django.db import models


class CalculationTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    power = models.IntegerField(default=0)
    
    STATUS = (
        ('Created', '已创建'),
        ('Executing', '执行中'),
        ('Completed', '已完成'),
    )
    status = models.CharField(max_length=20, choices=STATUS, default='Created', verbose_name='状态')
    result = models.FloatField(default=0)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Task: {self.name}, Result: {self.result}'
