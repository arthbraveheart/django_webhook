from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.shortcuts import render
from .models import Conversa
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import json


@csrf_exempt  # Isso desativa a verificação de CSRF para a requisição do Twilio
def whatsapp_reply(request):
    if request.method == "POST":

        #Get the content 4all:

        # Suas credenciais da conta Twilio
        account_sid = "AC069f1485becb681509aa3ea0b36dec02"  # Substitua pelo seu Account SID
        auth_token = "d53f84c881d473e27613feb55258c774"  # Substitua pelo seu Auth Token
        client = Client(account_sid, auth_token)

        # MessageSid da mensagem recebida
        message_sid = request.POST.get('MessageSid')#"SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Substitua pelo MessageSid da mensagem

        # Buscar os detalhes da mensagem usando o MessageSid
        message = client.messages(message_sid).fetch()

        remetente = request.POST.get('From')
        destinatario = request.POST.get('To')
        mensagem = message.body#request.POST.get('Body')

        # Armazenar a conversa no banco de dados
        conversa = Conversa(remetente=remetente, destinatario=destinatario, mensagem=mensagem)
        conversa.save()

        # Capturar a mensagem recebida
        incoming_msg = request.POST.get('Body')#.lower()

        # Criar uma resposta automática
        response = MessagingResponse()
        msg = response.message()

        # Definir a mensagem automática de resposta
        msg.body("Obrigado por entrar em contato! Recebemos sua mensagem e responderemos em breve.")

        # Retornar a resposta como XML para o Twilio
        return HttpResponse(str(response), content_type='text/xml')

    return HttpResponse("Método não permitido", status=405)

@csrf_exempt  # Ignorar a verificação CSRF para requisições externas
def whatsapp_webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Aqui você pode processar a mensagem recebida
        message_body = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
        sender_number = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

        # Exibir ou processar a mensagem como desejar
        print(f"Mensagem recebida de {sender_number}: {message_body}")

        # Retornar uma resposta para o Twilio
        return JsonResponse({'status': 'received'}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)