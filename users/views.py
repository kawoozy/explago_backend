from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from users.models import Users
from users.serializers import UsersSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def users_list(request):
    user_list = Users.objects.all()
        
    username = request.GET.get('username', None)
    
    if username is not None:
        user_list = user_list.filter(username__icontains=username)
        
    users_serializer = UsersSerializer(user_list, many=True)
    return JsonResponse(users_serializer.data, safe=False)