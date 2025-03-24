from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('incoming_requests/', views.incoming_requests, name='incoming_requests'),
    path('add_friends/', views.add_friends, name='add_friends'),
    path('list_friends/', views.list_friends, name='list_friends'),
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:request_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('remove_friend/<int:friend_id>/', views.remove_friend, name='remove_friend'),
]

