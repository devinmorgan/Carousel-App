from django.db import models

from django.db import models

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    image_count = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Carousel: %s" % self.name

class Image(models.Model):
    name = models.CharField(max_length=100)
    carousel = models.ForeignKey(Carousel, related_name="pictures")
    carousel_order_index = models.IntegerField()
    image_url = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Image: %s" %self.name
