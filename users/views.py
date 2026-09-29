from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import responses, Response

from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class MeView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "id" : user.id,
            "username" : user.username,
            "email" : user.email,
        })

