from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from model_utils import Choices


class Task(models.Model):
    STATUS = Choices("created", "started", "stopped")

    priority = models.SmallIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(100), ])
    status = models.CharField(choices=STATUS, default=STATUS.created, max_length=20)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    responsible = models.ForeignKey('Responsible', on_delete=models.CASCADE, )

    def save(self, *args, **kwargs):
        print("Overriding create behavior")
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def delete(self, *args, **kwargs):
        print("Overriding delete/destroy behavior")
        super().delete(*args, **kwargs)  # Call the "real" delete() method.

    @classmethod
    def choose(cls):
        """selects higher priority task with statuses 'created' and 'stopped', and with the earliest creation date"""
        # выбираем все задачи со статусом created и stopped (исключая все со статусом started)
        tasks_by_status = cls.objects.filter(~models.Q(status="started"))
        highest_priority = tasks_by_status.aggregate(models.Max('priority'))
        priority_tasks = tasks_by_status.filter(priority=highest_priority['priority__max'])
        earlier_date = priority_tasks.aggregate(models.Min('creation_date'))
        older_priority_task = priority_tasks.filter(creation_date=earlier_date['creation_date__min'])
        return older_priority_task.values()


class Responsible(models.Model):
    name = models.CharField(max_length=40)
