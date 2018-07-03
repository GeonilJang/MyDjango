"# MyDjango"


pip install -r requirements.txt 통하여 한번에 사용 라이브러리들을 설치 할수 있습니다.


ep1)
1) 프로젝트 생성
django-admin startproject 프로젝트명
2)장고프로젝트 생성 및 개발서버 구동
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

########################################################################################################
ep2)
1) 앱만들기
  1. python manage.py startapp 앱이름
2) 만든 앱등록
  1. settings.py에 INSTALLED_APPS에서 앱 등록
          INSTALLED_APPS = [
              'django.contrib.admin',
              'django.contrib.auth',
              'django.contrib.contenttypes',
              'django.contrib.sessions',
              'django.contrib.messages',
              'django.contrib.staticfiles',
              'bolg',  <---- 여기처럼
          ]
  2. views.py에 url로 접속시 사용할 함수를 정의 해준다.
  3. urls.py를 만들어 접속 url정의를 해준다 2번과 3번의 순서 바뀌어도 상관없다.
  4. 프로젝트 urls.py에도 등록을 해준다 import 해주는 값들을 잘 보아야 한다
  5. templates/앱이름/.html 파일 만들어주기
  ** 개발서버 옵션
   -> python manage.py runserver
      + 장고서버가 돌고 있는 머신에서만 서버 접속 가능
      + 네트워크를 통해 다른 컴퓨터에서 접속 불가능
   -> python manage.py runserver 0:8000
      + 네트워크를 통해, 같은 네트워크의 다른 컴퓨터에서 접속 가능
      + 외부망에서 접속할려면, 외부 네트워크 설정이 추가로 필요

** settings에 들어가서
ALLOWED_HOSTS = ['bc6f5308.ngrok.io'] 자신의 주소 추가


      ngrok 다운받아서
      ngrok.exe http 현 서버 포트


ep3)
정규표현시
 + 문자열의 패터, 규칙, rule을 정의 하는 방법
 + 이를 통해, 문자열 검색이나 치환작업을 간편하게 처리할 수 있습니다.

 []   : 대괄호 특정 1글자 나올 수 있다
 []{a,b} : 대괄호 뒤에 {} a개 부터 b개 까지

 - 반복 획수 지정 -
  "\d?" : 숫자 0회 또는 1회
  "\d*" : 숫자 0회 이상
  "\d+" : 숫자 1회 이상
  "\d{m}" : 숫자 m글자
  "\d{m,n}" : 슷지 m글자 이상, n글자 이하



 -> 최대 3자리 숫자 : "[0-9]{1,3}" 혹은 "\d{1,3}"
 -> 한글 이름 2글자 혹은 3글자 : "[ㄱ-힣]{2,3}"
 -> 성이 "이"인 이름 : "이[ㄱ-힣]{1,2}"


  val ="01097315256"

  if len(val) == 11 and val[:3] in ("010","011",,,,):
    print("ok")

===>
 import re
 if re.match(r'^01[1-9]\d{6,7}$', val):
  print("ok")
 else:
  print("invalid")


갑자기 본 장고 수업으로 진입~~
-최상의 urlconf settings에 -
 1. ROOT_URLCONF = 'Django_Geonil_Web.urls'
 2. URLConf 정규표현식 매핑연습 #1
  -> (?P<id>\d+) 소괄호의 값을 정규 표현식으로 추출 하겠다라는 의미입니다.
  (?P): 이 역역의 문자열에 정규표현식을 적용해서
  \d+ : \d+패터에 부합된다면
  <id>: id라는 변수명으로 인자를 넘기겠다. -> 뷰에서 사용할 함수의 인자값을 적어주는 것이다
  뷰의 인자로 넘겨받은 값들은 모두 문자열 타입입니다.

########################################################################################################
ep4)

