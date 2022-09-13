from django.urls import path
from .views import PasswordChangeAPI

urlpatterns = [
    path('password-change/<pk>/', PasswordChangeAPI.as_view()),
]
