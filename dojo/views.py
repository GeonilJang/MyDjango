from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse


import os
#지정경로 장고 이용하여 정의하기
from django.conf import settings


from .forms import PostForm
from .models import Post

#폼을 정의해준다
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            """방법1)
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()"""

            """방법2)post = Post(title=form.cleaned_data['title'],content=form.cleaned_data['content'])
            post.save()"""

            """방법3) post = Post.objects.create(title=form.cleaned_data['title'],content = form.cleaned_data['conten'])"""




            """방법4)post = Post.objects.create(**form.cleaned_data) 방법4를응용 """
            post = form.save()

            return redirect('/dojo/') #namespace:name
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',{
        'form':form
    })






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
