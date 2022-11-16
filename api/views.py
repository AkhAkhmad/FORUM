from api.models import Checkbox
from api.serializers import CheckboxSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class CheckboxList(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, reg, format=None):
        checkboxes = Checkbox.objects.all()
        serializer = CheckboxSerializer(checkboxes, many=True)
        return Response(serializer.data)

    def post(self, reg, format=None):
        serializer = CheckboxSerializer(data=reg.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CheckboxDetail(APIView):
    permission_classes = [permissions.IsAdminUser]

    def put(self, reg, pk, format=None):
        try:
            checkbox = Checkbox.objects.get(pk=pk)
            serializer = CheckboxSerializer(data=reg.data)  # передаем данные
            if serializer.is_valid():
                serializer.save()
        except Checkbox.DoesNotExist:
            return Response({'error': f'Checkbox with id = {pk} is not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def delete(self, reg, pk, format=None):
        checkbox = Checkbox.objects.get(pk=pk)
        checkbox.delete()
        return Response(status == status.HTTP_204_NO_CONTENT)
