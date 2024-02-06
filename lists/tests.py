from django.test import TestCase
from django.http import HttpRequest
from .views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_use_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home.html")

    def test_can_save_post_request(self):
        response = self.client.post("/", data={"new_item": "A new item"})
        self.assertContains(response, "A new item")
        self.assertTemplateUsed(response, "lists/home.html")
