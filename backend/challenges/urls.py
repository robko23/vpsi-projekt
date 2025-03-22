from django.urls import path
from . import views
from .views import challenge_detail, add_user_result


urlpatterns = [
    path('', views.challenge_list, name='challenge_list'),
    path('<int:pk>/', challenge_detail, name='challenge_detail'),
    path('add/', views.create_challenge, name='create_challenge'),
    path("user_result/add/", add_user_result, name="add_user_result"),
]