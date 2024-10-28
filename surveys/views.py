from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import SurveyResponse

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            SurveyResponse.objects.create(#**form.cleaned_data)
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                question_1=form.cleaned_data['question_1'],
                question_2=form.cleaned_data['question_2'],
                comments=form.cleaned_data.get('comments', ''),)
            return redirect('success')
    else:
        form = SurveyForm()
    return render(request, 'survey.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')