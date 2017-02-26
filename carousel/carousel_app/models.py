from django.db import models

from django.db import models

class Carousel(models.Model):
    name = models.CharField(max_length=100)
    image_time_interval = models.IntegerField(default=-1)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name

class Image(models.Model):
    name = models.CharField(max_length=100)
    carousel = models.ForeignKey(
        Carousel,
        related_name="carousel",
        on_delete=models.CASCADE
    )
    carousel_position_index = models.IntegerField(default=-1)
    image_url = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" %self.name
