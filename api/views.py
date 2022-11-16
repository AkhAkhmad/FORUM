from api.models import Checkbox
from api.serializers import CheckboxSerializer, DataSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class CheckboxList(generics.ListCreateAPIView):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer


class CheckboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer


class DataView(APIView):
    def get(self, reg):
        serializer = DataSerializer(data=reg.query_params)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data
        val_1 = params.get('val_2')
        val_2 = params.get('val_2')
        result = val_1 + val_2
        Response(result)
