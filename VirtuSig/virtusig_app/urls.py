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

from django.urls import path, include
from virtusig_app.service import testing_service, Login_service

urlpatterns = [

    ################  test #######################
    path('test/', include([
        path('', include([

            path('test/', testing_service.Testing_list.as_view()),
            path('login_user/', Login_service.LoginReg.as_view()),
            path('envelop/', Login_service.EnvelopData.as_view()),
            path('login/', Login_service.Login_user.as_view()),
            path('reset_password/', Login_service.Validate_Forget_Password.as_view()),
            path('login_prod/', Login_service.LoginReg1.as_view()),
            path('logout/', Login_service.LogoutAllView.as_view()),

        ]))
    ]), ),



]