View
 1. URLConf에 매핑된 Callable Object
  -> 첫 번째 인자로 HttpRequest 인스턴스를 받습니다.
     + HttpRequest.GET + HttpRequest.POST + HttpRequest.COOKIES + HttpRequest.FILEs
  -> 필히 HttpResponse 인스턴스를 리턴해야 합니다.
 2. 크게 Funtion Based View와 Class Based View 로 구분
  ->
   FBV 샘플예시
   from django.http import HttpResponse

   - 예시 1번 -
   def post_list1(request):
    'FBV : 직접 문자열로 HTML형식 응답하기'

    name ="공유"
    return HttpResponse("""
    <h1>Hello geonil</h1>
    <p>{name}</P>
    <p>여러분의 친구가 되어 드리겠습니다.</p>
    """.format(name=name))


    - 예시 2번 - (render => 템플릿(HTML) 파일을 쓰다)
    from django.http import HttpResponse
    from django.shortcuts import render
    def post_list2(request):
      name = "공유"
      response = render(request, "dojo/post_list.html", {"name":name})
      return response

    --> 라고 정의 해주면 아래는 예시 1번과 동일한 코드이지만 .html 파일을 만들어서 사용할 수 있다.
    #dojo/post_list.html 에 name 이라는 파라미터의 값으로 name을 넘겨 주겠다.
    <h1>Hello goenil</h1>
    <p>{{name}}</p>
    <p>여러분의 친구가 되어 드리겠습니다.</p>

    ----- 나머지 예시는 views.py 에서 확인 가능 -----

    CBV 샘플예시

    1. django.views.generic
     -> 뷰사용 패턴을 일반화 시켜놓은 뷰의 모음
    2. .as_view() 클래스 함수를 통해 ,FBV를 생성해주는 클래스

    class SampleTemplateView(object):
      @classmethod
      def as_view(cls, templates_name):
        def view_fn(request):
          return render(request, template_name)
        return view_fn

    fbv_view = SampleTemplateView.as_view('dojo/post_list2.html')


    FBV에 해당하는 코드를 CBV로 만들어 보기위하여 vies_cbv.py 에서 작업 -> 이쪽으로 가서 확인을하는것이
    이해도를 높이는데 좋을것으로  판단됩니다.


    최초에는 함수 기반 뷰를 사용하는 것을 추천하며, 나중에 클래스 뷰로 구현 하는 것을 추천


########################################################################################################
ep5) Django Model 과 Model Fields

클라이언트   response<---------|------------->request      서버
                                                                      [SQL]
                                                URLConf -> view -> 모델 <-> db
                                                          ↓        [ORM: sql을 짜는 것이 아니라 코드로
                                                                   데이터 베이스 사용이 간능하게 하는 것]
                                                          템플릿

1. 파이썬 클래스와 데이터베이스 테이블 매핑
 Model : DB테이블 매핑 (엑셀의 워크시)
 Model Instance : DB 테이블의 1Row (엑셀의 필드명 첫 줄과 같은 느낌!)
 blog앱 Post모델 : blog_post 데이터베이스 테이블과 매핑 (저 테이블이 생성이 된다.)
 blog앱 Comment모델 : blog_comment 데이터베이 테이블과 매핑

2. 커스텀 모델 정의 (특정앱/model.py)
 데이터베이스 테이블 구조/타입을 먼저 설계를 한 다음에 모델 정의
 모델 클래스명은 단수형 (Posts 가 아니라 Post)

 ex)
 #blog/models.py
 from django.db import models

 class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

테이블 생성
python manage.py makemigrations blog #데이터 테이블 모델 생성
python manage.py migrate blog # 모델을 데이터 베이스에 적용
blog/admin.py에 내가 현재 만든 데이터베이스 등록 -> admin 페이지에서 확인 할 수 있다
      -> from .models import Post ? geonil
      -> admin.site.register(Post)


## 자주 쓰는 필드 옵션
1. null (DB옵션) : DB 필드에 NULL 허용 여부 (Default : False)
2. unique (DB옵션) : 유일성 여부
3. blank : 입력값 유효성 (validation)검사 시에 emplty 값 허용 여부 (Default : False)
4. default : 디폴트 값 지정. 값이 지정되지 않았을 때 사용.
   - 인자없는 함수 지정 가능. 함수 지정 시에는 매 리턴값이 필요할 때마다 함수를 호출하여 리턴값을 사용
5. choices 사용법은 models.py참고
6. validators : 입력값 유효성 검사를 수행할 함수를 다수 지정
   - 각 필드마다 고유한 validators 들이 이미 등록되어있긷 함.
   - ex) 이메일만 받기, 최대길이 제한, 최소길이 제한 ... 틍



########################################################################################################
ep6) Migrations -> 모델의 내용이 변경되면 테이블에 적용시켜 주는 것!


1. 파이썬 클래스와 데이터베이스 테이블 매핑
 Model : DB테이블 매핑 (엑셀의 워크시)
 Model Instance : DB 테이블의 1Row (엑셀의 필드명 첫 줄과 같은 느낌!)
 blog앱 Post모델 : blog_post 데이터베이스 테이블과 매핑 (저 테이블이 생성이 된다.)
 blog앱 Comment모델 : blog_comment 데이터베이 테이블과 매핑

