from django.test import TestCase
from .forms import ItemForm


# Create your tests here.
class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # instantiate a form with the name field not filled in and test
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # instantiate a form with the name field not filled in and test
        form = ItemForm({'name': 'test todo item'})
        self.assertTrue(form.is_valid())

    def test_field_are_explicit_in_form_meta_class(self):
        # test to ensure requisite field are displayed in form
        # ensures our form does not display information we don't want it to
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
