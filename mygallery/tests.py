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

    def test_get_category_by_id(self):
        with self.assertRaises(Category.DoesNotExist):
            # Category.get_category_by_id('example@gmail.com')
            Category.objects.get(name='flower')



class ImageTestCase(TestCase):
    def setUp(self):
        self.travel = Category(name='Tourism', id=1)
        self.nakuru = Location(name='Nakuru', id=1)
        self.nakuru.save_location()
        self.travel.save_category()
        self.image = Image(id=1,name='Birthday', description='My 50th birthday...', location=self.nakuru, category=self.travel)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    # def test_update_single_category(self):
    #     self.image.save_image()
    #     image_change = Image.update_image()
    #     self.assertEquals(image_change, 1)

    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertEquals(len(images), 0)

    def test_get_image_id(self):
        self.image.save_image()
        id = 1
        image = Image.get_image_by_id(id)
        self.assertEquals(len(image), 1)

    def test_filter_by_location(self):
        self.image.save_image()
        self.nakuru.save_location()
        location = Image.filter_by_location(1)
        self.assertEquals(len(location), 1)

    def test_search_image(self):
        self.image.save_image()
        self.travel.save_category()
        image = Image.search_image(1)
        self.assertTrue(len(image) == 1)

        


    