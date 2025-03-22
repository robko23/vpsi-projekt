from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField()
    metric = models.CharField(max_length=30)
    start = models.CharField(max_length=60)
    end = models.CharField(max_length=60)
    category = models.CharField(max_length=30)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="challenges", default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserChallenge(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete = models.PROTECT, related_name="user_challenges")
    result = models.CharField(max_length=30)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.PROTECT, related_name="user_challenges")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"