python manage.py makemigrations blog #데이터 테이블 모델 생성
python manage.py migrate blog # 모델을 데이터 베이스에 적용

id 필드란?
모든 데이터베이스 테이블에는 각 Row의 식별기준인 "기본키 (Primart Key)"가 필요
장고에서는 기본키로서 id 필드 (auto field)가 기본 지정
기본키는 줄여서 "pk"로도 접근가능 (primary key)

########################################################################################################
ep7) Django Shell
+ 장고 프로젝트 설정이 로딩된 파이썬 쉘
 -> 쉘> python manage.py shell
+ 일반 파이썬 쉘을 통해서는, 그냥 장고 환경에 접근 불가
 ->tip ipython이 설치 되어있다면, ipython으로 쉘이 구동
 ->jupyter notebook 과 함께 설치 됩니다.

 Post 모델을 통한 데이터 베이스에 등록한 정보를 가저오는 방법
1.
from blog.models import Post
Post.objects.all().count()
for post in Post.objects.all():
  print(post.id, post.title)

장고 쉘을 이용한 쥬피터 노트북사용법
pip install django-extension
setting.py django_extensions 등록
python manage.py shell_plus --notebook 으로 실행


########################################################################################################
ep8) Django admin
+ staff/superuser 계정에 한해 접근 가능
+ 모델클래스만 등록하면, 조희/추가/수정/삭제 웹 인터페이스가 제공

ex)
#blog/admin
from django.contrib import admin
from blog.models import Post

#등록법 1
admin.site.register(Post) @model만 등록하는 방법

#등록법 2
class PostAdmin(admin, ModelAdmin):
    list_display= ['id','title','content'] #해당 어드민 페이지에서 값을 보여주고 싶을때
admin.site.register(Post, PostAdmin) @model + 화면에 보여주고 싶은 클래스 같이 등록

#등록법 3 : 장식자 형태로 지원
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
      list_display = ['id','title','content_size','geonil','updated_at']
      list_display_links = ['title']
      list_editale = ['title']
      list_per_page = 4

      # 추가할 목록의 항목을 추가해주고 그것을 정의해준후 정의하면된다.
      def content_size(self, post):
            return '{}글자'.format(len(post.content))
        content_size.short_description = "글자수"
        content_size.allow_tags = True

      def geonil(self, post):
            return '{}글자'.format(len("hell"))
        geonil.short_description = "geonil"
        geonil.allow_tags = True


ModelAdmin OPTIONS

1. 어드민 목록에서 변경될 부분을 수행하는 부부
list_display : admin 목록에 보여질 필드목록.
list_display_links : 목록 내에서 링크로 지정할 필드 목록 - 이를 지정하지 않으면, 첫번째 필드에만 인크가 적용
list_editale : 목록상에서 수정할 필드 목록
list_per_page : 디폴트 100 페이지 별로 보여줄 최대 갯수
list_filter : 필터 옵션을 제공할 필드 목록
actions : 목록에서 수행할 actions 목록  ->admin 목록페이지에 체크 박스/action 선택 기능을 만들 수 있다.
 @admin Actions
  대개 선택된 model instance 들에 대해 Bulk UPdate 용도구현
   1. ModelAdmin 클래스내 맴버함수로 action함수를 구현
      -> 맴버함수.short_description을 통해, action 설명 추가
   2. ModelAdmin actions내에 등록




2. 폼을 이용할시 수정이 가해지는 부분
fields : add/change 폼에 노출할 필드 목록
fieldset : add/change 폼에 노출할 필드 목록 (fieldset)
formfield_overrides : 특정 form field에 대한 속정 재정의
form : 디폴트로 모델 클래스에 대한 form class 지정


옵션 사용 예)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','content_size','updated_at']
    list_display_links = ['title']
    list_editale = ['title']
    list_per_page = 4

    actions = ['make_published'] #d여기에 등록 2018-06-28

    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description = "글자수"
    content_size.allow_tags = True

    def make_published(self, request, queryset): #admin에서 목록에 해당하는 작업을 한번에 실행 처리
        updated_count = queryset.update(status='p') #choices 형이기 떄문에 가능한가????
        self.message_user(request, '{}건 published'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published상태로 변경'  # 함수의 이름으로 적용된 곳에 설명으로적용

    def make_Draft(self, request, queryset): #admin에서 목록에 해당하는 작업을 한번에 실행 처리
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건 Draft'.format(updated_count))
    make_Draft.short_description = '지정 포스팅을 Draft 상태로 변경'

    def make_withdraw(self, request, queryset): #admin에서 목록에 해당하는 작업을 한번에 실행 처리
        updated_count = queryset.update(status='w')
        self.message_user(request, '{}건 Withdraw'.format(updated_count))
    make_withdraw.short_description = '지정 포스팅을 Withdraw 상태로 변경'



########################################################################################################
ep9)Model Manager 모델을 통한 데이터 CRUD

