from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.survey_view, name='survey'),
    path('success/', views.success_view, name='success'),  # Define a success view or template for redirection
]
