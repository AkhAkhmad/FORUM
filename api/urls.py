from django.urls import path, include
from rest_framework import routers
from api.views import CheckboxViewSet

router = routers.DefaultRouter()
router.register('checkbox', CheckboxViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
