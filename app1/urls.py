from django.urls import path
from .views import RegisterView, SendOtp, VerifyOtpView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('send-otp/', SendOtp.as_view(), name="send-otp"),
    path('verify-otp/', VerifyOtpView.as_view(), name="send-otp"),
]