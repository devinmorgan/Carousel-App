from django import forms
from .models import Carousel, Image
from django.core.exceptions import ValidationError
import re

# form to provide custom data validation for carousels in admin
class CarouselAdminForm(forms.ModelForm):

    class Meta:
        model = Carousel
        exclude = ['created']

    def clean_name(self):
        # Ensure that carousel names only contain alphanumerics and underscores
        if re.search('([^a-zA-Z0-9_]+)', self.cleaned_data['name']):
            raise ValidationError(('Carousel names can only contain alphanumerics and underscores'))
        else:
            return self.cleaned_data['name']


# form to provide custom data validation for images in admin
class ImageAdminForm(forms.ModelForm):
    print("A--------")
    class Meta:
        model = Image
        exclude = ['created']

    def clean_carousel(self):
        # Ensure that each image gets assigned a carousel
        if 'carousel' not in self.cleaned_data:
            raise ValidationError(('Must select a Carousel fo the image'))
        else:
            return self.cleaned_data['carousel']