from django.conf.urls import url
from . import views
from . import views_cbv
urlpatterns = [

    url(r'^(?P<pk>\d+)$', views.post_detail),




    url(r'^new/$', views.post_new),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit),

    url(r'^sum/(?P<x>[\d/]+)/$', views.mysum), #함수의 인자로 넘겨줄 인자를 적는다 <>안에
    #<id>: id라는 변수명으로 인자를 넘기겠다. -> 뷰에서 사용할 함수의 인자값을 적어주는 것이다
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{1,3})/(?P<age>\d+)/$', views.info),
    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^list4/$', views.post_list4),


    url(r'^cbv/list1/$', views_cbv.post_list1),
    # url(r'^cbv/list2/$', views_cbv.post_list2),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    # url(r'^cbv/list3/$', views_cbv.post_list3),
    # url(r'^cbv/list4/$', views_cbv.post_list4),
]
