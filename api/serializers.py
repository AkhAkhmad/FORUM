from rest_framework import serializers
from api.models import Checkbox


class CheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = '__all__'
