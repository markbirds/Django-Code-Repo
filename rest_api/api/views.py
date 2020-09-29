from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def usersList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def usersCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUser(request,id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request,id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteUser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)