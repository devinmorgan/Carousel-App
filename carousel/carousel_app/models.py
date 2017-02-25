from django.db import models

from django.db import models

class Carousel(models.Model):
    name = models.CharField()
    image_count = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Carousel: %s" % self.name

class Image(models.Model):
    name = models.CharField()
    carousel = models.ForeignKey(Carousel, related_name="pictures")
    carousel_order_index = models.IntegerField()
    image_url = models.CharField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Image: %s" %self.name
