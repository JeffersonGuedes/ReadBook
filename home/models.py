from django.db import models
from django.contrib.auth.models import User


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255, blank=True, null=True)
    data_publicacao = models.DateField(blank=True, null=True)
    editora = models.CharField(max_length=255, blank=True, null=True)
    numero_paginas = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    idioma = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    formato = models.CharField(max_length=50, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_adicao = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='livros', default=1)

    def __str__(self):
        return f"Form {self.id} for {self.user.username}"