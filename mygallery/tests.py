from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationTestCase(TestCase):
    """
        This testcase:
            1. Defines setUp method that initializes Location instance,self.nakuru, that will be used a test instance.
            2. Defines test_instance method that tests if the instances created by the setUp method is an instance of Location.
            3. Defines test_save_method method that tests the save_location method to assertain that it is capable of adding an instance to the database.
            4. Defines test_update_single_location method tests the update manager.
            5. Defines test_delete_method that tests the delete_location method
    """
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
    """
        This testcase:
            1. Defines setUp method that initializes Category instance,self.travel, that will be used a test instance.
            2. Defines a tearDown method that deletes all Category and Location instances
            3. Defines test_instance method that tests if the instances created by the setUp method is an instance of Category.
            4. Defines test_save_method method that tests the save_category method to assertain that it is capable of adding an instance to the database.
            5. Defines test_update_single_category method tests the update manager.
            6. Defines test_delete_method that tests the delete_category method    
    """
    
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
    """
        This testcase:
            1. Defines setUp method that initializes Image instance,self.image, self.travel, self.nakuru that will be used a test instance.
            2. Defines tearDown method that deletes Image, Location, Category instances.
            3. Defines test_instance method that tests if the instances created by the setUp method is an instance of Image.
            4. Defines test_save_method method that tests the save_image method to assertain that it is capable of adding an instance to the database.
            5. Defines test_delete_method that tests the delete_image method
            6. Defines test_get_image_id that tests get_image_by_id method.
            7. Defines test_filter_by_location that tests filter_by_location.
            8. Defines test_search_image that tests search_image method.
    
    """
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

        


    