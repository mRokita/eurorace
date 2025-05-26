from drf_extra_fields.geo_fields import PointField
from rest_framework import serializers

from eurorace.models import LocationReport


class LocationReportSerializer(serializers.ModelSerializer):
    location = PointField()
    class Meta:
        fields = ("location", "timestamp", "user")
        model = LocationReport
