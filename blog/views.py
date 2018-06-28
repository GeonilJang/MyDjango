from django.shortcuts import render
from .models import Post
from django.db.models import Q
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
