from django.db import models
from django.forms import ValidationError
import re



# Create your models here.





#경도위도 검증 함수 구현하여 아래 모델에 적용하기
def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid Lnglat Type')



class Post(models.Model):
    STATUS_CHOICES1 = ( #2018-06-28
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdraw'),
    )
    STATUS_CHOICES2 = ( #2018-06-28
        ('g', 'Good'),
        ('b', 'Bad'),
        ('s', 'Sad'),
    )
    author = models.CharField(max_length=20, verbose_name="작성자")
    title = models.CharField(max_length=100,
                             # choices=(
                             #     ('제목1','제목1 레이블'), #선택 박스를 넣어 줄 수 있다
                             #     ('제목2','제목2 레이블'),
                             #     ('제목3','제목3 레이블'),
                             #     )
                             verbose_name="제목", help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.') #길이제한
    content = models.TextField(verbose_name="내용") #길이제한 없음
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, validators = [lnglat_validator] ,help_text="경도/위도 포맷으로 입력." ,blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES1, default='d') #2018-06-28
    tag_set = models.ManyToManyField('Tag')
    feeling = models.CharField(max_length=1, choices=STATUS_CHOICES2, default='g', verbose_name="기분")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ['-id'] #id로 내림 차순 정렬을 기본으로 정렬하겠다. [안에 여러 조건을 줄 수는 있지만 1가지 조건을사용하는 것을 추천]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post) # post 모델에 대한 외래키로 쓰겠다.
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
