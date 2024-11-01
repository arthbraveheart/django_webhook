from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import SurveyResponse
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, RegisterForm

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            SurveyResponse.objects.create(#**form.cleaned_data)
                nome_representante=form.cleaned_data['nome_representante'],
                regional          =form.cleaned_data['regional'],
                cliente           =form.cleaned_data['cliente'],
                cnpj_cliente      =form.cleaned_data['cnpj_cliente'],
                telefone_cliente  =form.cleaned_data['telefone_cliente'],
                loja_existe       =form.cleaned_data['loja_existe'],
                conhece_dvg       =form.cleaned_data['conhece_dvg'],
                segmento          =form.cleaned_data['segmento'],
                tamanho           =form.cleaned_data['tamanho'],
                parou_de_comprar  =form.cleaned_data['parou_de_comprar'],
                fez_pedido        =form.cleaned_data['fez_pedido'],
                sem_pedido        =form.cleaned_data['sem_pedido'],
                concorrente       =form.cleaned_data['concorrente'],
                dif_price         =form.cleaned_data['dif_price'],
                comprou_tubozan   =form.cleaned_data['comprou_tubozan'],
                submitted_by      = request.user,
                obs               =form.cleaned_data.get('obs', ''),)

            return redirect('success')
    else:
        form = SurveyForm()
    return render(request, 'forms/survey.html', {'form': form})

def success_view(request):
    return render(request, 'forms/success.html')

