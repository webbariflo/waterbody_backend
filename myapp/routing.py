from django.urls import re_path
from myapp.consumers import WeatherConsumer
from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/$', ChatConsumer.as_asgi()),
    re_path(r'ws/(?P<city>\w+)/$', WeatherConsumer.as_asgi()),
    # re_path(r'ws/(?P<city>\w+)/$', WeatherviewConsumer.as_asgi()),
]
