from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    timeStarted = models.DateTimeField(auto_now_add=True)
    timeFinish = models.DateTimeField()
    
    def __str__(self):
        return self.name

class Owner(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    def __str__(self):
        return self.username