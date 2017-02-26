from django.db import models

from django.db import models

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    auto_advance_timer = models.IntegerField(default=-1)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Carousel: %s" % self.name

class Image(models.Model):
    name = models.CharField(max_length=100)
    carousel = models.ForeignKey(Carousel, related_name="pictures")
    carousel_position_index = models.IntegerField(default=-1)
    image_url = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Image: %s" %self.name
