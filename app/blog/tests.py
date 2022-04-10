import unittest
from django.test import Client
from django.test import TestCase
from .models import Author,Tag
# Create your tests here.

class IndexViewTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_loads(self):
        """
        Test that the index page loads
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob', email="bob@test.com")

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Tag.objects.create(caption="test")