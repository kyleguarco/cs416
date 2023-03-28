from django.contrib import admin

from .models import TaskModel
from .forms import TaskForm

# Register your models here.
admin.register(TaskModel)
admin.register(TaskForm)
