from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.timezone import now



class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        USER = "user", "User"

    class Language(models.TextChoices):
        ENG = "en", "English"
        RU = "de", "Deutsch"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)
    language = models.CharField(
        max_length=2,
        choices=Language.choices,
        default=Language.ENG,
    )
    is_blocked = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # After confirm email