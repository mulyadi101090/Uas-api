from rest_framework import generics
from .models import JadwalSekolah, Guru, MataPelajaran, Ruangan
from .serializers import JadwalSekolahSerializer, GuruSerializer, MataPelajaranSerializer, RuanganSerializer
from django.shortcuts import render

class JadwalSekolahList(generics.ListCreateAPIView):
    queryset = JadwalSekolah.objects.all()
    serializer_class = JadwalSekolahSerializer

class GuruList(generics.ListCreateAPIView):
    queryset = Guru.objects.all()
    serializer_class = GuruSerializer

class MataPelajaranList(generics.ListCreateAPIView):
    queryset = MataPelajaran.objects.all()
    serializer_class = MataPelajaranSerializer

class RuanganList(generics.ListCreateAPIView):
    queryset = Ruangan.objects.all()
    serializer_class = RuanganSerializer


def home(request):
    return render(request, 'home.html')