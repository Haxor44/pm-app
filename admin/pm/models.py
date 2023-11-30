from django.db import models

# Create your models here.
class Pmforms(models.Model):
    name = models.CharField(max_length=200)
    staff_id = models.CharField(max_length=70,default="")
    serial_number = models.CharField(max_length=70)
    dept_name = models.CharField(max_length=200)
    device_name = models.CharField(max_length=200,default="")
    kgn_tag = models.CharField(max_length=70,default="")
class USer(models.Model):
    pass