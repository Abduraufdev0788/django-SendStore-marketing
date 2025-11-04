from django.contrib import admin
from django.urls import path, include
from sendstore.views import home_page, photos_page, videos_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('photos/', photos_page, name='photos_page'),
    path('videos/', videos_page, name='video_page'),

]
