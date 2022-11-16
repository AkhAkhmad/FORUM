from rest_framework import serializers
from api.models import Checkbox


class CheckboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = '__all__'


class DataSerializer(serializers.Serializer):
    # title = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    # attr = serializers.JSONField(required=False)
    # type = serializers.CharField()
    val_1 = serializers.IntegerField()
    val_2 = serializers.IntegerField()

    @staticmethod
    def validated_type(type):
        if not type in ['dict', 'list', 'tuple']:
            raise serializers.ValidationError(f'{type} is  not allowed')
        return type
