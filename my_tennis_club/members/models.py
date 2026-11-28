from django.db import models
# Create your models here.
# cria a classe Member para cadastrar os membros
class Member(models.Model):
    '''
    cria a classe Member para cadastrar os membros do site
    O primeiro campo, é um campo de Texto e conterá o primeiro nome dos membros.
    O segundo campo, também é um campo de Texto, com o sobrenome do membro.
    Ambos e estão configurados para ter um máximo de 255 caracteres.
    '''
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'