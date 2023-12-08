from rest_framework import serializers
from .models import Weather,Location,User,Admin
from rest_framework_gis.serializers import GeoFeatureModelSerializer 
# from .models import YourGeoSpatialModel

class weatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
        
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Location
        geo_field = "area"
        # id_field = False
        fields = '__all__'
        
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['user_name','mobile_no']