from django import forms
from .models import Task
#class for Tasks form model
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
