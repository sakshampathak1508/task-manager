from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255,blank=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='image/avatar',blank=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255,blank=True)
    desc = models.TextField(blank=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SubTask(models.Model):
    name = models.CharField(max_length=255,blank=True)
    desc = models.TextField(blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name