from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# TODO: are there more units than meters and repetitions? if no, we could inline this table into sport
class MeasurementUnit(models.Model):
    # For example kilometers, or repetitions
    full_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    # is this an SI unit? if yes, we offer automatic conversions
    # unit definition can be meters, and we mark is as SI, we can show user select for km or m
    si = models.BooleanField()
    pass

class Sport(models.Model):
    # Human-readable name of a sport
    name = models.CharField(max_length=100)
    # Machine-readable name of a sport
    code = models.CharField(max_length=100)

    # what unit are we working with?
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
    # how many kilo-calories we burn per one unit?
    # example:
    # XXX kcal per 1km running
    # XX kcal per 1 repetition
    calories_per_unit = models.FloatField()
    pass

class ActivityRecord(models.Model):
    class VisibilityChoices(models.TextChoices):
        PRIVATE = "private", _("Private")
        FRIENDS = "friends", _("Friends")
        PUBLIC = "public", _("Public")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # Derived (end_time - start_time) for easier querying and filtering
    duration = models.FloatField()

    # if unit in sport is kilometers, this says how many kilometers we ran
    recorded_units = models.FloatField()

    # derived value from (self.recorded_units * sport.calories_per_unit)
    calories_burned = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    visibility = models.CharField(
        max_length=10,
        choices=VisibilityChoices,
        default=VisibilityChoices.PRIVATE
    )
    pass