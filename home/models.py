from django.db import models
from django.utils import timezone

class FormularioUser(models.Model):
    section_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    nome = models.CharField(max_length=300, default='Desconhecido')
    pais = models.CharField(max_length=300, default='Desconhecido')
    cor = models.CharField(max_length=200, default='Desconhecido')
    nicho = models.CharField(max_length=200, default='Desconhecido')
    link_store = models.URLField(max_length=200, default='Desconhecido')
    url_loja = models.URLField(max_length=200, default='Desconhecido')
    plan = models.BooleanField(default=False)
    token_senha = models.CharField(max_length=200, default='Desconhecido')
    chave_de_api = models.CharField(max_length=200, default='Desconhecido')
    chave_secreta = models.CharField(max_length=200, default='Desconhecido')
    produt= models.BooleanField(default=False)
    banners = models.BooleanField(default=False)
    telefone = models.CharField(max_length=300, default='Desconhecido')
    email_suporte = models.EmailField(max_length=254, default='Desconhecido')
    empresa = models.CharField(max_length=300, default='Desconhecido')
    business_hours = models.CharField(max_length=300, default='Desconhecido')
    lojaproduzida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now)
    

    def data_criacao_formatada(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M:%S')

    def __str__(self):
        return f'Formulário de {self.nome} criado em {self.data_criacao_formatada()}'
