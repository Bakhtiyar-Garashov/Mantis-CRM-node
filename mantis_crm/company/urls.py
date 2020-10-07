from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import CompanyInfo, GeneralInfo,CompanyDetail


urlpatterns = [
    path('', CompanyInfo.as_view(), name="company information"),
    path('<int:id>/', CompanyDetail.as_view(), name="company details"),
    path('general', GeneralInfo.as_view(), name="company general"),
    
    #path('api/v1/company', include('mantis_crm.company.urls')),
    #path('api/v1/finance', include('mantis_crm.finance.urls'))
]
