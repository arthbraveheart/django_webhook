from django.db import models

# Create your models here.
class SurveyResponse(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question_1 = models.CharField(max_length=50)
    question_2 = models.CharField(max_length=50)
    comments = models.TextField(blank=True)
