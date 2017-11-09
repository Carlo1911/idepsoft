# coding:utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import User  # , Usuario


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'nombres', 'apellido_paterno', 'apellido_materno',
                  'es_activo', 'tipo_usuario',
                  'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['nombres'].required = True

    def clean_nombres(self):
        data = self.cleaned_data['nombres']
        return data

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput(attrs={'placeholder':'Enter Password Again'}),
                                help_text=_("Enter the same password as above, for verification."))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Email Address'}))

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):

    class Meta:
        fields = ('email', 'password')
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput)
    email = forms.EmailField(label=_("Email"))
