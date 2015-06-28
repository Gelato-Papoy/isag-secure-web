from django.db import models

# Create your models here.
class Messages(models.Model):
    user = models.CharField(max_length=30)
    talk = models.CharField(max_length=30)
    message = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)