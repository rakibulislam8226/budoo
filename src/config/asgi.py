import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from threadio import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/status", consumers.StatusConsumer.as_asgi()),
                ]
            )
        ),
    }
)
