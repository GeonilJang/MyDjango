from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ValidationError
# Create your models here.

def len_validator(value):
    if(len(value) > 80):
        raise ValidationError('최대 글자 수는 100자를 초과 할 수 없습니다.')

class Product(models.Model):
    user= models.CharField(max_length=20, verbose_name="작성자", help_text="작성자를 입력해 주세요.")
    title = models.CharField(max_length=100, verbose_name="제목", help_text="포스팅 제목을 입력해주세요. 최대 100자 내외.", validators=[len_validator])
    content = models.TextField(verbose_name="내용")
    user_agent = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ['-id'] #id로 내림 차순 정렬을 기본으로 정렬하겠다. [안에 여러 조건을 줄 수는 있지만 1가지 조건을사용하는 것을 추천]
      
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.id])

class After(models.Model):
    product = models.ForeignKey(Product)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
