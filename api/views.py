from api.models import Checkbox
from api.serializers import CheckboxSerializer, DataSerializer
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response


class CheckboxList(generics.ListCreateAPIView):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer

    @action(detail=FutureWarning, methods=['get'])
    def limit(self, reg, pk=None):
        params = reg.query_params
        return Response({'result': params})


class CheckboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer


class DataView(APIView):
    def get(self, reg):
        serializer = DataSerializer(data=reg.query_params)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data
        val_1 = params.get('val_1')
        val_2 = params.get('val_2')
        result = val_1 + val_2
        return Response(result)
