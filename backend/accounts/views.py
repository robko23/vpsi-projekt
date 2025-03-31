from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from .forms import UserProfileForm

# View pro registraci
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Automatické přihlášení uživatele
        
        # Vytvoření UserProfile, pokud neexistuje
        profile, created = UserProfile.objects.get_or_create(user=user)
        
        # Přesměrování na stránku pro editaci profilu
        return redirect("profile_update")


# View pro editaci profilu
class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "registration/userprofile_form.html"

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfile, user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("profile_update")
