from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('chatroom.urls')),
    path('', include('blog.urls')),
    path('', include('business.urls')),
    path('', include('mentor.urls')),
    path('', include('program.urls')),
    path('', include('fund.urls')),
    path('', include('application.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
