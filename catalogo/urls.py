"""Rutas de la app catalogo."""
from django.urls import path

from . import views

app_name = 'catalogo' 

urlpatterns = [
    path('', views.home, name='home'),                                  # FBV
    path('catalogo/', views.CatalogoListView.as_view(), name='lista'),  # CBV
    path('catalogo/<int:pk>/', views.detalle, name='detalle'),          # FBV
]