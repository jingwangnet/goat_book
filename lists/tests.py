from django.test import TestCase
from django.http import HttpRequest
from .views import home_page
from .models import Item, List


# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_use_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home.html")

    def test_save_item_when_necessary(self):
        response = self.client.get("/")
        self.assertEqual(0, Item.objects.count())


class NewListTest(TestCase):
    def test_can_save_post_request(self):
        response = self.client.post("/lists/new", data={"new_item": "A new item"})
        self.assertEqual(1, Item.objects.count())
        item = Item.objects.first()
        self.assertEqual(item.text, "A new item")

    def test_redirect_after_post(self):
        response = self.client.post("/lists/new", data={"new_item": "A new item"})
        self.assertRedirects(response, "/lists/the-only-url/")


class ViewListTest(TestCase):
    def test_view_list_use_list_template(self):
        response = self.client.get("/lists/the-only-url/")
        self.assertTemplateUsed(response, "lists/list.html")

    def test_can_display_all_items(self):
        Item.objects.create(text="First item")
        Item.objects.create(text="Second item")
        response = self.client.get("/lists/the-only-url/")
        self.assertContains(response, "First item")
        self.assertContains(response, "Second item")


class ItemModelTest(TestCase):
    def test_create_items_and_retrieves_later(self):
        new_list = List()
        new_list.save()
        first_item = Item()
        first_item.text = "First item"
        first_item.list = new_list
        first_item.save()

        second_item = Item()
        second_item.text = "Second item"
        second_item.list = new_list
        second_item.save()

        self.assertEqual(1, List.objects.count())
        self.assertEqual(2, Item.objects.count())
        saved_list = List.objects.first()
        first_saved_item, second_saved_item = saved_list.item_set.all()

        self.assertEqual(first_saved_item.text, "First item")
        self.assertEqual(first_saved_item.list, new_list)
        self.assertEqual(second_saved_item.text, "Second item")
        self.assertEqual(second_saved_item.list, new_list)
