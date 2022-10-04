from django.urls import path
from .views import PasswordChangeAPI, Profile

urlpatterns = [
    path('profile/', Profile.as_view()),
    path('password-change/<pk>/', PasswordChangeAPI.as_view()),
]
