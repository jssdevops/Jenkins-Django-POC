from django.test import TestCase
from .models import Item

class ItemModelTestCase(TestCase):
    def setUp(self):
        # Create a sample item for testing
        self.item = Item.objects.create(name='Test Item', description='This is a test item')

    def test_item_creation(self):
        # Check if the item was created successfully
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.description, 'This is a test item')

    def test_item_str_representation(self):
        # Check the string representation of the item
        self.assertEqual(str(self.item), 'Test Item')