+ 데이터베이스 질의 인터페이스를 제공
+ 디폴트 Manager로서 ModelCls.objects 가제공


ModelCls == Post (모델명)

ModelCls.objects.all() # 특정 모델의 전체 데이터 조회
ModelCls.objects.all().order_by('-id')[:10] #특정 모델의 최근 10개 데이터 조회
ModelCls.objects.create(title="New Title") # 특정 모델의 새 Row 저장


Post.objects 까지가 기본 이다.


QuerySet을 통항 And 조회 조건 추가 (Chaining, Lazy)

queryset = Modelcls.objects.all() # 데이터 전부를 가저와서
queryset = queryset.filter(조건필드1 = 조건값1, 조건필드2 = 조건값2)
queryset = queryset.filter(조건필드3 = 조건값3)
queryset = queryset.filter(조건필드4 = 조건값4, 조건필드5 = 조건값5)

@ 실제 데이터 Row에 접근할 때 데이터베이스에 쿼리 보냄(lazy)
for model_instance in queryset: #첫 레코드 패치 할 때 실행될 때  
  print(model_instance)





for post in Post.objects.all():
    print(post) --> str(post) -> post.__str__() 모델에 def __str__(self) 를 정의해주면
                                 Post.objects.all() 실행시 가저오는 리스트 형이 str 값이 구나. print
                                 시에 str 보여줌

And 조건
Post.objects.filter(title__icontains='1', title__endswith='3') #제목이 1로 시작하고 3으로 끝나는 것
Post.objects.filter(title__icontains='1').exclude(title__endswith='3') #1로 시작하고 3으로 끝나는 제외

Or 조건 만들기
from django.db.models import Q
Post.objects.filter(Q(title__icontains='1') | Q(title__endswith='3'))

@@@@@@@@@@@@@@
view.py에 쿼리셋을 정의하고 데이터를 데이터 베이스로 부터 가져오기 실습

post_list.html 에서 아래 코드 추가 후 실행 데이터 화면에 가져오기
<ul>
  {% for post in post_list %}
  <li>
    {{post.id}}
    {{post.title}}
    <small>by {{post.author}}</small>
    <small>at {{post.updated_at}}</small>
  </li>
  {% endfor%}
</ul>


@@@@@@@@@@@@
간단한 검색기능 구현

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


@@@@@@@@@@@
기본 정렬값 설정하기
models.py 에서 설정 해준다

모델 클레스 안에 Meta 클래스로 정의 해준다.
class Meta:
  ordering = ['-id'] #id로 내림 차순 정렬을 기본으로 정렬하겠다.


@@@@
슬라이싱을 통한 범위 조건 추가
queryset[:10]
queryset[10:20]
queryset[-10:] #음수 실라이싱을 지원하지 않는다.


@@@지정 조건으로 db로 부터 데이터를 Fetch

qs = Post.objects.all()  부터 실행 되고 여기서 데이터 가저오는 것입니다.

#1 지정 조건의 데이토 Row를 순회
for model_instance in queryset:       @다수 레코드
  print(model_instance)

#2 지정 조건 내에서 특정 인덱스 데이터 Row를 Fetch  (인덱스 조건)
model_instance = queryset[0] #갯수 밖의 인덱스틑 요청할 경우 IndexError 예외 발생
model_instance = queryset[1]

#3 특정 조건의 데이터 Row 1개 Fetch (1개 ! 2개이상말고 1개) (조건을 주어서 찾기)
model_instance = queryset.get(id=1)
model_instance = queryset.get(title='my title')

#4 qeuryset.first() or queryset.last() 처음과 끝의 Row를 Fetch
지정 조건에 맞는 데이토 Row가 없더라도, DoesNotExist 예외가 발생하지 않고, None을 반환



########################### CREATE ####################################
데이터 베이스에 데이터 추가 요청 방법 Create
1) 필수 필드를 모두 지정하고, 데이터 추가가 이루어져야 합니다.
   그렇지 않으면, IntegrityError 예외 발생

#방법1, 각 Model instance 의 save 함수를 통해 저장
model_instance = ModelCls(field1 = value1, field2 = value2)
print(model_instance.id) #데이저 저장 전 None값을 가진다.
model_instance.save() #데이터베이스에 저장을 시도하고, DB로 부터 id할당 받음
print(model_instance.id) #자동증가값이 지정

