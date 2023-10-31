from django.db import models

# Create your models here.
class Contato(models.Model):

#Opções do campo Estado Civil
#Primeiro valor da tupla é oq vai no banco, o segunda mostra na tela
    ESTADO_CIVIS = [('S','Solteiro'), ('C','Casado'), ('D','Divorciado'), ('V','Viúvo')]

    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField(verbose_name='Data de Aniversario')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    estado_civis = models.CharField(max_length=1, choices=ESTADO_CIVIS, null=True)

    def __str__(self):
        return self.nome

    # configuração deste modelo
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'







    



