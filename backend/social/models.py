from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from core.models import ActivityRecord


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="friend_requests_sent"
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="friend_requests_received"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user.username} -> {self.to_user.username}"


class Friendship(models.Model):
    # don't be confused about the from and to,
    # these fields are non-directional
    # from_user -> to_user = to_user -> from_user
    # there cannot exist two rows that have
    # from_user=Alice, to_user=Bob
    # from_user=Bob, to_user=Alice
    # because those two are equivalent
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="friendships_initiated"
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="friendships_received"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    pass


class ActivityRating(models.Model):
    activity = models.ForeignKey(ActivityRecord, on_delete=models.CASCADE)
    # Which user rated another users activity
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass


# If activity is not public (private, friends), user can selectively share activity with another user if they choose to
class ActivityShare(models.Model):
    activity = models.ForeignKey(ActivityRecord, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
