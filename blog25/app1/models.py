from django.db import models

# Create your models here.
class Actor(models.Model):

    Actor_name = models.CharField(max_length=50)
    Actor_des = models.TextField()