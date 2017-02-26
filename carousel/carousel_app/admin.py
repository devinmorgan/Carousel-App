from django.contrib import admin
from .models import Carousel, Image
from .forms import CarouselForm, ImageForm


class CarouselAdmin(admin.ModelAdmin):
    form = CarouselForm

class ImageAdmin(admin.ModelAdmin):
    form = ImageForm

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Image, ImageAdmin)

