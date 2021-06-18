from django.db import models
from django.db.models.base import Model
# from datetime import datetime

# Create your models here.
class TeleGroups(models.Model):
    # Sno=models.IntegerField(primary_key=True)
    Yourname=models.CharField(max_length=30)
    Groupname=models.CharField(max_length=30)
    Groupdesc=models.CharField(max_length=100)
    Groupimg=models.ImageField(upload_to='images/')
    times=models.DateField()
    
    def __str__(self) :
        return self.Yourname
    
class Names(models.Model):
    name=models.CharField(max_length=50)