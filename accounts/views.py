from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NormalUserRegistrationSerializer, OtherUserRegistrationSerializer

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
