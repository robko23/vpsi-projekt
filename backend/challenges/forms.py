from django import forms
from .models import Challenge, UserChallenge

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ["title", "description", "metric", "start", "end", "category"]

class UserChallengeForm(forms.ModelForm):
    class Meta:
        model = UserChallenge
        fields = ["challenge", "result", "comment"]