from django.db import models


# Create your models here.
class Location(models.Model):

    name = models.CharField(max_length=100, default='SOME STRING')
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model): 
    name = models.CharField(max_length=30, default='SOME STRING')
    def __str__(self):
        return self.name
    
    def save_category(self):
         """
            Method calls save method on an Category instance to save it to the database.
        """
        self.save()
    
    def delete_category(self):
        """
            This method uses delete manager to delete records of categories in the database.
        """
        self.delete()


class Image(models.Model):
    name = models.CharField(max_length=30, default='SOME STRING')
    description = models.TextField()
    location = models.ForeignKey(Location,default=1)
    category = models.ForeignKey(Category, default=1)
    image_locale = models.ImageField(upload_to='images/', default='/home/karangu/Desktop/Gallery/media')
    def __str__(self):
        return self.name

    def save_image(self):
        """
            Method calls save method on an Image instance to save it to the database.
        """
        self.save()

    def delete_image(self):
        """
            This method is used to delete an Image instance from the database by calling delete manager.
        """
        self.delete()


    @classmethod
    def get_image_by_id(cls, id):
        """
            This method allows retrieval of an image using its ID.
        """
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def filter_by_location(cls, location):
        """
            This method allows images to be filtered based on the location they were taken on.
        """
        images = cls.objects.filter(location=location)
        return images

    @classmethod
    def search_image(cls, category):
        """
            This method allows an image to be searched using category primary_key(pk)
        """
        image = cls.objects.filter(category=category)
        return image
    
    class Meta:
        ordering = ['name']
    