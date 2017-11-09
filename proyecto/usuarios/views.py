from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import (
    HttpResponseRedirect, Http404, HttpResponse, HttpResponseNotAllowed)
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import User
from .forms import UserForm, UserLoginForm
from .managers import UserManager


class UsuarioMixin:

    def get_context_data(self, **kwargs):
        context = super(UsuarioMixin, self).get_context_data(**kwargs)
        return context


class IniciarSesion(UsuarioMixin, TemplateView):

    """Vista para iniciar sesión"""
    template_name = "usuarios/login.html"
    model = User
    form_class = UserLoginForm
    object = None

    def dispatch(self, request, *args, **kwargs):
        return super(IniciarSesion, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(IniciarSesion, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IniciarSesion, self).get_context_data(**kwargs)
        context.update({
            'usuario': UserLoginForm(),
        })
        return context

    def form_valid(self, form):
        return super(IniciarSesion, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if request:
            form = UserLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")
                user = authenticate(request, email=email, password=password)
                if user:
                    login(request, user)
                else:
                    return render(request, self.template_name, {'usuario': form})
            else:
                return render(request, self.template_name, {'usuario': form})
        return HttpResponseRedirect(reverse('usuarios:usuario_perfil',
                                            kwargs={'usuario_id': user.id}))


@login_required
def CerrarSesion(request):
    """Vista para cerrar sesión"""
    logout(request)
    return redirect('home')
    object = None


@method_decorator(login_required, name='dispatch')
class Perfil(UsuarioMixin, TemplateView):

    """docstring for ClassName"""
    template_name = "user-profile.html"
    object = None

    def dispatch(self, request, *args, **kwargs):
        return super(Perfil, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(Perfil, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Perfil, self).get_context_data(**kwargs)
        context.update({
            'usuario': User.objects.get(id=kwargs['usuario_id'])
        })
        return context


class Registrar(UsuarioMixin, TemplateView):

    """Vista para registrar usuario"""
    template_name = "usuarios/register.html"
    model = User
    form_class = UserForm
    object = None

    def dispatch(self, request, *args, **kwargs):
        return super(Registrar, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(Registrar, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Registrar, self).get_context_data(**kwargs)
        context.update({
            'usuario': UserForm(),
        })
        return context

    def form_valid(self, form):
        return super(Registrar, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if request:
            form = UserForm(request.POST)
            if form.is_valid():
                self.object = form.save()
                login(request, self.object)
            else:
                return render(request, self.template_name, {'usuario': form})
        return HttpResponseRedirect(reverse('usuarios:usuario_perfil',
                                            kwargs={'usuario_id': self.object.id}))


class RecuperarContrasena(UsuarioMixin, TemplateView):

    """docstring for ClassName"""
    template_name = "user-forgot-password.html"


class BloquearPantalla(UsuarioMixin, TemplateView):

    """docstring for ClassName"""
    template_name = "user-lock-screen.html"
