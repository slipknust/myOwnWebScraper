from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.title)


class OlxItem(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.title)

class TwitterItem(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.title)


class Perfil(models.Model):
    nome = models.CharField(max_length=255)
    data_nasc = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return '{}'.format(self.nome)