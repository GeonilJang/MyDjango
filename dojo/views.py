from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def dojo_list(request):
    pass

def mysum(request,x=0):
    #request : HttpRequest
    return HttpResponse(sum(map(lambda x : int(x or 0), x.split("/"))))

def info(request, name, age):
    #request : HttpRequest
    return HttpResponse("{}님은 {}살 입니다.".format(name, age))
