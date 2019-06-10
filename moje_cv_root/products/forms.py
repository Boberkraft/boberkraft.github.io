from django import forms
from .models import Product
from django.conf import settings
import os

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'title',
            'image',
            'url',
            'description',
            'stack',
            'visible',

        )


    # def clean_image(self, *args, **kwargs):
    #     image = self.cleaned_data.get("image")
    #     new = image.replace(os.path.join(
    #         settings.BASE_DIR,
    #         settings.STATICFILES_DIRS[0]),
    #         '')
    #     print(new)
    #     return new
