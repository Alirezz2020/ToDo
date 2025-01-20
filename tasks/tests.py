from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Task
from .forms import TaskForm


class TaskURLsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Creating a sample user for authentication
        cls.user = get_user_model().objects.create_user(username='testuser', password='password123')

        # Creating a sample task for testing views and associating it with the user
        cls.task = Task.objects.create(
            title='Sample Task',
            description='Sample Task Description',
            user=cls.user  # Associate the task with the user
        )

    def test_task_list_url(self):
        # Ensure the user is logged in for task list view
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('tasks:task_list'))
        self.assertEqual(response.status_code, 200)

    def test_task_detail_url(self):
        # Ensure the user is logged in for task detail view
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('tasks:task_detail', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_task_create_url(self):
        # Ensure the user is logged in for creating a task
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('tasks:task_create'))
        self.assertEqual(response.status_code, 200)

    def test_task_update_url(self):
        # Ensure the user is logged in for updating a task
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('tasks:task_update', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_task_delete_url(self):
        # Ensure the user is logged in for deleting a task
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('tasks:task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_task_search_url(self):
        # Ensure the user is logged in for search view
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('tasks:task_search'))
        self.assertEqual(response.status_code, 200)


class TaskFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = get_user_model().objects.create_user(username='testuser', password='password123')

    def test_form_valid(self):
        # Test valid data
        form_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'completed': False
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        # Test missing required fields (title)
        form_data = {
            'title': '',
            'description': 'Test Description',
            'completed': False
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_form_save(self):
        # Test form save with valid data and associate the task with the user
        form_data = {
            'title': 'New Task',
            'description': 'New Task Description',
            'completed': False
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Manually assign the user before saving
        task = form.save(commit=False)
        task.user = self.user
        task.save()

        self.assertEqual(task.title, 'New Task')
        self.assertEqual(task.description, 'New Task Description')
        self.assertFalse(task.completed)
        self.assertEqual(task.user, self.user)  # Ensure the task is associated with the user

    def test_form_fields(self):
        # Test that the form includes the correct fields
        form = TaskForm()
        self.assertIn('title', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('completed', form.fields)

    def test_form_completed_default_value(self):
        # Test the default value for the 'completed' field
        form = TaskForm()
        task = form.save(commit=False)
        self.assertFalse(task.completed)









