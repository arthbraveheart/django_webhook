from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationFormForm
# Create your models here.
class SurveyResponse(models.Model):
    nome_representante = models.CharField(max_length=100)
    regional           = models.CharField(max_length=100)
    cliente            = models.CharField(max_length=50)
    cnpj_cliente       = models.CharField(max_length=50)
    telefone_cliente   = models.CharField(max_length=50)
    loja_existe        = models.CharField(max_length=50)
    comprou_tubozan    = models.CharField(max_length=50)
    conhece_dvg        = models.CharField(max_length=50)
    segmento           = models.CharField(max_length=50)
    parou_de_comprar   = models.CharField(max_length=50)
    tamanho            = models.CharField(max_length=50)
    fez_pedido         = models.CharField(max_length=50)
    sem_pedido         = models.CharField(max_length=50)
    concorrente        = models.CharField(max_length=50)
    dif_price          = models.CharField(max_length=50)
    obs                = models.TextField(blank=True)
    submitted_by       = models.ForeignKey(User, on_delete=models.CASCADE)

class LoginEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
