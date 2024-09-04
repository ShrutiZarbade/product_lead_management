from rest_framework.viewsets import ModelViewSet
from .models import ProductManagement,LeadManagement,ProductLead
from .serializers import ProductSerializer,LeadSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class ProductViewSet(ModelViewSet):
    queryset = ProductManagement.objects.all()
    serializer_class = ProductSerializer


class LeadViewSet(ModelViewSet):
    queryset = LeadManagement.objects.all()
    serializer_class = LeadSerializer

    def create(self,request,*args):
        lead_data = request.data        
        leadmanage_data = LeadManagement.objects.create(name=lead_data.get("name"),
                            email = lead_data.get("email"),phone_number= lead_data.get("phone_number"))
        leadmanage_data.save()
        product_id = ProductManagement.objects.get(name = lead_data.get("product_name")).id
        
        product_lead = ProductLead.objects.create(product_id=product_id,lead_id=leadmanage_data.id)
        product_lead.save()

        return Response({"success":"Lead has generated successfully"}, status=status.HTTP_201_CREATED)

