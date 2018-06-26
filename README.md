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
