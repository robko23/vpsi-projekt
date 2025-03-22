from django.contrib import admin
from .models import Challenge, UserChallenge

# Register your models here.

admin.site.register(Challenge)
admin.site.register(UserChallenge)