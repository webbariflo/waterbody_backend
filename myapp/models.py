from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models 
from django.contrib.gis.geos import Point
from django.contrib.gis.admin.widgets import OpenLayersWidget
# Create your models here.


class Weather(models.Model):
    name = models.CharField(max_length=100,blank=True)
    temperature = models.FloatField(blank=True)
    feels_like = models.FloatField(blank=True)
    temp_min = models.FloatField(blank=True)
    temp_max = models.FloatField(blank=True)
    pressure = models.IntegerField(blank=True)
    humidity = models.IntegerField(blank=True)
    main = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=100,blank=True)
    icon = models.CharField(max_length=10,blank=True)
    wind_speed = models.FloatField(blank=True)
    wind_deg = models.IntegerField(blank=True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    
class Admin(models.Model):
    user_name = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()
    address = models.CharField(max_length=100,blank=True)
    area = models.PointField(geography=True)
    city = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return str(self.mobile_no)
    
class User(models.Model):
    user_name = models.CharField(max_length=50) 
    mobile_no = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return str(self.mobile_no)
    
class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True)
    area = models.PointField(geography=True)
    city = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.name
    
# class Location(models.Model):
#     name = models.CharField(max_length=100,blank=True)
#     area = models.PointField(geography=True)
#     address = models.CharField(max_length=255, blank=True)
    
    # area.widget = OpenLayersWidget(
    #     attrs={
    #         'default_lon': 78.9629,  # Longitude of the center (India)
    #         'default_lat': 20.5937,  # Latitude of the center (India)
    #         'default_zoom': 5,      # Default zoom level
    #     }
    # )
     

     
# class Location(models.Model):
#     name = models.CharField(max_length=100,blank=True)
#     area = models.PointField(geography=True,srid=4326)
#     address = models.CharField(max_length=255, blank=True)
     
    
    #  def __str__(self):
    #     return self.city