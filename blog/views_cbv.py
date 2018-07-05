from django.views.generic import CreateView,ListView,DeleteView,DetailView, UpdateView, CreateView
from django import forms
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=10)
post_detail = DetailView.as_view(model=Post)
post_edit = UpdateView.as_view(model=Post, fields='__all__')
post_new = CreateView.as_view(model=Post, fields='__all__')
post_delete = DeleteView.as_view(model=Post, success_url='/blog/')



"""
원래대로라면
#blog/forms.py에 구현 해줘야한다 지금은 연습차원
"""

#기본 모델을 post로 필드는 전부 선택하겠다는 의미  "meta"
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields  = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
#success_url을 = "//" 원래 적어 줘야 하지만  제공안해주면

# post_new = PostCreateView.as_view()
