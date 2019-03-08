from django.db import models

# Create your models here.


class GarageSellmodel(models.Model):
    name = models.CharField(max_length=20,default='')
    description = models.CharField(max_length=100)
    price = models.IntegerField(default='')
    imageURL = models.CharField(max_length=500,default='')
