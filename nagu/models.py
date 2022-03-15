from django.db import models

# Create your models here.
class Good(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    village=models.CharField(max_length=30)