from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('webhook/', views.whatsapp_reply, name='whatsapp_reply'),
    path('webhook_talk/', views.whatsapp_webhook, name='whatsapp_webhook'),

]
