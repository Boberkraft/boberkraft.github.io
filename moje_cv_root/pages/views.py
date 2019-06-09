from django.shortcuts import render
from products.models import Product
# Create your views here.

def home_view(request):
    objects = Product.objects.all()
    context = {
        'objects':objects,
    }
    return render(request, 'home.html', context)