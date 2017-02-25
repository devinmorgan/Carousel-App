from models import Carousel
from rest_framework import viewsets
from .serializers import CarouselSerializer


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all().order_by('date_created')
    serializer_class = CarouselSerializer

