from django.db import models
from django.db.models import Q

from django.db import models


class Arbeitsgruppe(models.Model):

    Name = models.CharField(max_length=200)
    Kostenstelle = models.IntegerField()

    def __str__(self):
        return self.Name  
        
class Task(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    ag = models.ForeignKey(Arbeitsgruppe, on_delete =models.CASCADE)


    
    def __str__(self):
        return self.title