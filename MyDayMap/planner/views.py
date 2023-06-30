from django.views.generic import ListView, CreateView
from .models import Task, Event
from .forms import TaskForm, EventForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = '/tasks/'

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_create.html'
    success_url = '/events/'
