from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    print(args, kwargs)
    play_dict = {
        'me': 'Krzysiek',
        'lst': [123, 321, 231],
    }
    return render(request, 'home.html', play_dict)


def product_detail(request):
    obj = Product.objects.get(id=1)
    # context={
    #     'title':obj.title,
    #
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/detail.html', context)
