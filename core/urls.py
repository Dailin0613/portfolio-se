from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('home.urls')),
                  path('project/', include('project.urls')),
                  path('blog/', include('blog.urls')),
                  path('authentication/', include('authentication.urls')),
                  path('admin-site/', admin.site.urls, name='admin'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
