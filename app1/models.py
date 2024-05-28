from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class VerificationOtp(models.Model):
    otp = models.CharField(max_length=6, unique=True, null=False, blank=False)
    expires_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
