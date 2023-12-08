from django.contrib.gis import admin
# Register your models here.
from  .models import Weather,User,Location,Admin

@admin.register(Weather)
class Weather(admin.ModelAdmin):
    list_display = ['name','temperature','feels_like','temp_min','temp_max','pressure','humidity','main','description','icon','wind_speed','wind_deg','time']
   
   
@admin.register(Admin)
class Admin(admin.GISModelAdmin):
    list_display = ['user_name','mobile_no','address','area','city']
 
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['user_name','mobile_no']

@admin.register(Location)
class Location(admin.GISModelAdmin):
    list_display = ['user','name','area','city']