from django.contrib import admin
from .models import Food
from .models import FoodRecord
# Register your models here.
admin.site.register(Food)
admin.site.register(FoodRecord)