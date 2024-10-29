from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import RegisterForm
# Create your views here.
"""
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        # Save the login event
        ip_address = self.request.META.get('REMOTE_ADDR')
        LoginEvent.objects.create(user=user, ip_address=ip_address)

        return super().form_valid(form)"""


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = RegisterForm.objects.create(

                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                username=form.cleaned_data['username'],
                password1=form.cleaned_data['password1'],


            )#form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})