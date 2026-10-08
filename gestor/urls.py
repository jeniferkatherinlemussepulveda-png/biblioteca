from django.contrib import admin
from django.urls import path
from biblioteca import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crearAutor/', views.crearAutor, name='crearAutor'),
    path('editarAutor/<int:autor_id>/', views.editarAutor, name='editarAutor'),
    path('eliminarAutor/<int:autor_id>/', views.eliminarAutor, name='eliminarAutor'),
    path('crearLibro/', views.crearLibro, name='crearLibro'),
    path('',views.listarLibros,name='listarlibros'),
    path('editarLibro/<int:libro_id>/', views.editarLibro, name='editarLibro'),
    path('eliminarLibro/<int:libro_id>/', views.eliminarLibro, name='eliminarLibro'),
    path('listarAutores/',views.listarAutores,name='listarAutores'),
    ]
