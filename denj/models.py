from django.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField
from django.contrib.auth.models import User

# Create your models here.

class Denj(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',null=True)
    # location = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    gears = models.CharField(max_length=100)
    # likes = models.ManyToManyField(User, related_name='denj_like')
    created = models.DateTimeField(auto_now_add=True) 
    # discoverer = models.ForeignKey(
    #     'users.User', related_name='denjs', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Review(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/',default=[])
    created = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(User, related_name='review_like')
    # discoverer = models.ForeignKey(
    #     'users.User', related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.title   



