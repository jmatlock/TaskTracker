from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


# Create your views here.
class HomePageView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'all_tasks_list'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = ['summary', 'details', 'category', 'location']


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_edit.html'
    fields = ['summary', 'details', 'category', 'location']


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('index')

class AboutPageView(TemplateView):
    template_name = 'about.html'