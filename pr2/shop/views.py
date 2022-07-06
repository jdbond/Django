from concurrent.futures.process import _python_exit
import email
from itertools import product
from math import ceil
from pydoc import describe
from sqlite3 import paramstyle
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Contact

def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = ceil(n/4)
    # allProds = [[products,range(1,nSlides),nSlides],
    #             [products,range(1,nSlides),nSlides]]

    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html',params)
    
def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"shop/contact.html")

def tracker(request):
    return render(request, 'shop/tracker.html')
    
def search(request):
    return render(request, 'shop/search.html')

def productView(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request, 'shop/productView.html',{'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')    