from django.urls import path
from .views import ConversationAPIView

urlpatterns = [
    path("conversation/", ConversationAPIView.as_view(), name="conversation"),
]
