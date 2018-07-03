#dojo/forms.py
from django import forms
from .models import Post


#유효성 검사 수가하기 3 -> 폼에서는 예외 발생유무로 처리함.
#value에는 폼에서 넘어오는 값을 가지고 유효성 판단을 시작한다
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해 주세요.')

"""
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
"""


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content', "user_agent"]  #전체 필드 지정. 혹은 list 로 읽어올 필드면 지정
        widgets = {
            #커스텀 가능
            'user_agent':forms.HiddenInput,
        }
