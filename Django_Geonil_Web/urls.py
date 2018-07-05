from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static

def root(request):
    return redirect('blog:post_list')

urlpatterns = [
    # url(r'^$', root, name="root"),
    url(r'^$', lambda r: redirect('blog:post_list'), name="root"),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')), #blog.urls  / -> .으로
    url(r'^dojo/', include('dojo.urls', namespace='dojo')), #blog.urls  / -> .으로
    url(r'^accounts/', include('account.urls')), #blog.urls  / -> .으로
    url(r'^product/', include('product.urls', namespace='product')), #blog.urls  / -> .으로
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=[
        url(r'^__debug__/',include(debug_toolbar.urls))
    ]
