from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('predict/<int:pk>/', views.predict_genre, name='predict_genre'),  
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

