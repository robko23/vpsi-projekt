from django.conf import settings
from django.db import models

class InvalidFoodRecord(ValueError):
    pass

class Food(models.Model):
    name = models.CharField(max_length=100)
    # TODO: image?
    # image = models.ImageField(upload_to="nutrition/food/images", null=True, blank=True)

    # Nutrition facts per 100g
    calories = models.FloatField()
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    sodium = models.FloatField()

    # Optionally: serving size (e.g. "1 slice", "1 egg", "100g")
    serving_size = models.CharField(max_length=50, null=True, blank=True)
    pass

class FoodRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    # weight in grams (optional)
    weight = models.FloatField(null=True, blank=True)

    # servings (optional)
    servings = models.FloatField(null=True, blank=True)

    # Derived value: calculated calories based on either grams or servings
    calories_consumed = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """ Auto-calculate calories based on weight or servings """
        if self.weight:
            self.calories_consumed = (self.weight / 100) * self.food.calories
        elif self.servings and not self.food.serving_size:
            raise InvalidFoodRecord("Food.servings can be specified only for foods that have serving_size")
        elif self.servings and self.food.serving_size:
            # Example logic: 1 serving = 1 predefined portion size (e.g. "1 slice")
            self.calories_consumed = self.servings * self.food.calories
        else:
            raise InvalidFoodRecord("either FoodRecord.weight or FoodRecord.servings must be specified")
        super().save(*args, **kwargs)
    pass