from drf_extra_fields.geo_fields import PointField
from rest_framework import serializers

from eurorace.models import LocationReport, Factory


class LocationReportSerializer(serializers.ModelSerializer):
    location = PointField()
    class Meta:
        fields = ("location", "timestamp", "user")
        model = LocationReport


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "description")
        model = Factory
