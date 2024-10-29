from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SurveyForm(forms.Form):
    # Text question
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email")

    # Radio button question
    QUESTION_1_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
    ]
    question_1 = forms.ChoiceField(
        label="Do you like Django?",
        choices=QUESTION_1_CHOICES,
        widget=forms.RadioSelect,
    )

    # Another radio button question
    QUESTION_2_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    question_2 = forms.ChoiceField(
        label="What is your skill level in Django?",
        choices=QUESTION_2_CHOICES,
        widget=forms.RadioSelect,
    )

    # Text area for comments
    comments = forms.CharField(
        label="Any additional comments?",
        widget=forms.Textarea,
        required=False,
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