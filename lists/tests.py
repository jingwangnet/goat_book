from django.test import TestCase
from django.http import HttpRequest
from .views import home_page
from .models import Item


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_use_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home.html")

    def test_can_save_post_request(self):
        response = self.client.post("/", data={"new_item": "A new item"})
        self.assertEqual(1, Item.objects.count())
        item = Item.objects.first()
        self.assertEqual(item.text, "A new item")
        self.assertRedirects(response, "/")

    def test_save_item_when_necessary(self):
        response = self.client.get("/")
        self.assertEqual(0, Item.objects.count())

    def test_can_display_all_items(self):
        Item.objects.create(text="First item")
        Item.objects.create(text="Second item")
        response = self.client.get("/")
        self.assertContains(response, "First item")
        self.assertContains(response, "Second item")


class ItemModelTest(TestCase):
    def test_create_items_and_retrieves_later(self):
        first_item = Item()
        first_item.text = "First item"
        first_item.save()

        second_item = Item()
        second_item.text = "Second item"
        second_item.save()

        self.assertEqual(2, Item.objects.count())
        first_saved_item, second_saved_item = Item.objects.all()

        self.assertEqual(first_saved_item.text, "First item")
        self.assertEqual(second_saved_item.text, "Second item")
