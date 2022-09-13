from django.urls import path
from .views import PasswordChangeAPI

urlpatterns = [
    path('change-password', PasswordChangeAPI.as_view()),
]
