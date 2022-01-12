from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DpawRegionSerializer
from .models import DpawRegion


class DpawRegionViewSet(viewsets.ModelViewSet):
    queryset = DpawRegion.objects.all()
    serializer_class = DpawRegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [] #disables authentication
    #permission_classes = [] #disables permission
