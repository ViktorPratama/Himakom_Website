# core/admin.py
from django.contrib import admin
from .models import Bidang, Anggota, Pengumuman, Event, Dokumentasi

# Daftarkan setiap model di sini
admin.site.register(Bidang)
admin.site.register(Anggota)
admin.site.register(Pengumuman)
admin.site.register(Event)
admin.site.register(Dokumentasi)