from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name="product_list"),
    url(r'^(?P<id>\d+)/$', views.product_detail, name="product_detail"),
    url(r'^new/$', views.product_new, name="product_new"),
    url(r'^(?P<id>\d+)/edit/$', views.product_edit, name="product_edit"),

]
