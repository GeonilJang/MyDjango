from django.shortcuts import render , get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_list(request):

    element = Product.objects.all()

    return render(request, 'product/product_list.html',{
        "elements":element
    })

def product_detail(request, id):
    element = get_object_or_404(Product, id=id)
    return render(request, 'product/product_detail.html',{
        "element":element
    })

def product_new(request):
    if request.method =="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(product)
    else:
        form = ProductForm()
    return render(request, 'product/product_new.html',{
        "form":form,
    })


def product_edit(request, id):
    element = get_object_or_404(Product, id=id)
    if request.method =="POST":
        form = ProductForm(request.POST, request.FILES, instance=element)
        if form.is_valid():
            product = form.save()
            return redirect(product)
    else:
        form = ProductForm(instance=element)
    return render(request, 'product/product_new.html',{
        "form":form,
    })
