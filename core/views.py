from django.shortcuts import render, get_object_or_404
from .models import Bidang
from .models import Anggota # Pastikan Anggota sudah di-import
from .models import Pengumuman, Event 
from .models import Dokumentasi # tambahkan model Dokumentasi

# Anggota
def anggota_list(request):
    # Mengambil semua bidang, dan 'prefetch_related' mengambil semua anggota
    # yang terkait dengan bidang-bidang tersebut secara efisien untuk menghindari
    # query berulang di dalam template.
    semua_bidang = Bidang.objects.prefetch_related('anggota').all()
    
    context = {
        'semua_bidang': semua_bidang
    }
    return render(request, 'core/anggota_list.html', context)

#Detail Anggota
def anggota_detail(request, pk):
    # Mengambil satu objek anggota berdasarkan Primary Key (pk).
    # Jika tidak ditemukan, akan menampilkan halaman 404 Not Found.
    anggota = get_object_or_404(Anggota, pk=pk)
    
    context = {
        'anggota': anggota
    }
    return render(request, 'core/anggota_detail.html', context)

# Homepage
def home(request):
    # Ambil 3 pengumuman terbaru
    pengumuman_terbaru = Pengumuman.objects.order_by('-tanggal_publikasi')[:3]
    
    # Ambil 3 event yang akan datang
    event_mendatang = Event.objects.filter(status='Akan Datang').order_by('tanggal_mulai')[:3]
    
    context = {
        'daftar_pengumuman': pengumuman_terbaru,
        'daftar_event': event_mendatang,
    }
    return render(request, 'core/home.html', context)

# Pengumuman
def pengumuman_list(request):
    semua_pengumuman = Pengumuman.objects.order_by('-tanggal_publikasi')
    context = {
        'semua_pengumuman': semua_pengumuman
    }
    return render(request, 'core/pengumuman_list.html', context)

# Pengumuman Detail
def pengumuman_detail(request, pk):
    pengumuman = get_object_or_404(Pengumuman, pk=pk)
    context = {
        'pengumuman': pengumuman
    }
    return render(request, 'core/pengumuman_detail.html', context)

# Event
def event_list(request):
    event_mendatang = Event.objects.filter(status='Akan Datang').order_by('tanggal_mulai')
    event_selesai = Event.objects.filter(status='Selesai').order_by('-tanggal_mulai')
    context = {
        'event_mendatang': event_mendatang,
        'event_selesai': event_selesai,
    }
    return render(request, 'core/event_list.html', context)

# Dokumentasi
def dokumentasi_list(request):
    # .select_related('event_terkait') untuk optimasi query database
    semua_dokumentasi = Dokumentasi.objects.select_related('event_terkait').order_by('-event_terkait__tanggal_mulai')
    context = {
        'semua_dokumentasi': semua_dokumentasi
    }
    return render(request, 'core/dokumentasi_list.html', context)