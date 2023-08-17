from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, status, response, generics
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset
    
        
