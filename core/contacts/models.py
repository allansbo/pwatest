from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='nome')
    last_name = models.CharField(max_length=100, verbose_name='sobrenome')
    phone = PhoneNumberField(verbose_name='telefone', unique=True)
    email = models.EmailField(verbose_name='e-mail', unique=True)
    city = models.CharField(max_length=120, verbose_name='cidade')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'
