from django.shortcuts import render, get_object_or_404, redirect
from .models import Challenge
from .forms import ChallengeForm, UserChallengeForm

def challenge_list(request):
    challenges = Challenge.objects.all()
    return render(request, "challenges/challenge_list.html", {"challenges": challenges})

def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    return render(request, "challenges/challenge_detail.html", {"challenge": challenge})

def create_challenge(request):
    if request.method == "POST":
        form = ChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.creator = request.user
            challenge.save()
            return redirect("challenge_list")
    else:
        form = ChallengeForm()
    return render(request, "challenges/create_challenge.html", {"form": form})

def add_user_result(request):
    if request.method == "POST":
        form = UserChallengeForm(request.POST)
        if form.is_valid():
            user_challenge = form.save(commit=False)
            user_challenge.user = request.user
            user_challenge.save()
            return redirect("challenge_list") 
    else:
        form = UserChallengeForm()
    
    return render(request, "challenges/add_user_result.html", {"form": form})