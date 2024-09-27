from django.urls import path
from .consumers import ChatConsumer,NotificationConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
    path("ws/notifications/<str:username>/", NotificationConsumer.as_asgi()),
]