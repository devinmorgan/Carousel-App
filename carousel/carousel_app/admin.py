from django.contrib import admin
from .models import Carousel, Image
from .forms import CarouselAdminForm, ImageAdminForm

class CarouselAdmin(admin.ModelAdmin):
    # form to provide custom data validation for carousels in admin
    form = CarouselAdminForm

class ImageAdmin(admin.ModelAdmin):
    # form to provide custom data validation for carousels in admin
    form = ImageAdminForm

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Image, ImageAdmin)