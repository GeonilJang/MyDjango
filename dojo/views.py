from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse


import os
#지정경로 장고 이용하여 정의하기
from django.conf import settings

# Create your views here.
def dojo_list(request):
    pass

def mysum(request,x=0):
    #request : HttpRequest
    return HttpResponse(sum(map(lambda x : int(x or 0), x.split("/"))))

def info(request, name, age):
    #request : HttpRequest
    return HttpResponse("{}님은 {}살 입니다.".format(name, age))
        #클라이언트가 받는 응답이 됩니다.


##ep4에 적은 내용실습
#ex1
def post_list1(request):
    name="공유"
    response = ("""
                <h1>Hello Python with Django</h1>
                <p>{name}</p>
                <p>여러분의 친구가 되어 드리겠습니다.</p>
                """.format(name=name))
    return HttpResponse(response)

#ex2
def post_list2(request):
    name="공유"
    return render(request, 'dojo/post_list2.html',{'name':name})


#ex3 json형식으로 응답하기
def post_list3(request):
    return JsonResponse({
        'message':'안녕, 파이썬&장고',
        'items' : ['파이썬','장고','Celery','Azure','AWS']
    }, json_dumps_params={'ensure_ascii':False})

#ex4 엑셀 다운로드
def post_list4(request):
    #filepath="C:/Users/Geonil/Django_Geonil_Web/post.xlsx"
    filepath = os.path.join(settings.BASE_DIR, 'post.xlsx')

    filename = os.path.basename(filepath)
    with open (filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel') #default 'text/html'
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return response
