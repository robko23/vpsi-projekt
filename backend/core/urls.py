from core import views
from django.urls import path

urlpatterns = [
    path('activity/create', views.create_activity, name = "create_activity"),
    path('activity/', views.list_activities, name = "list_activities"),
]