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

class Image(models.Model):
    name = models.CharField(max_length=30, default='SOME STRING')
    description = models.TextField()
    location = models.ForeignKey(Location,default=1)
    category = models.ForeignKey(Category, default=1)
