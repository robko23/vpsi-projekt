from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['weight', 'height', 'age', 'gender', 'basal_metabolic_rate']
        widgets = {
            'basal_metabolic_rate': forms.TextInput(attrs={'readonly': 'readonly'})
        }