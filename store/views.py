from django.shortcuts import render
from .models import Products




def index(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'store/index.html', context)


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