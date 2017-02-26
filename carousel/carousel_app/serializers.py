from .models import Carousel, Image
from rest_framework import serializers

class ImageSerializer (serializers.Serializer):
    name = serializers.CharField(max_length=100)
    image_url = serializers.CharField(max_length=300)

class CarouselSerializer (serializers.Serializer):
    name = serializers.CharField(max_length=100)
    image_time_interval = serializers.IntegerField()
    images = ImageSerializer(many=True, required=False)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def save(self):
        pass
