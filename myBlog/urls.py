from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'iStudent Admin'
admin.site.site_title = 'iStudent Admin Panel'
admin.site.index_title = 'Welcome to iStudent Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blog/',include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
