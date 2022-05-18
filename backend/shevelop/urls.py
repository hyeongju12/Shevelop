from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_pydenticon.views import image as pydenticon_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('shareinfo/', include('shareinfo.urls')),
    path('codecast/', include('codecast.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('identicon/image/<path:data>.png', pydenticon_image, name='pydenticon_image'),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


