from django.db import models
from django import forms


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해 주세요.')


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator], help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.')
    content = models.TextField()
    user_agent = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
