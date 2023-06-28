from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import UserSerializer,RegisterSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    def get_queryset(self):
        queryset = User.objects.all()
        username =self.request.query_params.get('username',None)
        if username is not None:
            queryset=User.objects.filter(username=username)
        return queryset

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RegisterSerializer