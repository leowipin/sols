from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from users.serializers import LoginSerializer, GroupSerializer, SignUpSerializer
from rest_framework import status

class LoginView(APIView):
    permission_classes = AllowAny

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({"token": user.auth_token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#This class should be in other app
class GroupView(APIView):
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            role = serializer.save()
            role.permissions.set(serializer.validated_data['permissions'])
            return Response({'message': 'Group created successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignUpView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data, context={'group_name': request.data.get('group')})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Sign up succesfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
