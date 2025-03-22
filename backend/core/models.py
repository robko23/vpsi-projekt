from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


# TODO: are there more units than meters and repetitions? if no, we could inline this table into sport
class MeasurementUnit(models.Model):
    # For example kilometers, or repetitions
    full_name = models.CharField(max_length=100, help_text=_("Full name of the unit (eg. Meters)"))
    code = models.CharField(max_length=100, help_text=_("Short code of the unit (eg. m)"))
    # is this an SI unit? if yes, we offer automatic conversions
    # unit definition can be meters, and we mark is as SI, we can show user select for km or m
    si = models.BooleanField(help_text=_(
        "Is this unit standard SI measurement unit? Example of SI unit is meter, while steps is not. SI measurement units will get automatic conversion based on SI spec (example: 1000 m -> 1 km)"))

    def __str__(self):
        return self.full_name + " (" + self.code + ")"
    pass


class Sport(models.Model):
    # Human-readable name of a sport
    name = models.CharField(max_length=100, help_text=_("Name of the sport (eg. Running)"))
    # Machine-readable name of a sport
    code = models.CharField(max_length=100, help_text=_("Short code of the sport (eg. RUN)"))

    # what unit are we working with?
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE,
                             help_text=_("Unit that this sport is measured in. For running, this would be meters"))
    # how many kilo-calories we burn per one unit?
    # example:
    # XXX kcal per 1km running
    # XX kcal per 1 repetition
    calories_per_unit = models.FloatField(help_text=_(
        "How many calories you burn per measurement unit in this sport. For example climbing is 300 calories per hour of climbing"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super(Sport, self).save(*args, **kwargs)
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
    # Derived (end_time - start_time) for easier querying and filtering (in seconds)
    duration = models.FloatField()

    # if unit in sport is kilometers, this says how many kilometers we ran
    recorded_units = models.FloatField()

    # derived value from (self.recorded_units * sport.calories_per_unit)
    calories_burned = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    visibility = models.CharField(
        max_length=10,
        choices=VisibilityChoices.choices,  # ✅ Opraveno!
        default=VisibilityChoices.PRIVATE
    )
