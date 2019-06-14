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

    def test_delete_method(self):
        self.nakuru.save_location()
        self.nakuru.delete_location()
        locations = Location.objects.all()
        self.assertEquals(len(locations), 0)

class CategoryTestCase(TestCase):
    def setUp(self):
        self.travel = Category(name='Tourism')

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.travel, Category))

    def test_save_method(self):
        self.travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
    def test_update_single_category(self):
        self.travel.save_category()
        self.assertEquals(Category.objects.filter(name='Tourism').update(name='travel'), 1)

    def test_delete_method(self):
        self.travel.save_category()
        self.travel.delete_category()
        categories = Category.objects.all()
        self.assertEquals(len(categories), 0)


