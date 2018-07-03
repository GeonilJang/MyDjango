from django.shortcuts import render , get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
# Create your views here.



from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'pro/user_list.html', { 'users': users })




def product_list(request):

    element = Product.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(element, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'product/product_list.html',{
        "elements":element,
        'users': users
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
            messages.success(request, "새 글이 등록되었습니다.")
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
            messages.success(request, "포스팅을 수정했습니다.")
            return redirect(product)
    else:
        form = ProductForm(instance=element)
    return render(request, 'product/product_new.html',{
        "form":form,
    })