#방법2, 각 Model Manager
model_instance = ModelCls.objects.create(피드명1 = 값1, 필드명2 = 값2)
print(model_instance.id) #자동증가값이 지정

@SQL = insert into blog_post ('필드명1','필드명2') values ('값1','값2')

########################### UPDATE ####################################
데이터 베이스 UPDATE

#방법1, 각 Model 인스턴스 속성을 변경하고, save 함수를 통해 저장
 -> 각 Model 인스턴스 별로 SQL이 수행
 -> 다수 ROW 에 대해서 수행 시에는 성능저학 발생할 수 있음

 post = Post.objects.get(id=1)
 post.tags = "Python_Django"
 post.save()

 queryset = Post.objects.all()
 for post in qeuryset:
     post.tags = "Python, Django"
     post.save()

#방법2, qeuryset의 update 함수에 업데이트할 속성값을 지정하여 일괄 수정
하나의 SQL로서 동작하므로, 동작이 빠르다.
queryset = Post.objects.all()
queryset.update(tags="Python, Django") #일괄 update 요청

@SQL = update blog_post set tags ="python, django"


########################### DELETE ####################################
데이터 베이스 DELETE

#방법1, 각 Model 인스턴스의 delete 함수를 호출하여, 데이터베이스 혹은 관련데이터를 삭제
 -> 각 Model 인스턴스 별로 sql이 수행
 -> 다수 row 에 대해서 수행 시에는 성능 저하가 발생할 수 있음.

post = Post.objects.get(id=1)
post.delete()

queryset = Post.objects.all()
for post in qeuryset:
    post.delete()

#방법2, QuerySet의 delete 함수를 호출하여, 데이터베이스 측의 관련 데이터 삭제
-> 하나의 sql로서 동작하므로, 동장이 빠르다.

queryset = Post.object.all()
qeuryset.delete()

Delete from blog_post




########################################################################################################
ep10) Http Status code 404

HTTP Status Code
웹 서버는 적절한 상태코드로서 응답해야합니다.

대표적 http 응답 상태 코드
200 : 성공
302 : 임시 url로 이동했다. (Redirect)
404 : 서버가 요청한 페이지를 찾을 수 없음.(Not Found)
500 : 서버 오류 발생 (Server Error)

#200응답
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

def view1(request):
   return HttpResponse('안녕하세요.')

def view2(request):
   return render(request, 'tamplate.html')

def view3(reqeust):
   return JsonResponse({"hello":'world'})


#302응답
from django.http import HttpResponseRedirect
from django.shortcuts imrpot redrict, resolve_url

def view1(request):
    return HttpResponseRedirect('/blog/')

def view2(request):
    url = resolve_url('blog:post_list')  #후에 배울 url Reverse 적용
    return HttpResponseRedirect(url)

def view3(request):
    return redirect('blog:post_list')

#404응답
from django.http imrpot Http404, HttpResPonseNotFound
from django.shortcuts import get_object_or_404

def view1(request):
    raise Http404 #Exception class

def view2(request):
    post = get_object_or_404(Post, id=100) # 없는 id에 접근할 경우 Http404예외 발생

def view3(request):
    return HttpResPonseNotFound() # 잘사용하지 않는 방법


##### views.py에 아래 함수 등록하여 404 에러 처리    
    def post_detail(request, id):

        post = get_object_or_404(Post, id=id) # 아래 4줄과 동일한 1줄이다
        # try:
        #     post = Post.objects.get(id=id)
        # except Post.DoesNotExist:
        #     raise Http404


        return render(request, 'blog/post_detail.html',{
            'post':post,
        })




#500응답
from blog.models import POST

def view1(request):
    name = ['tom','steve'][100]
    #생략

def view2(request):
    post = Post.objects.get(id=100) #없는 id에 접근할 경우 Post.DoesNotExist예외가 발생
    #생략




#### 현재까지
post_list 를 통하여 데이터베이스의 값을 화변에 보여줬고
post_detail 을 통하여 post_list 에서 보여지고 있는 목록을 통하여 데이터베이스 값을 보여주는 페이지 처리및
404에러 발생시 처리 방법에 대하여 배웠다.









########################################################################################################
ep11) Model Relationship Fields

포스팅과 댓글, 포스팅과 글쓴이, 포스팅과 카케고리 등의 정보를 관계형데이터베이스에 넣기 위해서는
Relation에 대한 이해가 필요하다.

