from django import forms
from .models import Task, Event

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time','end_time']
