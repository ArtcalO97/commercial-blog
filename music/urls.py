from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.musicList_view, name="music"),
    path('download/<slug>/', views.musicDownload_view, name="download"),
]