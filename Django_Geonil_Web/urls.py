from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')), #blog.urls  / -> .으로
    url(r'^dojo/', include('dojo.urls')), #blog.urls  / -> .으로
]
