from django.db import models
from django.db.models import Q
from django.db import models


class Ag(models.Model):

    Name = models.CharField(max_length=200)
    Kostenstelle = models.IntegerField()

    def __str__(self):
        return self.Name 
    
class Task(models.Model):

    name = models.CharField(max_length=200)
    beschreibung = models.CharField(blank=True)
    abgeschlossen = models.BooleanField(default=False)
    geliefert = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    arbeitsgruppe = models.ForeignKey(Ag, on_delete =models.CASCADE)
    file = models.FileField(upload_to='task_pdfs/', blank=True, null=True)

    def __str__(self):
        return self.beschreibung
    

    