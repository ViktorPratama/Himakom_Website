# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL untuk Homepage
    path('', views.home, name='home'),
    # URL untuk Pengumuman
    path('pengumuman/', views.pengumuman_list, name='pengumuman_list'),
    path('pengumuman/<int:pk>/', views.pengumuman_detail, name='pengumuman_detail'),
    # URL untuk Event
    path('event/', views.event_list, name='event_list'),
    # URL untuk Dokumentasi
    path('dokumentasi/', views.dokumentasi_list, name='dokumentasi_list'),
    # URL untuk Anggota
    path('anggota/', views.anggota_list, name='anggota_list'),
    path('anggota/<int:pk>/', views.anggota_detail, name='anggota_detail'),
]