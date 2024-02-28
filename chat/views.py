from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .tokenauthentication import *

# Create your views here.

class UserRegistration(APIView):
    def post(self, request):
        
        serializer = UserSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class Login(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            token=JWTAuthentication.generate_token(payload=serializer.data)
            return Response({"mssg":"login successful",'token':token,'user':serializer.data},status=status.HTTP_201_CREATED)
        
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
            