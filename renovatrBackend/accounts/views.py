from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import (
	AllowAny
)
 
from accounts.serializers import (User_Creation_Serializer, User_Serializer)

User = get_user_model()

class User_Creation_View(CreateAPIView):
    queryset=User.objects.all()
    serializer_class = User_Creation_Serializer
    permission_classes = [AllowAny]

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': User_Serializer(user, context={'request': request}).data
    }
    print("hello")



