from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestCase(TestCase):
    def setUp(self):
        self.nakuru = Location(name='Nakuru')

    def test_instance(self):
        self.assertTrue(isinstance(self.nakuru, Location))

    def test_save_method(self):
        self.nakuru.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    
    def test_update_single_location(self):
        self.nakuru.save_location()
        self.assertEquals(Location.objects.filter(name='Nakuru').update(name='Nakuru West'), 1)
        