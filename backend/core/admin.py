from django.contrib import admin

from core.models import MeasurementUnit, Sport


class MeasurementUnitAdmin(admin.ModelAdmin):
    list_filter = ["si"]
    list_display =  ["full_name", "code", "si"]
    pass

class SportAdmin(admin.ModelAdmin):
    list_filter = ["unit"]
    list_display = ["name", "code", "unit", "calories_per_unit"]
    pass

admin.site.register(MeasurementUnit, MeasurementUnitAdmin)
admin.site.register(Sport, SportAdmin)