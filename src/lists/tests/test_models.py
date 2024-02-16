from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List


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

    def test_cannot_save_empty_list_items(self):
        mylist = List.objects.create()
        item = Item(list=mylist, text="")
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f"/lists/{list_.pk}/")
