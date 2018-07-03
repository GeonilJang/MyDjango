from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.db.models import Q
from django.http import Http404
from django.conf import settings
from .forms import PostForm
# Create your views here.
def post_list(request):

    qs = Post.objects.all()
    q = request.GET.get('q','')  #-> 해당 함수 호출 될 때 파라미터 q에 해당 하는 값이 있다면 값을 가져와라
    if q:
        qs = qs.filter( Q(title__icontains=q) | Q(content__icontains=q) )
                            # form 테그를 이용하여 파라미터를 던져서 해당 주소로 갈때 실행 되는 함수가
                             #이 함수 이기 때문에 render와 동일한 장소에 쿼리 처리 를 보여주고 있구만.
    return render(request, 'blog/post_list.html',{
        'post_list':qs,
    })

#view.py에 쿼리셋을 정의하고 데이터를 데이터 베이스로 부터 가져오기 실습



def post_detail(request, id):

    post = get_object_or_404(Post, id=id) # 아래 4줄과 동일한 1줄이다
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404
    return render(request, 'blog/post_detail.html',{
        'post':post,
    })



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html',{
        "form":form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html',{
        "form":form,
    })
