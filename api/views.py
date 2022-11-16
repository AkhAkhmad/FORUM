from api.models import Checkbox
from api.serializers import CheckboxSerializer
from rest_framework import generics


class CheckboxList(generics.ListCreateAPIView):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer


class CheckboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializer
