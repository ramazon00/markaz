from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('account/', include('login.urls', namespace='login')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
# O'chirdim
#    path('accounts/', include('accounts.urls')),
#   path('accounts/', include('django.contrib.auth.urls')),
#    path('', include('pages.urls')),    
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
