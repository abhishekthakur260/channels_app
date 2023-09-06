"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os

from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat_app.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')


application = get_asgi_application()

wss_patterns =[
    path('consumers/',ChatConsumer)
]

application = ProtocolTypeRouter(
    {
       "websocket": URLRouter(wss_patterns)
    }    
)
