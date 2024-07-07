
from django.db import models

class Guru(models.Model):
    id_guru = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alamat = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.id_guru} - {self.nama}'

class MataPelajaran(models.Model):
    id_mata_pelajaran = models.AutoField(primary_key=True)
    mata_pelajaran = models.CharField(max_length=100)
    
    hari = models.CharField(max_length=20)
    waktu_mulai = models.TimeField()
    waktu_selesai = models.TimeField()
    materi = models.TextField()

    def __str__(self):
        return f'{self.id_mata_pelajaran} - {self.mata_pelajaran}'

class Ruangan(models.Model):
    id_ruangan = models.AutoField(primary_key=True)
    
    nama_ruangan = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id_ruangan} - {self.nama_ruangan}'

class JadwalSekolah(models.Model):
    guru = models.ForeignKey(Guru, on_delete=models.CASCADE)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    ruangan = models.ForeignKey(Ruangan, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guru.nama} - {self.mata_pelajaran.mata_pelajaran} - {self.ruangan.nama_ruangan}'
