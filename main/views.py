from rest_framework.views import APIView
from .serializers import *;
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


# Create your views here.
class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer._validated_data['password'])
            user.save()

            return Response({'message': "User registered successfully."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self,request):

        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username = username, password=password)
        if user is not None:
            return Response({
                "message": "Login succesful",
            }, status=status.HTTP_200_OK)
        
        else:
            return Response({
                "error": "Invalid username or password"
            }, status=status.HTTP_400_BAD_REQUEST)