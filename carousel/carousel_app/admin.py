from django.contrib import admin
from .models import Carousel, Image
from .forms import CarouselForm, ImageForm

class CarouselAdmin(admin.ModelAdmin):
    # form to provide custom data validation for carousels in admin
    form = CarouselForm

class ImageAdmin(admin.ModelAdmin):
    # form to provide custom data validation for carousels in admin
    form = ImageForm

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Image, ImageAdmin)