from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import SignInSerializer, GroupSerializer, SignUpSerializer
from rest_framework import status
from django.contrib.auth.models import Permission
import jwt
from sols import settings
import datetime
from datetime import timedelta
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

JWT_SECRET_KEY = settings.JWT_SECRET_KEY
DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL

class SignInView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignInSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        payload = {
            "user_id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + timedelta(days=1),
        }
        permissions = Permission.objects.filter(user=user)
        payload['permissions'] = [p.codename for p in permissions]
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
        return Response({
            "token": token.decode("utf-8")
        }, status=status.HTTP_200_OK)

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
            context = {'user': serializer.validated_data}
            html_content = render_to_string('signupEmail.html', context)
            subject = 'Welcome to My Site!'
            from_email = DEFAULT_FROM_EMAIL
            to = [serializer.validated_data['email']]
            email = EmailMessage(subject, html_content, from_email, to)
            email.content_subtype = 'html'

            try:
                email.send()
                serializer.save()
            except Exception as e:
                print(e)
                return Response({'message': 'Error sending email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'message': 'Sign up successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
