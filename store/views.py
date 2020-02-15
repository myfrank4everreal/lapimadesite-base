from django.shortcuts import render
from .models import Products
from .models import GigZone
from .models import BusinesZone
from .models import GameZone




def index(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'store/index.html', context)


def businessZone(request):
    bizproducts = BusinesZone.objects.all()
    context = {'bizproducts':bizproducts}
    return render(request, 'store/businesszone.html', context)


def gigZone(request):
    gigproducts = GigZone.objects.all()
    context = {'gigproducts':gigproducts}
    return render(request, 'store/gigzone.html', context)

def gameZone(request):
    gameproducts = GameZone.objects.all()
    context = {'gameproducts':gameproducts}
    return render(request, 'store/gamerszone.html', context)






def Services(request):
    context = {}
    return render(request, 'store/Services.html', context)



def addContact(request):
    context = {}
    return render(request, 'store/addContact.html', context)


def Blog(request):
    context = {}
    return render(request, 'store/Blog.html', context)


def About(request):
    context = {}
    return render(request, 'store/about.html', context)