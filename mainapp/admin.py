from django.contrib import admin
from .models import Task, Category, Location, WorkItem

# Register your models here.
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(WorkItem)