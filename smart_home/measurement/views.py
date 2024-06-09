# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SensorDetailSerializer
        return SensorSerializer

class MeasurementViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer