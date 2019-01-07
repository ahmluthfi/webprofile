from django.forms import ModelForm
from .models import User, Organisasi, Gallery, Kegiatan, Berita, Rekening

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class OrganisasiForm(ModelForm):
    class Meta:
        model = Organisasi
        fields = ['organisasi_nama','organisasi_email','organisasi_telepon']

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['gallery_caption','gallery_foto']

class KegiatanForm(ModelForm):
    class Meta:
        model = Kegiatan
        fields = ['kegiatan_nama','kegiatan_deskripsi']

class BeritaForm(ModelForm):
    class Meta:
        model = Berita
        fields = ['berita_judul','berita_isi']

class RekeningForm(ModelForm):
    class Meta:
        model = Rekening
        fields = ['rekening_bank','rekening_nama','rekening_nomor','rekening_gambar']