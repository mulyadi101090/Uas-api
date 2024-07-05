from django.urls import path
from .views import JadwalSekolahList, GuruList, MataPelajaranList, RuanganList

urlpatterns = [
    path('jadwal/', JadwalSekolahList.as_view(), name='jadwal-list'),
    path('guru/', GuruList.as_view(), name='guru-list'),
    path('matapelajaran/', MataPelajaranList.as_view(), name='matapelajaran-list'),
    path('ruangan/', RuanganList.as_view(), name='ruangan-list'),
]