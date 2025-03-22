from django import forms
from .models import ActivityRecord
from django.utils.timezone import make_naive
from django.utils.translation import gettext_lazy as _


class ActivityRecordForm(forms.ModelForm):
    class Meta:
        model = ActivityRecord
        fields = ['sport', 'start_time', 'end_time', 'recorded_units', 'visibility']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)

        if user is None:
            raise forms.ValidationError(_('Must be logged in to save activity record'))
        instance.user = user

        # Calc duration
        instance.duration = (instance.end_time - instance.start_time).total_seconds()

        # Calc calories
        instance.calories_burned = instance.recorded_units * instance.sport.calories_per_unit

        if commit:
            instance.save()
        return instance

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_time')
        end = cleaned_data.get('end_time')
        if start and end and end <= start:
            raise forms.ValidationError(_("End time must be after start time."))
        return cleaned_data
