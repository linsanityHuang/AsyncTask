# Generated by Django 2.1.2 on 2019-04-20 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20190420_0228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculationresult',
            name='task',
        ),
        migrations.DeleteModel(
            name='CalculationResult',
        ),
    ]
