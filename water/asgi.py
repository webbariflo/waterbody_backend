import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from myapp import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
# django_asgi_app = get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application,
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             routing.websocket_urlpatterns
#         )),
# })

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
         URLRouter(
             routing.websocket_urlpatterns
         )),
        # Just HTTP for now. (We can add other protocols later.)
    }
)

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': URLRouter(
#             myapp.routing.websocket_urlpatterns
#         )
# })