외래키 - 1:n 관계를 표현
Many to ManyFiled - m:n관게
 - 중간 테이블이 생성되며, ForeingKey 관계로 참조
One to OneField - 1:1관계

데이터베이스 정규화

_정규화 : rdbms 설계에서 중복을 최소화 하게 데이터를 구조화 하는 프로세스
_충분히 정규화 하지 않는다면, 중복 정보가 복수 개의 Row/Column에 혼재 : Record 갱신/삭제 시에
 _관련되 Row/Column에 대해서 처리 되지 않을경우, 논리적 모순 발생
 _ 경우에 따라 비정규화 과정 필요

__

ex)
#코멘트 모델 추가
1:n - 포스팅과 댓글 ( 한 개의 포스팅과 여러개의 댓글)

from jango.db import models
class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()

class Comment(models.Model):
  post = models.ForeingKey(Post) #Point!!!!
  message = models.TextField()

_실제 아래와 같이 적용 시켜두었다.
class Comment(models.Model):
    post = models.ForeignKey(Post) # post 모델에 대한 외래키로 쓰겠다.
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
__

외해키 사용은 아래와 같이 사용할 수 있다.
#post_detail.html
{%for comment in post.comment_set.all%}
<ol>
  <li>
  {{comment.message}}
    작성자 : {{comment.author}}
    <small>작성시간 : {{comment.update_at}}</small>
  </li>
</ol>
{%endfor%}


릴레이션 걸기위해서
Tag set 을만들기 위하여 Post 모델에 추가헤주고 Tag 클래스도 생성

Post.objects.filter(tag_set__name="django")
post.objects.filter(tab_set__name__in=['django','python'])




1:1 User 와 Profile
account 앱생성

프로필 모델 생성 및 등록
class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_nuber = models.CharField(max_length=20)
    address = models.CharField(max_length=50)





Foreignkey를 이용하여 만들었던 comment 모델에서 데이터를 가저오는 방법
1) Comment 모델의 구성은?? -> blog.models.Comment 로 만들어 졌네
2) comment = Comment.objects.first()  -> Comment: Coment object
3) comment.post 로 가져올 수 있다.

모델 사용 추천 방식을 사용하기 위해서 account -> models.py 에서 수정

//
_ForeignKey.on_delete 옵션
# #1측의 Row가 삭제될 경우, N측의 Row의 처리에 대한 동작을 지정 # #
Cascade: 연뎔된 Row를 일괄 삭제 (디폴트 동작)
Protect : ProtectError 예외를 발생시키며, 삭제 방지
SET_NULL : null = True 설정이 되어있을 때, 삭제되면 해당 필드를 null설정
SET_DEFAULT : 필드에 지정된 디폴트 값을 설정__


그러니까)
1) post 포린키로 만들었으니까 댓글을 달기위해서는 해당 post를 들고 와야한다.
-> post = Post.objects.get(id=3) #3번 포스팅을 가져오고
2) comment = post.comment_set.all() # 포린키로 연결된 값을 다 들고 온다.
2-1 ) Comment.objects.create(post=post, author="geonil", message="댓글") #위에서 들고온 3번 포스팅에 값을    추가 하겠다.
3)

########################################################################################################
ep12) 장고 템플릿 상속

여러 템플릿 파일 별로 필연적으로 발생하는중복을 상속을 통해 중복 제거 상속은 여러번 이루어 질 수 있다.

부모 템플릇은 전체 레이아웃을 정의하며, 자식 템플릿은 재정의할 block을 다수 정의해야 한다.

자식 템플릿은 부모 템플릿을 상속받은 후에 부모 템플릿의 _block__
역역에 대해서 재정의만 가능 하며 그외 코드는 무시

_템플릿 상속 문법 : 항시 자식템플릿 코드 내, 최상단에 쓰여져야 합니다.__
{% extends "부모템플릿 경로 "%}


2단계 상속을 추천한다
전반적인 프로젝트 앱의 것을 상속받는 것을 추천한다

프로젝트 밑에 templates 폴더를 만들어서 거기서 레이아웃을 관리 하는 것을 추천한다

########################################################################################################
ep13) Djanog Template Loader

다수 디렉토리 목록에서 지정 상태결로를 가지는 템플릿을 찾음

+ app_directories.Loder 와 filesystem.Loader 위 Loade를 통해, 템플릿 디렉토리가
있을 후보 디렉토리 리스트를 작성 합니다. 이는 장고 서버 초기 시작 시에만 1회 작성됩니다.


