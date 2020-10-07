from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Company, General, Code, Type, Contact, Notes
from .serializers import CompanySerializer, GeneralSerializer
# Create your views here.


class CompanyInfo(APIView):
    """
    GET or POST company information
    """

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetail(APIView):
    """
    GET PUT OR DELETE object based on id
    """

    def get_object(self, id):
        try:
            return Company.objects.get(pk=id)
        except Company.DoesNotExist:
            raise Http404


    def get(self, request,id):
        company = self.get_object(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)


    def put(self, request, id):
        obj = self.get_object(id)
        serializer = CompanySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        company=self.get_object(id)
        company.delete()
        return Response({"success":"object deleted"})

    
        


class GeneralInfo(APIView):
    """
    GET or POST general information of company
    """

    def get(self, request):
        general_info = General.objects.all()
        serializer = GeneralSerializer(general_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GeneralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
