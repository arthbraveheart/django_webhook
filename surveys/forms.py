from django import forms


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
