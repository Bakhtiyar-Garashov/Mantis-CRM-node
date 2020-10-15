from django.db.models import fields
from rest_framework import serializers
from .models import Company, General, Code, Type, Contact, Notes


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class GeneralSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = General
        fields = '__all__'
