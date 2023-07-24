from django.db import models

# Create your models here.

class Nombre(models.Model):
    name = models.CharField(max_length=250)
    age = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name