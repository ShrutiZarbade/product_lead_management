from rest_framework.viewsets import ModelViewSet
from .models import ProductManagement,LeadManagement
from .serializers import ProductSerializer,LeadSerializer
from rest_framework import generics

class ProductViewSet(ModelViewSet):
    queryset = ProductManagement.objects.all()
    serializer_class = ProductSerializer


class LeadViewSet(ModelViewSet):
    queryset = LeadManagement.objects.all()
    serializer_class = LeadSerializer

