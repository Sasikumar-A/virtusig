import logging

from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework.response import Response

from virtusig_app import serializer


class Testing_list(GenericAPIView):
    serializer_class = serializer.TestSerializer
    def get(self,request):
        data = {"test" : "test"}
        return Response(data)