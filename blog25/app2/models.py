from django.db import models

# Create your models here.

class Actoress(models.Model):

    Actoress_name = models.CharField(max_length=50)
    Actoress_des = models.TextField()