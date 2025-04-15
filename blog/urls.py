from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('buscar_post/', views.buscar_post, name='buscar_post'),
]
