from django.db import models

# Create your models here.
class PmStaff(models.Model):
    name = models.CharField(max_length=200)

class User(models.Model):
    pass