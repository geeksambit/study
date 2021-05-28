from django.shortcuts import render

from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from materials import views
from materials.models import *
from materials.serializers import *

# Create your views here.


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    # def create(self, request):
    #     serializer_class = ClassSerializer
    #     # serializer = serializer_class(data=request.data, context={'request' : request})
    #     # serializer.is_valid(raise_exception=True)
    #     # serializer.save()

    #     return Response(
    #         {
    #             "data": serializer.data,
    #             "status" : "ok",
    #             "code" : 200,
    #             "message" : "Successfully created Product record",
    #         },
    #         status.HTTP_200_OK
    #     )