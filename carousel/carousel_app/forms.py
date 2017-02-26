from django import forms
from .models import Carousel, Image
from django.core.exceptions import ValidationError
import re

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        exclude = ['created']

    def clean_carousel(self):
        # Ensure that each image gets assigned a carousel
        if 'carousel' not in self.cleaned_data:
            raise ValidationError(('Must select a Carousel fo the image'))
        else:
            return self.cleaned_data['carousel']

    def clean_carousel_position_index(self):
        if 'carousel' not in self.cleaned_data:
            raise ValidationError(('Invalid image position index'))

        # Ensure that the position index for an image is a valid index in the
        # image list for the carousel
        carousel_image_count = len(Image.objects.filter(carousel__name=self.cleaned_data['carousel']))
        if self.cleaned_data['carousel_position_index'] < 0 or \
                        self.cleaned_data['carousel_position_index'] > carousel_image_count:
            raise ValidationError(('Invalid image position index'))
        else:
            return self.cleaned_data['carousel_position_index']


class CarouselForm(forms.ModelForm):

    class Meta:
        model = Carousel
        exclude = ['created']

    def clean_name(self):
        # Ensure that carousel names only contain alphanumerics and underscores
        if re.search('([^a-zA-Z0-9_]+)', self.cleaned_data['name']):
            raise ValidationError(('Carousel names can only contain alphanumerics and underscores'))
        else:
            return self.cleaned_data['name']