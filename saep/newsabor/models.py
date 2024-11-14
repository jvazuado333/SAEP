from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)  
    email = models.CharField(max_length=150)  
    nickname = models.CharField(max_length=60)  
    senha = models.CharField(max_length=60, min_length=8)  
    foto = models.CharField(max_length=150)  
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.nickname

class Empresa(models.Model):
    id_empresa = models.IntegerField(primary_key=True)  
    nome = models.CharField(max_length=100)
    logo = models.CharField(max_length=60)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.nome

class Publicacao(models.Model):
    id_publicacao = models.IntegerField(primary_key=True)  
    foto = models.CharField(max_length=150)  
    titulo_prato = models.CharField(max_length=60)  
    local = models.CharField(max_length=255)  
    cidade = models.CharField(max_length=55)  
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)  

    def __str__(self):
        return self.titulo_prato
