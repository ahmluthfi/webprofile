from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
       return self.username

class Organisasi(models.Model):
    organisasi_nama = models.CharField(max_length=50)
    organisasi_email = models.CharField(max_length=50)
    organisasi_telepon = models.CharField(max_length=50)
    organisasi_profile = models.TextField()

    def __unicode__(self):
       return self.organisasi_nama

class Gallery(models.Model):
    gallery_foto = models.FileField(upload_to='documents/')
    gallery_caption = models.TextField()

    def __unicode__(self):
       return self.gallery_foto

class Kegiatan(models.Model):
    kegiatan_nama = models.CharField(max_length=100)
    kegiatan_deskripsi = models.TextField()

    def __unicode__(self):
       return self.kegiatan_nama


class Berita(models.Model):
    berita_judul = models.CharField(max_length=100)
    berita_isi = models.TextField()
    berita_foto = models.CharField(max_length=100)

    def __unicode__(self):
       return self.berita_judul

class Rekening(models.Model):
    rekening_nomor = models.CharField(max_length=100)
    rekening_nama = models.CharField(max_length=100)
    rekening_bank = models.TextField()
    rekening_gambar = models.FileField(upload_to='documents/')

    def __unicode__(self):
       return self