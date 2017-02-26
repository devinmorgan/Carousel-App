from rest_framework import serializers
from .models import Carousel, Image

class CarouselSerializer (serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ('id', 'name')