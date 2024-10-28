from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import SurveyResponse

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            SurveyResponse.objects.create(**form.cleaned_data)
            return redirect('success')
    else:
        form = SurveyForm()
    return render(request, 'surveys/survey.html', {'form': form})
