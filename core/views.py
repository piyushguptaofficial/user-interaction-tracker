from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .serializers import RegisterSerializer
from .tasks import send_welcome_email

# Create your views here.

class PublicView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({'message': 'This is a public endpoint'}, status = 200)
    
class DashboardView(APIView):
    permission_class = [IsAuthenticated]
        
    def get(self, request):
        return Response({'message':f'welcome {request.user.username}! This is a protected dashboard.'})
        
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Trigger the background task
            send_welcome_email.delay(user.username, user.email)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    