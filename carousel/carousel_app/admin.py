from django.contrib import admin
from .models import Carousel, Image
from .forms import CarouselAdminForm, ImageAdminForm

class CarouselAdmin(admin.ModelAdmin):
    form = CarouselAdminForm

class ImageAdmin(admin.ModelAdmin):
    form = ImageAdminForm

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Image, ImageAdmin)