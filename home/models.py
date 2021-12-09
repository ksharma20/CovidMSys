from django.db import models

# Create your models here.
class CData(models.Model):

    total = models.IntegerField(default=0)
    covid = models.IntegerField(default=0)
    treatment = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    dead = models.IntegerField(default=0)
    discharged = models.IntegerField(default=0)
