from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestCase(TestCase):
    def setUp(self):
        self.nakuru = Location(name='Nakuru')

    def test_instance(self):
        self.assertTrue(isinstance(self.nakuru, Location))
