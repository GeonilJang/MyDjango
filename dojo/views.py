from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView


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
            post.save()
            """

            """방법2)post = Post(title=form.cleaned_data['title'],content=form.cleaned_data['content'])
            post.save()"""

            """방법3) post = Post.objects.create(title=form.cleaned_data['title'],content = form.cleaned_data['conten'])"""




            """방법4)post = Post.objects.create(**form.cleaned_data) 방법4를응용 """
            post = form.save(commit=False)  #지연시키는 방법
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo/new') #namespace:name
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',{
        'form':form
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id) #해당 id에 해당하는 객체를 가져와라
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo/')
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html',{
        'form':form
    })



"""
스텝1 함수기반뷰
"""
# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     return render(request, 'dojo/post_detail.html', {
#         "post":post
#     })


"""
스텝2
"""

# def generic_view_fn(model):
#     def view_fn(request, id):
#         instance = get_object_or_404(model, id=id)
#         instance_name = model._meta.model_name
#         template_name = '{}/{}_detail.html'.format(model._meta.app_label, instance_name)
#         return render(request , template_name,{
#             instance_name : instance,
#         })
#     return view_fn
#
# post_detail = generic_view_fn(Post)



"""
스텝3
"""

#
# class DetailView():
#     def __init__(self, model):
#         self.model  = model
#
#     def get_object(self, *args, **kwargs):
#         return get_object_or_404(self.model, id=kwargs['id'])
#
#     def get_template_name(self):
#         return '{}/{}_detail.html'.format(self.model._meta.app_label, self.model._meta.model_name)
#
#     def dispatch(self, request, *args, **kwargs):
#         return render(request, self.get_template_name(), {
#             self.model._meta.model_name: self.get_object(*args, **kwargs),
#         })
#
#     @classmethod
#     def as_view(cls, model):
#         def view(request, *args, **kwargs):
#             self = cls(model)
#             return self.dispatch(request, *args, **kwargs)
#         return view
#
# post_detail = DetailView.as_view(Post)

"""
스텝4
"""
post_detail = DetailView.as_view(model=Post)










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
