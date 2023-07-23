from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import MusicSearch

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerpage, name="register"),
    path('login/', views.loginpage, name="login"),
    path('upload/', views.upload_song, name='upload_song'),
    path('search/', MusicSearch.as_view(), name='search_song'),
    path('download/<int:song_id>/', views.download_song, name='download_song'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
