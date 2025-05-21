from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from eurorace.models import LocationReport, Factory
from eurorace.serializers import LocationReportSerializer, FactorySerializer


class LocationReportViewSet(viewsets.ModelViewSet):
    queryset = LocationReport.objects.all()
    serializer_class = LocationReportSerializer


    @extend_schema(responses=LocationReportSerializer(many=True))
    @action(detail=False)
    def latest(self, request):
        return Response(LocationReportSerializer(instance=LocationReport.objects.latest_for_users(), many=True).data)


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
