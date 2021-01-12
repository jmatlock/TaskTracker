from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name[:25]


class Location(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name[:25]


class Task(models.Model):
    summary = models.TextField()
    details = models.TextField()
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    location = models.ForeignKey(Location,
                                 on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return self.summary[:50]


class WorkItem(models.Model):
    task = models.ForeignKey(Task,
                             on_delete=models.CASCADE)
    start = models.DateTimeField()
    percent_complete = models.IntegerField()
    modified = models.DateTimeField()
    details = models.TextField()
    archived = models.BooleanField()

    def __str__(self):
        return self.task.summary + 'Task'
