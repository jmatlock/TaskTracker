from django.urls import path

from .views import HomePageView, AboutPageView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('task/new/', TaskCreateView.as_view(), name='task_new'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete')
]