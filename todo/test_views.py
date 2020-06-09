from django.test import TestCase
from .models import Item

# test here that views return a successful HTTP response and
# that they're using the proper templates.
class testViews(TestCase):

    def test_get_todo_list(self):
        # use a built-in HTTP client that comes with the Django
        # testing framework- use '/' to test home page - status
        # code 200 = success.
        # we can also check that the correct template was used.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_lists.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # edit item URL containts item id, so create Item and test against it
        item = Item.objects.create(name='Test Todo Item')
        # Python f string - add an f before the opening quotation mark.And then
        # anything we put in curly brackets will be interpreted and turned into
        # part of the string.
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # create item, add it and test is the site successfully redirects
        # to home page
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # extra check - search for item id and check if the length of the
        # filter is equal to zero (i.e. empty)
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
