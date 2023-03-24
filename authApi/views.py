from django.shortcuts import render
from rest_framework import viewsets, permissions
from authApi.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils.hash import hash,verify 
import re
# Create your views here.


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        password=request.data['password']
        username=request.data['username']
        email=request.data['email']
        dumb_password=password
        request.data['password']=str(hash(password))
        if serializer.is_valid():
            if User.objects.filter(username=username).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif not re.match(r'[A-Za-z0-9]+', username):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif not re.match(r'[A-Za-z0-9@#$%^&+=]', dumb_password):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer   

class UserDelete(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserUpdate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HealthCheck(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format='json'):
        return Response(status=status.HTTP_200_OK)
    
class Login(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        username=request.data['username']
        password=request.data['password']
        if User.objects.filter(username=username).exists():
            user=User.objects.get(username=username)
            pwd=user.password
            hashed=pwd[2:66]
            salt=pwd[70:80]
            pwd_ary=[hashed,salt]
            if verify(pwd_ary,password):
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
      