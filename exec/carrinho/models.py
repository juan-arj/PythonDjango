from django.db import models

# Create your models here.
class Compra(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    email = models.TextField(max_length=150)
    endereco = models.TextField(max_length=100)
    cidade = models.TextField(max_length=50)
    cep = models.TextField(max_length=10)
    num_cartao = models.TextField(max_length=50)
    nome_cartao = models.TextField(max_length=100)
    validade = models.TextField(max_length=20)
    cvv = models.TextField(max_length=3)

    def __str__(self):
        return self.nome
    