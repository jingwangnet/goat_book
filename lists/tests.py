from django.test import TestCase
from django.http import HttpRequest
from .views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_use_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home.html")
