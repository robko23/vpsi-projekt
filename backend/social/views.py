from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import FriendRequest

# Create your views here.

def index(request):
    return render(request, 'social/index.html')

def get_friends(user):
    qs_from = FriendRequest.objects.filter(from_user=user, is_accepted=True).values_list('to_user', flat=True)
    qs_to = FriendRequest.objects.filter(to_user=user, is_accepted=True).values_list('from_user', flat=True)

    friend_ids = list(qs_from) + list(qs_to)
    return User.objects.filter(id__in=friend_ids)

@login_required
def incoming_requests(request):
    friend_requests = FriendRequest.objects.filter(
        to_user=request.user,
        is_accepted=False
    )
    return render(request, 'social/incoming_requests.html', {
        'friend_requests': friend_requests
    })

@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
    friend_request.is_accepted = True
    friend_request.save()
    return redirect('incoming_requests')

@login_required
def reject_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
    friend_request.delete()
    return redirect('incoming_requests')

@login_required
def add_friends(request):
    search_query = request.GET.get('search', '').strip()
    possible_friends = None

    if search_query:
        my_friends = get_friends(request.user)
        pending_sent = FriendRequest.objects.filter(
            from_user=request.user, is_accepted=False
        ).values_list('to_user', flat=True)
        pending_received = FriendRequest.objects.filter(
            to_user=request.user, is_accepted=False
        ).values_list('from_user', flat=True)

        exclude_ids = list(my_friends.values_list('id', flat=True)) \
                      + list(pending_sent) \
                      + list(pending_received) \
                      + [request.user.id]

        possible_friends = User.objects.exclude(id__in=exclude_ids) \
                                       .filter(username__icontains=search_query)

    return render(request, 'social/add_friends.html', {
        'search_query': search_query,
        'possible_friends': possible_friends
    })

@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)

    existing_request = FriendRequest.objects.filter(
        from_user=request.user,
        to_user=to_user,
        is_accepted=False
    ).first()
    if not existing_request:
        FriendRequest.objects.create(from_user=request.user, to_user=to_user)

    return redirect('add_friends')

@login_required
def list_friends(request):
    friends = get_friends(request.user)
    return render(request, 'social/list_friends.html', {
        'friends': friends
    })

@login_required
def remove_friend(request, friend_id):
    friend = get_object_or_404(User, id=friend_id)
    fr = FriendRequest.objects.filter(
        is_accepted=True
    ).filter(
        Q(from_user=request.user, to_user=friend) | Q(from_user=friend, to_user=request.user)
    ).first()

    if fr:
        fr.delete()

    return redirect('list_friends')