주로 아래 함수를 통해 Template파일들을 활용합니다.
reder 템플릿을 렌더링은 문자열로 HttpResponse 객체를 리턴
reder to string 템플릿 렌더링한 문자열을 리턴

response = render(request, "blog/post_list.html", context_params)  -   HttpResponse
welcome_message = render_to_string('accounts/signup_welcome.txt', context_params) string

# app_directories.Loader
-> settings.INSTALLED_APPS에 설정된 앱 디렉토일 내 templates 경로 에서 템플릿 파일을 찾습니다.

앱 디렉토리 별로 각 앱을 위한 템플리 파일을 위치
- blog앱용 템플릿은 blog/templates/ 경로에 두는 것이 관리성이 좋다.


#filesystem.Loader 프로젝트 레벨에 템플릿을 사용하기 위해 아래처럼 'settings.py 에 등로'
'DIRS': [
        os.path.join(BASE_DIR,"Django_Geonil_Web","templates"),
    ],




from django.template.loader import render_to_string
render_to_string('accounts/signup_welcome.txt')
message=render_to_string('accounts/signup_welcome.txt',{"name":"geonil","when":"2018-07-02"})



########################################################################################################
ep14)URL Reverse
urls.py변경만으로 "각 뷰에대한 url"이 변경되는 유연한 url시스템

+ 개발자가 일일이 url을 계산하지 않아도 됩니다.
  url이 변경되더라도, url reverse가 변경된 url을 추척 누락될 일이 없다.


url -> 뷰 함수
~ URLReverse 개년 url이 변경되도 뷰 함수는 변경되지 않도록 하기위해서

URL이 변경될 때마다 , 이 url 을 참조하고 있는 코드를 일일이 찾아서 변경하느 것은 너무 번거롭고, 수정건을 누락시킬 여지도 많다.!!! 그래서

urls.py -> urlpatterns 에  name을 만들어 준다.

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^detail/(?P<id>\d+)/$', views.post_detail, name="post_detail"),
]


<a href="{% url "post_detail" post.id %}">{{post.title}}</a>
<!-- <a href="/blog/detail/{{post.id}}">{{post.title}}</a> -->

위에 처럼 사용하는 것은 project urls 에 namespace를 안쓸경우 사용이 가능 한 방법이고
urlspace를 사용하게 되요 앞에 앱이름 blog: 를 붙여 줘야한다

<a href="{% url "blog:post_list" %}">글 목록</a>
    <a href="{% url "blog:post_detail" post.id %}">{{post.title}}</a>


_최초 진입 url 설정하기__
프로젝트 urls 에서해줌


namsepace 를 사용하는 이유는 중복을 피하기 위해서 사용하는 것이다
중복이 없다면 name 만으로 사용해도 문제가 없을 것을 보입니다.  


모델.py
아래 코드를 추가 해줌으로 조금더 쉽게 데이터를 가져올 수 있다.
def get_absolute_url(self):
      return reverse('blog:post_detail',args=[self.id])

위의 함수를 구현을 해두 었다면

createView/ UpdateView에 success_url을 제공하지 않을 경우,
해당 모델인스턴스의 get_absolute_url주소로 이동이 가능한지 체크하고, 이동이 가능할 경우 이동.
* 글 작성후 작성을 확인 페이지로 자동으로 페이지 전환이 이루어짐 (이동페이지 정하지 않았을 경우)


blog에 view_cbv 만들어서 실습



########################################################################################################
ep15)부트 스트렙3
12칸 grid system
다양한 써드 파티

########################################################################################################
ep16) 장고 템플릿 엔진 TAG
Fat Model
stupid Template
Thin View

_장고 템플릿 엔진에서의 for 문

{% for row in rows %}
  <tr>
    {% for name in row %}
    <td>{{name}}</td>
    {% endfor %}
  </tr>
{% endfor %}

__

people = {"tom"L10, "steve":10}
call Person(object):
  def say_hello():
    print("hello world")

person = Person()

#python
people['tom']
person.say_hello()

#template engine 모든 어트리 뷰트를 .으로 접근한다.
{{people.tom}} -> 이렇게 사용하는 것을 지원한다.
{{person.say_hello}}


########################################################################################################
ep17) 장고 템플릿 엔진 filter

+ 템플린 변수값 변환을 위한 함수 이며, 다수 필터 함수를 연결가능
 {{var|filter1}},{{var|filter2:인자}},{{var|filter3:인자|filter4}}

+ 빌트인 filter가 지원되며, 장고앱 별로 커스텀 Filter추가 가능
|앞에가 1번째 인자 : 뒤에가 2번째 인자 -> | 를 기준으로  

