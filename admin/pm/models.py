from django.db import models

# Create your models here.
class Pmforms(models.Model):
    name = models.CharField(max_length=200)
    staff_id = models.IntegerField()
    serial_number = models.IntegerField()
    dept_name = models.CharField(max_length=200)

class USer(models.Model):
    pass