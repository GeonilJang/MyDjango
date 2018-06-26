from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sum/(?P<x>[\d/]+)/$', views.mysum), #함수의 인자로 넘겨줄 인자를 적는다 <>안에
    #<id>: id라는 변수명으로 인자를 넘기겠다. -> 뷰에서 사용할 함수의 인자값을 적어주는 것이다
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{1,3})/(?P<age>\d+)/$', views.info)
]
