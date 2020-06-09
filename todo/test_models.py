from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        # test that our todo items will be created by default with
        # the done status of false.
        item = Item.objects.create(name='test todo item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='test todo item')
        self.assertEqual(str(item), 'test todo item')