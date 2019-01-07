from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_user, name="index_user"),
    
    url(r'bo/user', views.index_user, name="index_user"),
    url(r'bo/form_user/', views.form_user, name="form_user"),
    url(r'bo/edit_user/(?P<pk>\d+)$', views.edit_user, name='edit_user'),
    url(r'bo/delete_user/(?P<pk>\d+)$', views.delete_user, name='delete_user'), 

    url(r'bo/organisasi', views.index_organisasi, name="index_organisasi"),
    url(r'bo/form_organisasi/', views.form_organisasi, name="form_organisasi"),
    url(r'bo/edit_organisasi/(?P<pk>\d+)$', views.edit_organisasi, name='edit_organisasi'),
    url(r'bo/delete_organisasi/(?P<pk>\d+)$', views.delete_organisasi, name='delete_organisasi'), 

    url(r'bo/gallery', views.index_gallery, name="index_gallery"),
	url(r'bo/form_gallery/', views.form_gallery, name="form_gallery"),
	url(r'bo/edit_gallery/(?P<pk>\d+)$', views.edit_gallery, name='edit_gallery'),
	url(r'bo/delete_gallery/(?P<pk>\d+)$', views.delete_gallery, name='delete_gallery'), 

	url(r'bo/kegiatan', views.index_kegiatan, name="index_kegiatan"),
    url(r'bo/form_kegiatan/', views.form_kegiatan, name="form_kegiatan"),
    url(r'bo/edit_kegiatan/(?P<pk>\d+)$', views.edit_kegiatan, name='edit_kegiatan'),
    url(r'bo/delete_kegiatan/(?P<pk>\d+)$', views.delete_kegiatan, name='delete_kegiatan'),

    url(r'bo/berita', views.index_berita, name="index_berita"),
    url(r'bo/form_berita/', views.form_berita, name="form_berita"),
    url(r'bo/edit_berita/(?P<pk>\d+)$', views.edit_berita, name='edit_berita'),
    url(r'bo/delete_berita/(?P<pk>\d+)$', views.delete_berita, name='delete_berita'),

    url(r'bo/rekening', views.index_rekening, name="index_rekening"),
    url(r'bo/form_rekening/', views.form_rekening, name="form_rekening"),
    url(r'bo/edit_rekening/(?P<pk>\d+)$', views.edit_rekening, name='edit_rekening'),
    url(r'bo/delete_rekening/(?P<pk>\d+)$', views.delete_rekening, name='delete_rekening'), 

]