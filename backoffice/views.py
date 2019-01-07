from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .forms import UserForm, OrganisasiForm, GalleryForm, KegiatanForm, BeritaForm, RekeningForm
from .models import User, Organisasi, Gallery, Kegiatan, Berita, Rekening

import json
from froala_editor.fields import FroalaField
#from froala_editor import Image
#from froala_editor import DjangoAdapter

def index_user(request):
    page = 'user_list.html'
    limit = 10
    user_list = User.objects.all()
    halaman = request.GET.get('page')

    paginator = Paginator(user_list, limit)
    users = paginator.get_page(halaman)
    
    if halaman is None or halaman=='1': hal = 1
    else: hal = (int(halaman)*limit)+1

    no = hal 
    for user in users:
        user.no = no
        no+=1

    return render(request, page, {'users': users })

def form_user(request):
    page = 'user_form.html'   
    if request.method == 'POST':
        data = request.POST
        user = UserForm(data)
        if user.is_valid():
            user.save()
        return HttpResponseRedirect('/bo/user')
    else:
        return render(request, page, {})

def edit_user(request, pk):
    page = 'user_form.html'
    users = get_object_or_404(User, pk=pk)	
    
    if request.method == 'POST':
    	data = UserForm(request.POST, instance=users)
    	if data.is_valid():
        	data.save()
        	return render(request, page, {'user': users})
    	else:
        	return render(request, page, {'user': users})
    else:
        return render(request, page, {'user': users})

def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return HttpResponseRedirect('/bo/user')

############ ORGANISASI ############

def index_organisasi(request):
    page = 'organisasi_list.html'
    limit = 10
    organisasi_list = Organisasi.objects.all()
    halaman = request.GET.get('page')

    paginator = Paginator(organisasi_list, limit)
    organisasis = paginator.get_page(halaman)
    
    if halaman is None or halaman=='1': hal = 1
    else: hal = (int(halaman)*limit)+1

    no = hal 
    for organisasi in organisasis:
        organisasi.no = no
        no+=1

    return render(request, page, {'organisasis': organisasis })

def form_organisasi(request):
    page = 'organisasi_form.html'   
    if request.method == 'POST':
        data = request.POST
        organisasi = OrganisasiForm(data)
        if organisasi.is_valid():
            organisasi.save()
            return HttpResponseRedirect('/bo/organisasi')
        else:
            return HttpResponseRedirect('/bo/form_organisasi')
    else:
        return render(request, page, {})

def edit_organisasi(request, pk):
    page = 'organisasi_form.html'
    organisasis = get_object_or_404(Organisasi, pk=pk)  
    
    if request.method == 'POST':
        data = OrganisasiForm(request.POST, instance=organisasis)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect('/bo/gallery')
        else:
            return render(request, page, {'organisasi': organisasis})
    else:
        return render(request, page, {'organisasi': organisasis})

def delete_organisasi(request, pk):
    organisasi = Organisasi.objects.get(pk=pk)
    organisasi.delete()
    return HttpResponseRedirect('/bo/organisasi')

    
############ GALLERY ############

def index_gallery(request):
    page = 'gallery_list.html'
    limit = 10
    gallery_list = Gallery.objects.order_by('-id')
    halaman = request.GET.get('page')

    paginator = Paginator(gallery_list, limit)
    gallerys = paginator.get_page(halaman)
    
    if halaman is None or halaman=='1': hal = 1
    else: hal = ((int(halaman)-1)*limit)+1

    no = hal 
    for gallery in gallerys:
        gallery.no = no
        no+=1

    return render(request, page, {'gallerys': gallerys })

def form_gallery(request):
    page = 'gallery_form.html'
    
    if request.method == 'POST' and request.FILES['gallery_foto']:
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bo/gallery')
        else:
            return HttpResponseRedirect('/bo/form_gallery')
    else:
        return render(request, page, {})

def edit_gallery(request, pk):
    page = 'gallery_form.html'
    gallerys = get_object_or_404(Gallery, pk=pk)  
    # return HttpResponse(gallerys)
    if request.method == 'POST':
        data = GalleryForm(request.POST, request.FILES, instance=gallerys)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect('/bo/gallery')
        else:
            return render(request, page, {'gallery': gallerys})
    else:
        return render(request, page, {'gallery': gallerys})

def delete_gallery(request, pk):
    gallery = Gallery.objects.get(pk=pk)
    gallery.delete()
    return HttpResponseRedirect('/bo/gallery')


############ KEGIATAN ############

