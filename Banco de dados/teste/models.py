from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    idade = models.IntegerField(blank=True)
    email = models.EmailField(blank =True, default="", null=True)
    cpf = models.CharField(max_length=11, blank=True)
    date_added = models.DateTimeField(auto_now=True)
    
    ESTADO_CIVIL_CHOICES = [
        ('CS', 'Casado'),
        ('VD', 'Viuvo'),
        ('SE', 'Separado'),
        ('UN', 'União Estável'),
        ('OU', 'Outros'),
        ('', 'Nenhum'),
    ]
    
    GENERO_CHOICES = [
        ('FE', 'Feminino'),
        ('MA', 'Masculino'),
        ('AG', 'Agenero'),
        ('FL', 'Genero Fluido'),
        ('NB', 'Nao Binario'),
        ('OU', 'Outro'),
        ('', 'Nenhum'),
    ]
    
    estado_civil = models.CharField(
        max_length=2,
        choices=ESTADO_CIVIL_CHOICES,
        default="",
        blank=True)
    
    genero = models.CharField(
        max_length=2,
        choices=GENERO_CHOICES,
        default="",
        blank=True
    )


    def __str__(self):
        return self.nome
    
    
    

