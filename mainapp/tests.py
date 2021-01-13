from django.test import TestCase
from .models import Task, Category, Location, WorkItem

# Create your tests here.

class SimpleWebTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)


class TaskModelTest(TestCase):
    def setUp(self):
        Location.objects.create(name='Garage')
        Category.objects.create(name='Declutter')
        Task.objects.create(summary='Declutter garage',
                            details='Declutter garage',
                            category=Category.objects.get(id=1),
                            location=Location.objects.get(id=1))
        # TODO: add WorkItem to setUp

    def test_task_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.summary}'
        self.assertEqual(expected_object_name, 'Declutter garage')