from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="user-register"),
    path("adminregister/", views.AdminRegisterView.as_view(), name="admin-register"),
    path("login/", views.LoginView.as_view(), name="user-login"),
    path("otp/", views.OtpRequestView.as_view(), name="user-otp"),
    path("username/", views.UsernameValidation.as_view(), name="username"),
    path("googlelogin/", views.GoogleLogin.as_view(), name="googlelogin"),
    path("listusers/", views.AdminUserListCreateView.as_view(), name="listusers"),
    path("forgotpassword/", views.ForgotPassword.as_view(), name="forgotpassword"),
    path("otpvalidation/", views.OtpValidation.as_view(), name="otpvalidation"),
    path("changepassword/", views.ChangePasswordView.as_view(), name="changepassword"),
    path("isblocked/", views.BlockVerification.as_view(), name="isblocked"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]