def index_kegiatan(request):
    page = 'kegiatan_list.html'
    limit = 10
    kegiatan_list = Kegiatan.objects.all()
    halaman = request.GET.get('page')

    paginator = Paginator(kegiatan_list, limit)
    kegiatans = paginator.get_page(halaman)
    
    if halaman is None or halaman=='1': hal = 1
    else: hal = (int(halaman)*limit)+1

    no = hal 
    for kegiatan in kegiatans:
        kegiatan.no = no
        no+=1

    return render(request, page, {'kegiatans': kegiatans })

def form_kegiatan(request):
    page = 'kegiatan_form.html'   
    if request.method == 'POST':
        data = request.POST
        kegiatan = KegiatanForm(data)
        if kegiatan.is_valid():
            kegiatan.save()
            return HttpResponseRedirect('/bo/kegiatan')
        else:
            return HttpResponseRedirect('/bo/form_kegiatan')
    else:
        return render(request, page, {})

def edit_kegiatan(request, pk):
    page = 'kegiatan_form.html'
    kegiatans = get_object_or_404(Kegiatan, pk=pk)  
    
    if request.method == 'POST':
        data = KegiatanForm(request.POST, instance=kegiatans)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect('/bo/kegiatan')
        else:
            return render(request, page, {'kegiatan': kegiatans})
    else:
        return render(request, page, {'kegiatan': kegiatans})

def delete_kegiatan(request, pk):
    kegiatan = Kegiatan.objects.get(pk=pk)
    kegiatan.delete()
    return HttpResponseRedirect('/bo/kegiatan')


############ BERITA ############

def index_berita(request):
    page = 'berita_list.html'
    limit = 10
    berita_list = Berita.objects.all()
    halaman = request.GET.get('page')

    paginator = Paginator(berita_list, limit)
    beritas = paginator.get_page(halaman)
    
    if halaman is None or halaman=='1': hal = 1
    else: hal = (int(halaman)*limit)+1

    no = hal 
    for berita in beritas:
        berita.no = no
        no+=1

    return render(request, page, {'beritas': beritas })

def form_berita(request):
    page = 'berita_form.html'   
    if request.method == 'POST':
        data = request.POST
        # return HttpResponse(request.POST['berita_isi'])
        berita = BeritaForm(data)
        if berita.is_valid():
            berita.save()
            return HttpResponseRedirect('/bo/berita')
        else:
            return HttpResponseRedirect('/bo/form_berita')
    else:
        return render(request, page, {})

def edit_berita(request, pk):
    page = 'berita_form.html'
    beritas = get_object_or_404(Berita, pk=pk)  
    
    if request.method == 'POST':
        data = BeritaForm(request.POST, instance=beritas)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect('/bo/berita')
        else:
            return render(request, page, {'berita': beritas})
    else:
        return render(request, page, {'berita': beritas})

def delete_berita(request, pk):
    berita = Berita.objects.get(pk=pk)
    berita.delete()
    return HttpResponseRedirect('/bo/berita')


############ REKENING ############

def index_rekening(request):
    page = 'rekening_list.html'
    limit = 10
    rekening_list = Rekening.objects.order_by('-id')
    halaman = request.GET.get('page')

    paginator = Paginator(rekening_list, limit)
    rekenings = paginator.get_page(halaman)
    
    if halaman is None or halaman=='1': hal = 1
    else: hal = (int(halaman)*limit)+1

    no = hal 
    for rekening in rekenings:
        rekening.no = no
        no+=1

    return render(request, page, {'rekenings': rekenings })

def form_rekening(request):
    page = 'rekening_form.html'
    
    if request.method == 'POST' and request.FILES['rekening_gambar']:
        form = RekeningForm(request.POST, request.FILES)
        # return HttpResponse(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bo/rekening')
        else:
            return HttpResponseRedirect('/bo/form_rekening')
    else:
        return render(request, page, {})

def edit_rekening(request, pk):
    page = 'rekening_form.html'
    rekenings = get_object_or_404(Rekening, pk=pk)  
    # return HttpResponse(rekenings)
    if request.method == 'POST':
        data = RekeningForm(request.POST, request.FILES, instance=rekenings)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect('/bo/rekening')
        else:
            return render(request, page, {'rekening': rekenings})
    else:
        return render(request, page, {'rekening': rekenings})

def delete_rekening(request, pk):
    rekening = Rekening.objects.get(pk=pk)
    rekening.delete()
    return HttpResponseRedirect('/bo/rekening')