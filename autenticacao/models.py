from django.db import models


class Cargos (models.Model):
    nome = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.nome
    
class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField()
    senha = models.CharField(max_length = 100)
    cargo = models.ManyToManyField(Cargos)

    def __str__(self):
        return self.nome