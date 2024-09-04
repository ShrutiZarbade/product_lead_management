from rest_framework.viewsets import ModelViewSet
from .models import ProductManagement,LeadManagement,ProductLead
from .serializers import ProductSerializer,LeadSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
from django.utils.dateparse import parse_datetime

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


class GetDataThroughDate(ModelViewSet):

    def list(self, request, *args, **kwargs):

        start_date_str = request.GET.get("start_date")
        end_date_str = request.GET.get("end_date")

        start_date = parse_datetime(start_date_str) if start_date_str else None
        end_date = parse_datetime(end_date_str) if end_date_str else None

        leads = LeadManagement.objects.filter(created_at__range=[start_date, end_date])
        data = []
        for lead in leads:
            dict_data = {
                "name":lead.name,
                "email":lead.email,
                "created_at":lead.created_at

            }
            data.append(dict_data)

        return Response(data, status=status.HTTP_200_OK)

class GetTopMostLead(ModelViewSet):

    def list(self, request, *args, **kwargs):
        lead_product_data = ProductLead.objects.values('product_id').annotate(interested_leads=Count('product_id')).order_by('-interested_leads')[:10]
        data = []
        for lead_data in lead_product_data:
            dict_data = {
                "name":ProductManagement.objects.get(id = lead_data.get("product_id")).name,
                "interested_leads" : lead_data.get("interested_leads")
            }
            data.append(dict_data)
        return Response(data, status=status.HTTP_200_OK)

class GetBottomMostLead(ModelViewSet):

    def list(self,request, *args, **kwargs):
        lead_product_data = ProductLead.objects.values('product_id').annotate(interested_leads=Count('product_id')).order_by('-interested_leads')
        data = []
        for lead_data in lead_product_data[-10:]:
            dict_data = {
                "name":ProductManagement.objects.get(id = lead_data.get("product_id")).name,
                "interested_leads" : lead_data.get("interested_leads")
            }
            data.append(dict_data)
        return Response(data, status=status.HTTP_200_OK)
