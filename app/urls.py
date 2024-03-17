from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('katalog', views.katalog, name='katalog'),
    path('detailbuku/Atlas-Indonesia-Junior-38-Provinsi', views.detailproduk, name='detailbuku'),
]