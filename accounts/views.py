from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from .serializers import NormalUserRegistrationSerializer, OtherUserRegistrationSerializer,UserProfileSerializer,CustomUserSerializer
from .models import UserProfile

# <------------------sign up ------------------------->

@api_view(['POST'])
def normal_user_signup(request):
    if request.method == 'POST':
        serializer = NormalUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def other_user_signup(request):
    if request.method == 'POST':
        serializer = OtherUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# <-------------------------------User_Profile--------------------------------------------------------->

class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        return user_profile
    
    def perform_update(self, serializer):
        serializer.save()  # Save the updated profile

class UserProfileDetailView(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user