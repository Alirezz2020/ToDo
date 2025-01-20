from django.test import TestCase
from django.urls import reverse

class HomePageViewTests(TestCase):

    def test_home_page_status_code(self):
        # Test if the home page returns a 200 status code
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        # Test if the correct template is used
        response = self.client.get(reverse('home:home'))
        self.assertTemplateUsed(response, 'home/index.html')

    def test_home_page_content(self):
        # Test if specific content is rendered in the template
        response = self.client.get(reverse('home:home'))
        self.assertContains(response, "Welcome to the ToDo App!")
