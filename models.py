from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.Model(max_length=50)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    