from rest_framework import serializers
from .models import Carousel, Image

class TaskSerializer (serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ('id', 'carousel_name')