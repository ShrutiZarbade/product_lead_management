from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,LeadViewSet,GetDataThroughDate,GetTopMostLead,GetBottomMostLead,GetNumberProductByLead

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'leads',LeadViewSet)
router.register(r'get_leads_between_dates',GetDataThroughDate,basename='Leads between two dates')
router.register(r'get_top_10_leads',GetTopMostLead,basename='Top 10 leads')
router.register(r'get_bottom_10_leads',GetBottomMostLead,basename='Bottom 10 leads')
router.register(r"get_product_by_lead",GetNumberProductByLead,basename="get product by leads")

urlpatterns = [
    path('', include(router.urls)),
]
