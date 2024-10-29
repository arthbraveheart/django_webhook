from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.survey_view, name='survey'),
    path('success/', views.success_view, name='success'),  # Define a success view or template for redirection
    #path('login/', views.CustomLoginView.as_view(), name='login'),
    #path('sign_up/', views.sign_up, name='sign_up'),
]
