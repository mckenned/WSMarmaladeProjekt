from django.db import models

# Create your models here.
class Ingredients (models.Model):
    Name = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)

    object = models.Manager()
