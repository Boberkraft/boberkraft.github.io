from django.shortcuts import render
from products.models import Product
# Create your views here.
from django.utils import translation
from django.conf import settings

def home_view(request):
    objects = Product.objects.all()

    context = {
        'objects': objects,
        'cv_link': "cv-{}-Andrzej-Bisewski-n.pdf".format(translation.get_language()),
        'default_language': settings.LANGUAGE_CODE,
    }
    return render(request, 'home.html', context)
