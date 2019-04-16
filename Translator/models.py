from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Text(models.Model):
  nazovTextu = models.CharField(max_length=100)
  kapitola = models.CharField(max_length=100)
  strana = models.PositiveIntegerField(default=1)
  riadok = models.PositiveIntegerField(default=1)
  origText = models.TextField(default="n/a")
  otLanguage = models.CharField(max_length=4, default="n/a")
  translatedText = models.TextField(default="n/a")
  ttLanguage = models.CharField(max_length=4,default="n/a")
  
  def __unicode__(self):
    return self.nazov
    

      