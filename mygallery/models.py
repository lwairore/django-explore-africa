from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, default='SOME STRING')
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length=30, default='SOME STRING')
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=30, default='SOME STRING')
    description = models.TextField()
    location = models.ForeignKey(Location,default=1)
    category = models.ForeignKey(Category, default=1)
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # @classmethod
    # def update_image(cls):
    #     cls.objects.filter(name='Tourism').update(name='image')

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(location=location)
        return images

    