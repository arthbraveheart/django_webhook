from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationFormForm
# Create your models here.
class SurveyResponse(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question_1 = models.CharField(max_length=50)
    question_2 = models.CharField(max_length=50)
    comments = models.TextField(blank=True)




class LoginEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
