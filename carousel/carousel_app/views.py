from .models import Carousel, Image
from rest_framework import viewsets, generics
from .serializers import CarouselSerializer, ImageSerializer


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all().order_by('created')
    serializer_class = CarouselSerializer

class ImageList(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        carousel_name = self.kwargs['carousel_name']
        return Image.objects.filter(carousel__name=carousel_name).order_by('carousel_position_index')