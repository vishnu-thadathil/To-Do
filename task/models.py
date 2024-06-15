from django.db.models import (AutoField, CharField, DateTimeField, Model,
                              SmallIntegerField, TextField)

from .constants import REPEAT_CHOICES


class Task(Model):
    task_id = AutoField(primary_key=True)
    name = CharField(max_length=200, default=None)
    due_date = DateTimeField()
    completed = SmallIntegerField(default=0)
    repeat = CharField(choices=REPEAT_CHOICES, max_length=50)
    description = TextField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted = SmallIntegerField(default=0)
