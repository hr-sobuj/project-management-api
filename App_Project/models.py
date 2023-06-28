from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length = 5550)
    project_description = models.CharField(max_length = 5550)

    def __str__(self):
        return self.project_title

class Task(models.Model):
    project_title = models.ForeignKey(Project, on_delete=models.CASCADE)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length = 1000)
    task_type = models.CharField(max_length = 1000)
    task_deadline = models.CharField(max_length = 1000)
    task_status=models.CharField(max_length = 1000)
    

    def __str__(self):
        return str(self.project_title)

# class Activity(models.Model):
#     project_title = models.ForeignKey(Project, on_delete=models.CASCADE)
#     developer = models.ForeignKey(User, on_delete=models.CASCADE)
#     activity = models.CharField(max_length = 5550)

#     def __str__(self):
#         return str(self.project_title)