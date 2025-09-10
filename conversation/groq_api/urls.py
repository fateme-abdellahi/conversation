from django.urls import path
from .views import ConversationAPIView

urlpatterns = [
    path("", ConversationAPIView.as_view(), name="conversation"),
]
