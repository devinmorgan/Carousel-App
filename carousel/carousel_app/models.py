from django.db import models
from django.db import models

class Carousel(models.Model):

    # data fields for Carousel object
    name = models.CharField(max_length=100, unique=True)
    image_time_interval = models.IntegerField(default=-1)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

class Image(models.Model):

    # Images will point to Carousel objects
    carousel = models.ForeignKey(
        Carousel,
        related_name="carousel",
        on_delete=models.CASCADE
    )

    # data fields for Image object
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "%s" %self.name
