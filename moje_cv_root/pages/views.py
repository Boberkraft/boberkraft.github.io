from django.shortcuts import render
from products.models import Product
# Create your views here.
from django.utils import translation


def home_view(request):
    objects = Product.objects.all()

    context = {
        'objects': objects,
        'cv_link': "CV {} Andrzej Bisewski.pdf".format(translation.get_language()),
    }
    return render(request, 'home.html', context)
