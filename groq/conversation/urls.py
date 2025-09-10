from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ConversationAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("conversation/", ConversationAPIView.as_view(), name="conversation"),
]
