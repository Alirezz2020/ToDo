
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'accounts.views.custom_404'
handler500 = 'accounts.views.custom_500'
handler403 = 'accounts.views.custom_403'
handler400 = 'accounts.views.custom_400'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('', include('home.urls', namespace='home')),  # Other apps' URLs
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
