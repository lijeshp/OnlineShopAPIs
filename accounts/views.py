from django.shortcuts import render
from rest_framework.views import APIView
from .  serializer import RegisterSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):

    def post (self,request):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["response"]="User created" 
            data["username"]=account.username
            data["email"]=account.email
            token,create = Token.objects.get_or_create(user=account)
            data["token"]=token.key
        else:
            data=serializer.errors
        return Response(data)


class WelcomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'user':str(request.user),'userid':str(request.user.id)

        }
        return Response(content)


   