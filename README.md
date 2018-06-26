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
