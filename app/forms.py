from app.models import *
from django import forms

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'id': 'update-task-title'}),
            'status': forms.Select(attrs={'id': 'update-task-status'}),
        }