len(value) = {{value | length}}
             {{ value | linebreaks}}  -> <p>
           = {{ value | random}} -> value = [1,2,3,4,5]
             {{ safe fileter }}
             {{ html | safe }} -> 자바스크립트 같은 동작을 안전하게
             {{ some_list | slice ":2"}}
             {{ value1 | truncatechars : 9}} 아홉글자 뒤에 ....
             {{ value | urlencode }} get / post



########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
ep18) html form

HTML- 웹 페이지에서는 FORM태그를 통해, 데이터를 전송

EX) 로그인 폼, 댓글 폼

하나의 FORM태그는 하나 이상의 위젯(Widget)을 가진다. 하나의 ui 구성요서
<form action="" method="post">
  <input type="text">
  <textarea></textarea>
  <select></select>
  <input type="checkbox">
  <input type="raido">
  그 외 다수 위젯
</form>



Action
Method get : 주로 데이터 조회시 요청  header 만
       post: 파괴적인 핵션(생성/수정/삭제)에 대한 요청 시 header + body

enctype : request.POST
 -> application/x-www-form-urlencode(디폴트)
 -> multipart/form-data : 파일 업로드 가능
 -> text/plain: 스펙에는정의 되어있으나 실제로는 사용하지 않음.

url encoded란?
key=value 값의 쌍이 &문자로 이어진 형태

from urllib.parse import urlencode
urlencode({'key1':'value1'})


_form method
Get 방식 : 엽서에 비유. 물건을 보낼 수 없다.

Post 방식 : 택배에 비유. 다양한 물건을 보낼 수 있다.
    -> get/post 인자가능
    -> 지정된 enctype으로 인코딩하여, body에 포함 시켜 처리

    head GET POST

    body POST__



########################################################################################################
########################################################################################################
ep19) CSRF   Cross-site requests forgery
사이트 간 요청 위조 공-> 사용자가 의도하지 않게 게시판에글을 작성하거나, 쇼핑을 하게 하는등의 공격

공격을 맞기 위하여 csrf token 발급을 한다.
{% csrf_token %} -> input hidden name="csrf_token~~" value="0asjd0as9dj234c09-8m345c834c84c3"

get으로 접근해서 post로 등록을 한다.
get단계에서 토큰을발급! 저장할때 post로 보낸다. -> 유효하면/ 그제서야 뷰를 호출 해준다. 안맞으면 403 포비든을 응답한다.

API뷰와 같은
특정 뷰에한해 csrf token 을 해제하기위해서는 csrf_exempt 를해준다.

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def my_view(request):
  return HttpResponse('Hello world')

########################################################################################################
########################################################################################################
ep20) httprequest httpresponse 에대해서

HttpRequest
+ 클라이언로부터의 몬든 요청 내용을 담고 있으며, 매 요청 시마다 뷰함수의 첫번째인자로 전달.

HttpRequest objects에서 폼 처리 관련속성들
  -> request.Method : get or post
  -> request.GET : get 인자, queryDict 타입 get/post
  -> request.POST : post 인자 , queryDict 타입 post 요청시
  -> request.Fields : post 업로드 파일 인자 MultiValueDict 타입

  fbc : request
  cbv : self.request

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
ep21) 장고폼 Form

+ 장고를 더욱 장고스럽게 만들어주는 주옥같은 틀
+ Model클래스와 유사하게 form클래스를 정의
+ 주요 역할 : 커스텀 form클래스를 통해..
   -> 입력폼 HTML 생성 : .as_table(), as_p(), as_ul()기본 제공
   -> 입력폼 값 검증(validation) 및 값 변환
   -> 검증을 통과한 값들을 사전타입으로 제공
                          => cleaned_data 로제공받는다.

front - form  <=> model - db


_a
ex) post_new(request):
      if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(**self.cleaned_data)
            post.save()
            return redirect(post)
      else:
        form = PostForm()

      return render(request, 'blog/post_form.html', {
            'form': form
        })
//**
__



1) 폼클래스 정의 dojo에서 실습을 진행
  1. 모델을 일단 만든다.
  2. forms.py를 만든다.
  3. 유효성 검사추가
  4. 뷰함수에서 폼 인스턴스 생성



########################################################################################################
########################################################################################################
ep22) 장고모델폼

모델폼은 폼 클래스를 상속받은 클래스이다.
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'  #전체 필드 지정. 혹은 list 로 읽어올 필드면 지정
"""

########################################################################################################
########################################################################################################
ep23) 폼유효성 검사
form.is_valid(): 유효성 검사 시작한다











































end
