from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import RegisterSerializer, VerificationOtpSerializer, VerifyOtpSerializer
from django.contrib.auth.models import User
from .models import VerificationOtp
from rest_framework import permissions
from rest_framework.response import Response


"""
Steps:
1. Run send otp to send the otp to the given email.
    OTP will be printed in terminal as the console backend is used for the emails.

2. Run Verify otp by providing the OTP and the email on which the OTP is sent.

3. When verify otp API runs successfully then only call the Register API.
"""


class SendOtp(CreateAPIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = VerificationOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class VerifyOtpView(CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        verify_serializer = VerifyOtpSerializer(data=request.data)
        verify_serializer.is_valid(raise_exception=True)
        return Response(data="OK", status=200)


class RegisterView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

