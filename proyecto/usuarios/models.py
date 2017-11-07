from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    """
    Modelo de usuario
    """

    ADMIN = 'admin'
    EXPERTO = 'experto'
    REGULAR = 'regular'

    TIPO_CHOICES = (
        (ADMIN, u'Administrador'),
        (EXPERTO, u'Experto'),
        (REGULAR, u'Regular')
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tipo_usuario']

    email = models.EmailField(_('email address'), unique=True)
    nombres = models.CharField(_('Nombres'), max_length=100, blank=True)
    apellido_paterno = models.CharField(
        _('Apellido paterno'), max_length=50, blank=True)
    apellido_materno = models.CharField(
        _('Apellido materno'), max_length=50, blank=True)
    tipo_usuario = models.CharField(_('Tipo de usuario'), default=REGULAR,
                                    choices=TIPO_CHOICES, max_length=20)
    es_activo = models.BooleanField(_('Activo'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )

    objects = UserManager()

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_nombre_completo(self):
        '''
        Retorna el nobmre completo del usuario.
        '''
        nombre_completo = '%s %s %s' % (
            self.nombres, self.apellido_paterno, self.apellido_materno)
        return nombre_completo.strip()

    def get_short_name(self):
        '''
        Retorna nombre corto del usuario.
        '''
        nombre = '%s %s' % (self.nombres, self.apellido_paterno)
        return nombre.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
