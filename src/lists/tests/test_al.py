from django.test import TestCase
from django.http import HttpRequest
from .views import home_page
from .models import Item, List


# Create your tests here.
class HomePageTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/")

    def test_home_page_use_home_template(self):
        self.assertTemplateUsed(self.response, "lists/home.html")

    def test_save_item_when_necessary(self):
        self.assertEqual(0, Item.objects.count())


class NewListTest(TestCase):
    def setUp(self):
        self.response = self.client.post("/lists/new", data={"new_item": "A new item"})

    def test_can_save_post_request(self):
        self.assertEqual(1, List.objects.count())
        self.assertEqual(1, Item.objects.count())
        item = Item.objects.first()
        new_list = List.objects.first()
        self.assertEqual(item.text, "A new item")
        self.assertEqual(item.list, new_list)

    def test_redirect_after_post(self):
        new_list = List.objects.first()
        self.assertRedirects(self.response, f"/lists/{new_list.pk}/")


class ViewListTest(TestCase):
    def setUp(self):
        self.new_list = List.objects.create()
        self.other_list = List.objects.create()
        self.response = self.client.get(f"/lists/{self.new_list.pk}/")

    def test_view_list_use_list_template(self):
        self.assertTemplateUsed(self.response, "lists/list.html")

    def test_can_display_all_items_that_lists(self):
        self.other_list = List.objects.create()
        Item.objects.create(text="First other item", list=self.other_list)
        Item.objects.create(text="Second other item", list=self.other_list)
        Item.objects.create(text="First item", list=self.new_list)
        Item.objects.create(text="Second item", list=self.new_list)
        self.response = self.client.get(f"/lists/{self.new_list.pk}/")
        self.assertContains(self.response, "First item")
        self.assertContains(self.response, "Second item")
        self.assertNotContains(self.response, "First other item")
        self.assertNotContains(self.response, "Second ohter item")

    def test_view_list_passes_correct_list(self):
        self.assertEqual(self.response.context["list"], self.new_list)


class AddItemTest(TestCase):
    def setUp(self):
        self.list = List.objects.create()
        self.response = self.client.post(
            f"/lists/{self.list.pk}/add", data={"new_item": "A new item"}
        )

    def test_can_save_post_request(self):
        self.assertEqual(1, List.objects.count())
        self.assertEqual(1, Item.objects.count())
        item = Item.objects.first()
        new_list = List.objects.first()
        self.assertEqual(item.text, "A new item")
        self.assertEqual(item.list, new_list)

    def test_redirect_after_post(self):
        self.assertRedirects(self.response, f"/lists/{self.list.pk}/")


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
