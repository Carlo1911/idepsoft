from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, tipo_usuario, password, **extra_fields):
        """
        Create un usuario con el correo y contraseña
        """
        if not email:
            raise ValueError('Se debe establecer un correo')
        if not tipo_usuario:
            raise ValueError('Se debe establecer un tipo')
        email = self.normalize_email(email)
        user = self.model(email=email, tipo_usuario=tipo_usuario,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, tipo_usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, tipo_usuario, password, **extra_fields)

    def create_superuser(self, email, tipo_usuario, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe ser is_superuser=True.')
        return self._create_user(email, tipo_usuario, password, **extra_fields)
