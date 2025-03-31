from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("editProfile/", views.UserProfileUpdateView.as_view(), name="profile_update"),
]
