from django.db import models

    
class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=2, null=True)
    country = models.CharField(max_length=50, null=True)
    dscrptn = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    lastName = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True, blank="")
    gender = models.CharField(max_length=15, null=True)
    occupation = models.CharField(max_length=30, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    

