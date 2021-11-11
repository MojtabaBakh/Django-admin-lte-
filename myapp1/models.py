from types import ClassMethodDescriptorType
from django.db import models

# Create your models here.

class Data_list (models.Model):
    name = models.CharField ( max_length=100  , default="none")
    family = models.CharField ( max_length=100 , default="none" )
    mobile = models.IntegerField ( default=0)
    code = models.IntegerField (default=0)
    adress= models.CharField ( max_length=500 , default="none" )
 
