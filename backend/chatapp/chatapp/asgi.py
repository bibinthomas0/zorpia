import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import routing
from api.consumers import ChatConsumer
from django.urls import re_path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r"ws/chat/(?P<room_name>[\w\d]+)/(?P<username>[\w\d]+)/$", ChatConsumer.as_asgi()),
            ]
        )
    ),
})