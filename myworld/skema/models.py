from django.db import models

# Create your models here.
class Skema(models.Model):
  navn = models.TextField()
  gruppe = models.TextField()
  mandag = models.TextField(blank=True)
  tirsdag = models.TextField(blank=True)
  onsdag = models.TextField(blank=True)
  torsdag = models.TextField(blank =True)
  fredag = models.TextField(blank=True)
  pligter = models.TextField(blank=True)

class Tlf(models.Model):
  navn = models.TextField()
  tlf = models.TextField(blank=True) 
  adresse = models.TextField(blank=True)
  arbejde = models.TextField (blank=True)

