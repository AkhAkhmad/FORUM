from api.models import Checkbox
from api.serializers import CheckboxSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins


class CheckboxList(generics.ListCreateAPIView):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer


class CheckboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer

