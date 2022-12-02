from django.contrib import admin
from django.urls import path, include
from poster import views, place_detail_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('places/<int:place_id>/', place_detail_view.get_place, name='places'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
