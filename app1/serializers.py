from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import VerificationOtp
import datetime 
from django.utils import timezone
import math
import random
from django.core.mail import send_mail


def generate_otp():
    """generates random OTP"""
    digits = "0123456789"
    otp = ""
    for i in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        )


class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField()
    email = serializers.EmailField()

    
    def validate(self, attrs):
        email = attrs['email']
        otp = attrs['otp']
        current_datetime = timezone.now()

        try:
            ver = VerificationOtp.objects.filter(otp=otp, email=email).first()
        except Exception:
            raise ValidationError({"otp": "Invalid OTP"})
        
        if not ver or ver.otp != otp or ver.expires_at < current_datetime:
            raise ValidationError({"otp": "Invalid OTP"})
        return attrs


class VerificationOtpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = VerificationOtp
        fields = (
            'email', 
        )


    def create(self, validated_data):
        email=validated_data['email'],

        instance, _ = VerificationOtp.objects.update_or_create(
            email=validated_data['email'],
            defaults={
                "otp": generate_otp()
            }
        )

        current_datetime = timezone.now()
        instance.expires_at = current_datetime + datetime.timedelta(minutes=2)
        instance.save()

        send_mail(
            subject="Subject here",
            message=f"Your OTP is {instance.otp}",
            from_email="from@example.com",
            recipient_list=[email],
            fail_silently=False,
        )

        return instance