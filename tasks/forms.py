from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "beschreibung", "arbeitsgruppe","abgeschlossen","geliefert","file"]



class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()