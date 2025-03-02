from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from eurorace.models import LocationReport


@admin.register(LocationReport)
class LocationReportAdmin(LeafletGeoAdmin):
    list_display = ("location", "timestamp")