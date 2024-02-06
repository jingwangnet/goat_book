from django.test import TestCase
from django.http import HttpRequest
from .views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_return_correct_content(self):
        request = HttpRequest()
        respponse = home_page(request)
        content = respponse.content.decode()

        self.assertTrue(content.startswith("<html>"))
        self.assertIn("<title>To-Do lists</title>", content)
        self.assertTrue(content.endswith("</html>"))

    def test_home_page_return_correct_content_2(self):
        response = self.client.get("/")
        self.assertContains(response, "To-Do lists")
