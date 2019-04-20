from django.shortcuts import HttpResponse, render, get_list_or_404
from .tasks import power_calculation
from .models import *
import json


def index(request):
    return render(request, 'calc/index.html')


def calc_tasks(request):
    tasks = CalculationTask.objects.filter(read__exact=False)
    result = [dict(id=str(task.id), result=task.result, read=task.read, name=task.name) for task in tasks]
    return HttpResponse(json.dumps(result), content_type="application/json")


def create_task(request):
    if request.method == 'GET':
        name = 'task'
        power = request.GET.get('power')
        
        task = CalculationTask.objects.create(name=name, power=int(power), status='已创建')
        
        power_calculation.delay(str(task.id), power)
        result = {'code': 0, 'task_id': str(task.id), 'task_name': task.name}
        return HttpResponse(json.dumps(result), content_type="application/json")

