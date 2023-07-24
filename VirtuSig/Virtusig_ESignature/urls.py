"""Virtusig_ESignature URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from django.conf.urls import include

# import swagger_service
import Virtusig_ESignature.swagger_service as swagger_service

urlpatterns = [

    # path('admin/', admin.site.urls),
    path('Virtusig_Esignature/docs/', swagger_service.schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('virtusig_app/', include('virtusig_app.urls')),

]
