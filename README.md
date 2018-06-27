"# MyDjango"

ep1)
1) 프로젝트 생성
django-admin startproject 프로젝트명
2)장고프로젝트 생성 및 개발서버 구동
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

===================================================================================================
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

===================================================================================================
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

===================================================================================================
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


===================================================================================================
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



===================================================================================================
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

===================================================================================================
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


===================================================================================================
ep8)






















































































end
