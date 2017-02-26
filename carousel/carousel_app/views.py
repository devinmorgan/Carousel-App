from .models import Carousel
from rest_framework import viewsets
from .serializers import CarouselSerializer


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all().order_by('created')
    serializer_class = CarouselSerializer

