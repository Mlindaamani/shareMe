from django.contrib import admin
from django.urls import path, include
from airdrop import settings
from django.conf.urls.static import static

admin.site.site_header = 'SHAREME'
admin.site.index_title = 'Admin'
admin.site.site_title = 'Book Share'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bot.urls', namespace='bot')),
    path('user/', include('users.urls', namespace='users')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
