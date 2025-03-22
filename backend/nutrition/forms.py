from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["name", "calories", "carbs", "protein", "fat", "sodium", "serving_size"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"}),
            "calories": forms.NumberInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"}),
            "carbs": forms.NumberInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"}),
            "protein": forms.NumberInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"}),
            "fat": forms.NumberInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"}),
            "sodium": forms.NumberInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"}),
            "serving_size": forms.TextInput(attrs={"class": "w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"}),
        }
