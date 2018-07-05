from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()  #폼필드 추가한 것으로 직접 데이터베이스에 저장해주려면??
    address = forms.CharField()


    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save() #부모의 세이브를 호출 해줄 것이

        Profile.objects.create(
                user = user,
                phone_number = self.cleaned_data['phone_number'],
                address = self.cleaned_data['address']
            )

        return user


class LoginForm(AuthenticationForm):

    #기존에 있던 로긴 폼에 내가 추가로 필드 하나 넣어 준것이다.
    answer = forms.IntegerField(label='3+3=?')

    #해당 필드에 대해서 clean_해당필드가 is_valid() 할때 실행 된다.
    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('정답이 아닙니다.')
        return answer #항상 클린 값에는 리턴이 존제 해야한다.
