from django.urls import path
from . import views  # Import views z aktuální aplikace

urlpatterns = [
    path('', views.index, name='index'),
    path('meal-plan/', views.meal_plan, name='meal_plan'),
    path('daily/', views.daily, name='daily'),
    path("food-record/create/", views.food_record_create, name="food_record_create"),
    path("food-records/", views.food_record_list, name="food_record_list"),
    path('food/new/', views.food_create, name='food_create'),
    path('food/<int:id>/delete/', views.food_delete, name='food_delete'),
]
