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
