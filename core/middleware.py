# core/middleware.py

from django.core.exceptions import PermissionDenied

class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Daftar IP yang diizinkan untuk mengakses halaman admin.
        # Anda bisa menambahkan IP publik Anda juga.
        # Untuk mengetahui IP publik Anda, cari "what is my ip" di Google.
        self.allowed_ips = ['127.0.0.1', '192.168.1.9', 'IP_PUBLIK_ANDA'] 

    def __call__(self, request):
        # Memeriksa apakah path URL dimulai dengan /admin/
        if request.path.startswith('/admin/'):
            # Mendapatkan alamat IP dari pengunjung
            ip = request.META.get('REMOTE_ADDR')
            
            # Jika IP pengunjung tidak ada di dalam daftar, tolak akses
            if ip not in self.allowed_ips:
                raise PermissionDenied  # Ini akan menghasilkan error 403 Forbidden

        response = self.get_response(request)
        return response