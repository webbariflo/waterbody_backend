from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/',views.weather,name='weather'),
    # path('user/<user_id>/',views.user,name='user'),
    path('user/',views.user,name='user'),
    path('fetch_area/',views.fetch_area),
    path('admin_page/',views.admin_page),
    path('user_pond_view/<mobileno>/',views.user_pond_view),
    path('user_pond_map/<mobileno>/',views.user_pond_map),
    path('weather_ten_data/<name>/',views.weather_ten_data),
    path('weather_twenty_data/<name>/',views.weather_twenty_data),
    path('weather_thirty_data/<name>/',views.weather_thirty_data),
    path('weather_data_range/<name>/',views.weather_data_range),
    path('login/',views.login,name='login'),
    path('download/<name>/',views.download),
]
