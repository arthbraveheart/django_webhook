from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SurveyForm(forms.Form):
    # Text question
    nome_representante = forms.CharField(label="Nome do Representante", max_length=100, required=True,)
    regional = forms.CharField(label="Regional", max_length=100, required=True,)
    cliente = forms.CharField(label="Cliente", max_length=100, required=True,)
    cnpj_cliente = forms.CharField(label="CNPJ do Cliente", max_length=100, required=True,)
    telefone_cliente = forms.CharField(label="Número do Telefone (Whatsapp)", max_length=100, required=True,)

    # Radio button question
    QUESTION_1_CHOICES = [
        ('sim', 'Sim'),
        ('não', 'Não'),
        # ('maybe', 'Maybe'),
    ]
    loja_existe = forms.ChoiceField(
        label="Loja Existe",
        choices=QUESTION_1_CHOICES,
        widget=forms.RadioSelect,
    )
    comprou_tubozan = forms.ChoiceField(
        label="Já comprou da TUBOZAN",
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
    QUESTION_3_CHOICES = [
        ('price', 'Preco'),
        ('fidelidade', 'Fidelidade com concorrente'),
        ('qualidade', 'Qualidade do produto'),
        ('prazo', 'Prazo de entrega'),
        ('atendimento', 'Atendimento'),
        ('outro_fornecedor', 'Já comprou de outro fornecedor este mes'),
        ('não', 'Não'),
    ]

    QUESTION_4_CHOICES = [
        ('depósito', 'Depósito Geral'),
        ('ferragem', 'Ferragem'),
        ('acabamento', 'Acabamento'),
        ('tintas_imp', 'Tintas / Impermeabilizacao'),
        ('hidraulica_ele', 'Hidráulica / Elétrica'),

    ]

    QUESTION_5_CHOICES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
        ('atacado_dist', 'Atacado / Distribuidor'),


    ]

    QUESTION_6_CHOICES = [
        ('relacionamento', 'Início de Relacionamento'),
        ('price', 'Preco'),
        ('fidelidade', 'Fidelidade com concorrente'),
        ('qualidade', 'Qualidade do produto'),
        ('prazo', 'Prazo de entrega'),
        ('atendimento', 'Atendimento'),
        ('variedade', 'Variedade de produtos'),

    ]

    QUESTION_7_CHOICES = [
        ('tigre', 'Tigre'),
        ('amanco', 'Amanco'),
        ('fortlev', 'Fortlev'),
        ('krona', 'Krona'),
        ('plastilit', 'Plastilit'),

    ]

    QUESTION_8_CHOICES = [
        ('muito_caro', 'Muito mais caro'),
        ('caro', 'Um pouco mais caro'),
        ('igual', 'Igual'),
        ('barato', 'Umpouco mais barato'),

    ]

    conhece_dvg = forms.MultipleChoiceField(
        label="Conhece alguma marca do GRUPO DVG",
        choices=QUESTION_2_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    parou_de_comprar = forms.MultipleChoiceField(
        label="Porque parou de comprar?",
        choices=QUESTION_3_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    segmento = forms.MultipleChoiceField(
        label="Segmento da Loja",
        choices=QUESTION_4_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    tamanho = forms.ChoiceField(
        label="Tamanho",
        choices=QUESTION_5_CHOICES,
        widget=forms.RadioSelect,
    )

    fez_pedido = forms.ChoiceField(
        label="Fez o pedido",
        choices=QUESTION_1_CHOICES,
        widget=forms.RadioSelect,
    )

    sem_pedido = forms.ChoiceField(
        label="Porque não efetuamos o Pedido",
        choices=QUESTION_6_CHOICES,
        widget=forms.RadioSelect,
    )

    concorrente = forms.ChoiceField(
        label="Qual concorrente?",
        choices=QUESTION_7_CHOICES,
        widget=forms.RadioSelect,
    )

    dif_price = forms.ChoiceField(
        label="Diferenca de Preco",
        choices=QUESTION_8_CHOICES,
        widget=forms.RadioSelect,
    )

    # Text area for comments
    obs = forms.CharField(
        label="Observacoes",
        widget=forms.Textarea,
        required=True,
    )


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))

class RegisterForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]