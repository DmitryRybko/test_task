from django.core.management.base import BaseCommand
from ...models import Task


class Command(BaseCommand):
    def handle(self, *args, **options):
        priority_task = Task.choose()
        print(f'приоритетная задача: {priority_task.values()}')
