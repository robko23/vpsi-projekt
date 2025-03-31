from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    weight = models.FloatField(null=True, blank=True, help_text="Váha v kg")
    height = models.FloatField(null=True, blank=True, help_text="Výška v cm")
    age = models.PositiveIntegerField(null=True, blank=True, help_text="Věk v letech")

    GENDER_CHOICES = [
        ('M', 'Muž'),
        ('F', 'Žena')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    basal_metabolic_rate = models.FloatField(null=True, blank=True, help_text="Bazální metabolismus v kcal")

    def save(self, *args, **kwargs):
        if self.weight and self.height and self.age and self.gender:
            self.calculate_basal_metabolic_rate()
        super().save(*args, **kwargs)

    def calculate_basal_metabolic_rate(self):
        if self.gender == 'M':
            self.basal_metabolic_rate = 88.36 + (13.4 * self.weight) + (4.8 * self.height) - (5.7 * self.age)
        elif self.gender == 'F':
            self.basal_metabolic_rate = 447.6 + (9.2 * self.weight) + (3.1 * self.height) - (4.3 * self.age)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user.email})"
    
    @property
    def basal_metabolic_rate_display(self):
        return round(self.basal_metabolic_rate, 2) if self.basal_metabolic_rate else None

