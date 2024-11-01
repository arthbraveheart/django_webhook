from django import forms
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SurveyForm(forms.Form):
    # Text question
    nome_representante = forms.CharField(label="Nome do Representante", max_length=100)
    regional           = forms.CharField(label="Regional", max_length=100)
    cliente            = forms.CharField(label="Cliente", max_length=100)
    cnpj_cliente       = forms.CharField(label="CNPJ do Cliente", max_length=100)
    telefone_cliente       = forms.CharField(label="Número do Telefone (Whatsapp)", max_length=100)


    # Radio button question
    QUESTION_1_CHOICES = [
        ('sim', 'Sim'),
        ('não', 'Não'),
        #('maybe', 'Maybe'),
    ]
    loja_existe = forms.ChoiceField(
        label="Loja Existe",
        choices=QUESTION_1_CHOICES,
        widget=forms.RadioSelect,
    )

    # Another radio button question
    QUESTION_2_CHOICES = [
        ('precon', 'Precon'),
        ('sical', 'Sical'),
        ('tubozan', 'Tubozan'),
        ('detali', 'Detali'),
        ('decoralita', 'Decoralita'),
        ('não', 'Não'),
    ]
    conhece_dvg = forms.MultipleChoiceField(
        label="Conhece alguma marca do GRUPO DVG",
        choices=QUESTION_2_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    # Text area for comments
    obs = forms.CharField(
        label="Observacoes",
        widget=forms.Textarea,
        required=False,
    )


