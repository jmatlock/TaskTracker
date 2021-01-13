from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Task

# Create your views here.
class HomePageView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'all_tasks_list'


class AboutPageView(TemplateView):
    template_name = 'about.html'