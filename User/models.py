from django.db import models

# Create your models here.
from encodings.punycode import digits
from django.contrib.auth.models import AbstractUser

from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class CustomUser(AbstractUser):

    # ОБЯЗАТЕЛЬНО добавь эти поля с related_name!
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_groups',  # ← УНИКАЛЬНЫЙ related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_permissions',  # ← УНИКАЛЬНЫЙ related_name
        related_query_name='user',
    )

    phone = models.CharField(max_length=12, unique=True, verbose_name='phone', blank=True)
    is_seller = models.BooleanField(default=False, verbose_name='seller')


    def check_phone(self):
        if len(self.phone) != 12:
             raise ValidationError('Номер должен состоять из 12 символов')
        if not self.phone.startswith('+'):
            raise ValidationError('Номер должен начинаться с +')
        if not self.phone[1:].isdigit():
            raise ValidationError('Номер должен состоять из цифр после знака +')



    def save(self, *args, **kwargs):
        if not self.is_superuser and self.phone:
            self.check_phone()
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Имя : {self.first_name.title()}, Фамилия : {self.last_name.title()}'

