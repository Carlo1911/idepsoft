from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/',
        views.IniciarSesion.as_view(),
        name='usuario_login'),
    url(r'^logout/',
        views.CerrarSesion,
        name='usuario_logout'),
    url(r'^perfil/(?P<usuario_id>\d+)',
        views.Perfil.as_view(),
        name='usuario_perfil'),
    url(r'^registrar/',
        views.Registrar.as_view(),
        name='usuario_registrar'),
    url(r'^recuperarcontrasena/',
        views.RecuperarContrasena.as_view(),
        name='usuario_recuperarcontrasena'),
    url(r'^bloquearpantalla/',
        views.BloquearPantalla.as_view(),
        name='usuario_bloquearpantalla'),

]
