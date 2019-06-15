from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    url('^$', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIAL_URL, document_root=settings.MEDIA_ROOT)