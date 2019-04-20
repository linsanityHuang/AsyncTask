### 异步任务实时通知

#### 简介
> 通过celery执行异步任务

> 实例异步为计算e^n, 计算结果为任务的计算时间

> 借助channels将计算结果通知到页面

#### 启动
0.  requirement
> pip install -r requirements.txt
1.  redis
> docker run -p 6379:6379 -d redis:2.8
2.  django
> python manage.py runserver
3.  celery
> celery -A notifications worker -l info -c 3
