"""mantis_crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi


#SWAGGER schema
schema_view = get_schema_view(
      openapi.Info(
         title="Mantis CRM company API",
         default_version='v1',
         description="CRM company node of MANTIS core project",
         contact=openapi.Contact(email="bakhtiyar.garashov@ut.ee"),
         license=openapi.License(name="BSD License"),
      ),
      public=True,
   )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/company/', include('company.urls')),
    #path('api/v1/finance', include('finance.urls'))
]
