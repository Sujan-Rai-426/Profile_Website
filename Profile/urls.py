

from django.conf import settings


from django.views.static import serve

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    
    re_path(r"^media/(?P<path>.*)$", serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {'document_root': settings.STATIC_ROOT}),
    
    path('admin/', admin.site.urls),
    path('', include("Home.urls")),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
    
