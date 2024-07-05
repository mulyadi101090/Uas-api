from rest_framework import serializers
from .models import JadwalSekolah, Guru, MataPelajaran, Ruangan

class GuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guru
        fields = '__all__'

class MataPelajaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataPelajaran
        fields = '__all__'

class RuanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruangan
        fields = '__all__'

class JadwalSekolahSerializer(serializers.ModelSerializer):
    guru = GuruSerializer()
    mata_pelajaran = MataPelajaranSerializer()
    ruangan = RuanganSerializer()

    class Meta:
        model = JadwalSekolah
        fields = '__all__'

    def create(self, validated_data):
        guru_data = validated_data.pop('guru')
        mata_pelajaran_data = validated_data.pop('mata_pelajaran')
        ruangan_data = validated_data.pop('ruangan')
        
        # Buat instance Guru
        guru = Guru.objects.create(**guru_data)
        # Buat instance MataPelajaran
        mata_pelajaran = MataPelajaran.objects.create(**mata_pelajaran_data)
        # Buat instance Ruangan
        ruangan = Ruangan.objects.create(**ruangan_data)
        
        jadwal_sekolah = JadwalSekolah.objects.create(
            guru=guru, 
            mata_pelajaran=mata_pelajaran, 
            ruangan=ruangan, 
            **validated_data
        )
        return jadwal_sekolah
