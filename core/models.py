# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Bidang(models.Model):
    nama_bidang = models.CharField(max_length=100)
    deskripsi_bidang = models.TextField()

    def __str__(self):
        return self.nama_bidang

class Anggota(models.Model):
    nama_lengkap = models.CharField(max_length=150)
    nim = models.CharField(max_length=20, unique=True)
    jabatan = models.CharField(max_length=50)
    foto_profil = models.ImageField(upload_to='anggota/')
    email = models.EmailField(blank=True, null=True)
    angkatan = models.IntegerField()
    bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE, related_name='anggota')

    def __str__(self):
        return f"{self.nama_lengkap} ({self.nim})"

class Pengumuman(models.Model):
    TIPE_CHOICES = [('Pemberitahuan', 'Pemberitahuan'), ('Pengumuman', 'Pengumuman')]
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    penulis = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)
    tipe = models.CharField(max_length=20, choices=TIPE_CHOICES, default='Pemberitahuan')

    def __str__(self):
        return self.judul

class Event(models.Model):
    STATUS_CHOICES = [('Akan Datang', 'Akan Datang'), ('Selesai', 'Selesai')]
    nama_event = models.CharField(max_length=200)
    deskripsi_event = models.TextField()
    tanggal_mulai = models.DateTimeField()
    lokasi = models.CharField(max_length=200)
    poster_event = models.ImageField(upload_to='event_posters/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Akan Datang')

    def __str__(self):
        return self.nama_event

class Dokumentasi(models.Model):
    event_terkait = models.OneToOneField(Event, on_delete=models.CASCADE)
    judul_dokumentasi = models.CharField(max_length=200)
    deskripsi_singkat = models.TextField()
    link_gdrive = models.URLField()
    foto_unggulan = models.ImageField(upload_to='dokumentasi/')

    def __str__(self):
        return f"Dokumentasi untuk {self.event_terkait.nama_event}"