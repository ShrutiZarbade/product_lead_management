from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,LeadViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'leads',LeadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
