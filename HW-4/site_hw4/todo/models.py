from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task = models.TextField(max_length=150)
    created = models.DateTimeField()
    completed = models.BooleanField()
