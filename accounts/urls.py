from django.urls import path
from .views import PasswordChangeAPI, Profile, ProfileUpdateAPIView

urlpatterns = [
    path('profile/', Profile.as_view()),
    path('profile/<pk>/', ProfileUpdateAPIView.as_view()),
    path('password-change/<pk>/', PasswordChangeAPI.as_view()),
]
