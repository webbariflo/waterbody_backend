from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from django.utils import timezone
from datetime import timedelta
import json
from .models import Weather,Admin,User,Location
from rest_framework.parsers import JSONParser
from django.contrib.gis.geos import Point,GEOSGeometry
from django.contrib.gis.measure import D
from .serializers import LocationSerializer,AdminSerializer
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
import csv
import pandas as pd
# from rest_framework import generics
import googlemaps


    

  
@csrf_exempt
def weather(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        # data = request.POST
        city = jsondata.get('city','')
        base_url = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5de227dcd9d14b80bb39771618ef96d5")
        weather_data = base_url.json()
        print(weather_data)
        value = {
            'name' :weather_data['name'], 
             'temp':weather_data['main']['temp'],
             'feels':weather_data['main']['feels_like'],
             'temp_min':weather_data['main']['temp_min'],
             'temp_max':weather_data['main']['temp_max'],
             'pressure':weather_data['main']['pressure'],
             'humidity':weather_data['main']['humidity'],
             'main' : weather_data['weather'][0]['main'],
             'description' : weather_data['weather'][0]['description'],
             'icon' : weather_data['weather'][0]['icon'],
             'wind' : weather_data['wind']['speed'],
             'deg' : weather_data['wind']['deg']            
        }
        final_value = Weather(name = value['name'],temperature=value['temp'],feels_like=value['feels'],temp_min=value['temp_min'],temp_max=value['temp_max'],pressure=value['pressure'],humidity=value['humidity'],main=value['main'],description=value['description'],icon=value['icon'],wind_speed=value['wind'],wind_deg=value['deg'])
        final_value.save()
        
        
        return JsonResponse(weather_data,safe=False)
    return JsonResponse({"message":"You are successfully stored data"})
        
        
        
  
@csrf_exempt
def admin_page(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        user_name = jsondata.get('user_name')
        mobile_no = jsondata.get('mobile_no')
        address = jsondata.get('address')
        latitude = jsondata.get('latitude')
        longitude = jsondata.get('longitude')
        city = jsondata.get('city')

        try:
            # Create a Location object and set the name
            location = Admin(user_name=user_name,mobile_no=mobile_no,address=address,city=city)

            # Create a PointField (aera) using latitude and longitude
            location.area = f'POINT({longitude} {latitude})'

            location.save()

            return JsonResponse({'message': 'Location saved successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
@csrf_exempt      
def login(request):
    if request.method == 'POST':
       userdata=JSONParser().parse(request)
       user_name = userdata.get('user_name')
       mobile_no = userdata.get('mobile_no')
       
       try:
            admins = Admin.objects.filter(mobile_no = mobile_no , user_name = user_name)
            if admins.exists():
                response_data = {'message': 'message saved successfully','user_name': user_name, 'mobile_no': mobile_no}
                return JsonResponse(response_data)
            #   return JsonResponse({'message':'ok', user_name})
            else:
                return JsonResponse({'message':'An error occured'}, status=500)
       except Exception as e:
           print(e)
           return JsonResponse({'message':'ooo'})
            
        
    
  

# @csrf_exempt
# def user(request,user_id):
#     if request.method == 'GET':
#         # Assuming you want to retrieve user data based on user_id
#         # user_id = request.GET.get('user_id')
#         try:
#             user = User.objects.get(user_id=user_id)
#             print(user)
#             data = {
#                 'user_id': user_id,
#                 'user_name': user.user_name,
#             }
#             return JsonResponse(data)
#         except User.DoesNotExist:
#             return JsonResponse({'message': 'User not found'}, status=404)
#     else:
#         return JsonResponse({'message': 'Invalid request method'}, status=400)
@csrf_exempt
def user_pond_view(request,mobileno):
    if request.method == 'GET':
        result = Admin.objects.filter(mobile_no=mobileno)
        try:
            a = []
            for i in result:
                a.append(i.address)
            return JsonResponse({'message':a})
            
        except:
            return JsonResponse({'message':'not found'})

@csrf_exempt
def weather_ten_data(request,name):
    if request.method == 'GET':
        ten_days_ago = timezone.now() - timedelta(days=5)
        
        result = Weather.objects.filter(name=name, time__gte=ten_days_ago)
        try:
            a = []
            for i in result:
                a.append([i.temperature,i.feels_like,i.temp_min,i.temp_max])
            return JsonResponse({'message':a})
        except:
            return JsonResponse({'message':'not found'})         
        
@csrf_exempt
def weather_twenty_data(request,name):
    if request.method == 'GET':
        twenty_days_ago = timezone.now() - timedelta(days=20)
        
        result = Weather.objects.filter(name=name, time__gte=twenty_days_ago)
        try:
            a = []
            for i in result:
                a.append([i.temperature,i.feels_like,i.temp_min,i.temp_max])
            return JsonResponse({'message':a})
        except:
            return JsonResponse({'message':'not found'})   
        
@csrf_exempt
def weather_thirty_data(request,name):
    if request.method == 'GET':
        thirty_days_ago = timezone.now() - timedelta(days=20)
        
        result = Weather.objects.filter(name=name, time__gte=thirty_days_ago)
        try:
            a = []
            for i in result:
                a.append([i.temperature,i.feels_like,i.temp_min,i.temp_max])
            return JsonResponse({'message':a})
        except:
            return JsonResponse({'message':'not found'})  
        
@csrf_exempt
def weather_data_range(request,name):
    if request.method == 'GET':
        req = JSONParser().parse(request)
        start_date = req.get('start_date')
        end_date = req.get('end_date')
        
        try:
            result = Weather.objects.filter(name=name, time__range=(start_date, end_date))
            if result.exists():
                data_list = [[entry.temperature, entry.feels_like, entry.temp_min, entry.temp_max] for entry in result]
                return JsonResponse({'message': data_list})
            else:
                return JsonResponse({'message':'No data found'})
        except Exception as e:
            return JsonResponse(e ,safe=False)
        
# @csrf_exempt
# def download(request,name):
#     if request.method ==  'GET':
#         ten_days_ago = timezone.now() - timedelta(days=5)
#         result = Weather.objects.filter(name=name, time__gte=ten_days_ago)
#         try:
#             data = []
#             for i in result:
#                 data.append([i.temperature,i.feels_like,i.temp_min,i.temp_max])
#             # return JsonResponse({'message':data})
#             response = HttpResponse(content_type='text/csv')
#             response['Content-Disposition'] = f'attachment; filename="{name}_weather_data.csv"'
#             writer = csv.writer(response)
#             writer.writerow(['Temperature','Feels Like','Min Temprature','Max Temprature'])
#             writer.writerows(data)
#             return response
#         except:
#             return JsonResponse({'message':'not found'})


@csrf_exempt
def download(request, name):
    if request.method == 'GET':
        ten_days_ago = timezone.now() - timedelta(days=5)
        result = Weather.objects.filter(name=name, time__gte=ten_days_ago)
        try:
            data = []
            for entry in result:
                data.append([entry.temperature   , entry.feels_like   , entry.temp_min    , entry.temp_max])

            # Create a DataFrame from the data
            df = pd.DataFrame(data, columns=['Temperature', 'Feels Like', 'Min Temperature', 'Max Temperature'])

            # Create a response object with the appropriate content type for CSV
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{name}_weather_data.csv"'

            # Use pandas to_csv method to write the DataFrame to the response
            df.to_csv('tapas.csv', index=False)


            return JsonResponse({'message':'successfully saved'})
        except:
            return JsonResponse({'message': 'not found'})



# @csrf_exempt
# def user_pond_map(request, mobileno):
#     if request.method == 'GET':
#         result = Admin.objects.filter(mobile_no=mobileno)
#         try:
#             coordinates = []

#             for admin_instance in result:
#                 area = GEOSGeometry(admin_instance.area)
#                 coordinates.append({'x': area.x, 'y': area.y, 'city': admin_instance.city})

#             return JsonResponse(coordinates, safe=False)

#         except:
#             return JsonResponse({'message': 'not found'})

@csrf_exempt
def user_pond_map(request, mobileno):
    if request.method == 'GET':
        result = Admin.objects.filter(mobile_no=mobileno)
        try:
            coordinates = []

            for i in result:
                area = GEOSGeometry(i.area)
                coordinates.append([area.x, area.y])

            return JsonResponse({'message': coordinates})

        except:
            return JsonResponse({'message': 'not found'})
       
        
# @csrf_exempt
# def user_pond_map(request,mobileno):
#     if request.method == 'GET':
#         result = Admin.objects.filter(mobile_no=mobileno)
#         try:
#             a = []
#             for i in result: 
#                 area = GEOSGeometry(i.area)
#                 area_json = {
#                     # 'type':'Point',
#                     'coordinates':[area.x,area.y]
#                 }
#                 a.append(area_json)
#             return JsonResponse({'message':a})
            
#         except:
#             return JsonResponse({'message':'not found'})

# @csrf_exempt
# def user_pond_map(request, mobileno):
#     if request.method == 'GET':
#         result = Admin.objects.filter(mobile_no=mobileno)
#         try:
#             coordinates = []

#             for i in result:
#                 area = GEOSGeometry(i.area)
#                 coordinates.extend([area.x, area.y])

#             return JsonResponse({'message': coordinates})

#         except:
#             return JsonResponse({'message': 'not found'})
        
        
@csrf_exempt
def user(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        user_name = jsondata.get('user_name')
        mobile_no = jsondata.get('mobile_no')
        user = User(user_name=user_name,mobile_no=mobile_no)
        user.save()
        return JsonResponse({'message': 'user saved successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)  


@csrf_exempt
def fetch_area(request):
    if request.method == 'POST':
        jsondata = JSONParser().parse(request)
        name = jsondata.get('name')
        latitude = jsondata.get('latitude')
        longitude = jsondata.get('longitude')
        city = jsondata.get('city')

        try:
            # Create a Location object and set the name
            location = Location(name=name,city=city)

            # Create a PointField (aera) using latitude and longitude
            location.area = f'POINT({longitude} {latitude})'
            

            location.save()

            return JsonResponse({'message': 'Location saved successfully.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# @csrf_exempt
# def fetch_area(request):
#     if request.method == 'POST':
#         jsondata = JSONParser().parse(request)
#         name = jsondata.get('name')
#         latitude = jsondata.get('latitude')
#         longitude = jsondata.get('longitude')
        
#         gmaps = googlemaps.Client(key='AIzaSyC-d-7RR_MQ45QLQXKSzOxviR2l11kN3wk')
        
#         reverse_geocode = gmaps.reverse_geocode((latitude, longitude))
#         if reverse_geocode:
#             address = reverse_geocode[0]['formatted_address']
#             area = Point(float(latitude),float(longitude), srid=4326)
#             print(jsondata)
#             res = Location(name=name,area=area,address=address)
#             res.save()

#             return JsonResponse({'message': 'Location saved successfully'})
#         else:
#             return JsonResponse({'message': 'Failed to convert coordinates to address'}, status=400)
#     else:
#         return JsonResponse({'message': 'Invalid request method'}, status=400)  

# @csrf_exempt
# def fetch_area(request):
#     if request.method == 'POST':
#         jsondata = JSONParser().parse(request)
#         name = jsondata.get('name')
#         latitude = jsondata.get('latitude')
#         longitude = jsondata.get('longitude')
#         point = Point(float(latitude),float(longitude), srid=4326)
#         print(jsondata)
#         area = Location(name=name,area=point)
#         area.save()

#         return JsonResponse({'message': 'Location saved successfully'})
#     else:
#         return JsonResponse({'message': 'Invalid request method'}, status=400)  


# @csrf_exempt
# def fetch_area(request):
#     if request.method == 'POST':
#         jsondata = JSONParser().parse(request)
#         name = jsondata.get('name')
#         latitude = jsondata.get('latitude')
#         print(latitude)
#         longitude = jsondata.get('longitude')
#         print(longitude)
#         print(jsondata)
#         location = Location(name=name,latitude=latitude,longitude=longitude)
#         location.save()

#         return JsonResponse({'message': 'Location saved successfully'})
#     else:
#         return JsonResponse({'message': 'Invalid request method'}, status=400)  


    
    
# @csrf_exempt                      #this is for send longitude & latitude from backend 
# def fetch_area(request, area):
#     if request.method == "GET":
#         url = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={area}&key=AIzaSyC-d-7RR_MQ45QLQXKSzOxviR2l11kN3wk')
        
#         response = url.json()
#         print(response)

#         name = response['results'][0]['address_components'][0]['long_name']
#         latitude =  response['results'][0]['geometry']['location']['lat']
#         longitude = response['results'][0]['geometry']['location']['lng']
#         data_saved = Location(name=name,latitude=latitude,longitude=longitude)
#         data_saved.save()
#         return JsonResponse({"message":"data saved"},status=500)
# @csrf_exempt   
# def fetch_area(request, area):
#     if request.method == "GET":
#         url = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={area}&key=AIzaSyC-d-7RR_MQ45QLQXKSzOxviR2l11kN3wk')
        
#         response = url.json()
#         print(response) 
#         return JsonResponse({'message': response}, status=500)

    
    
    
    
    
    
    
          # Get the HTTP status code

        # if status_code == 200:
        #     data = response.json()
        #     # Process data or save it to the database if needed
        #     return JsonResponse(data)
        # else:
        #     print(f"Request failed with status code: {status_code}")
        #     return JsonResponse({'error': 'Failed to fetch location data.'}, status=500)
    
# @csrf_exempt
# def area(request):
#     if request.method == "GET":
#         query_point = Point(-122.123456, 37.654321)
#         results = Area.objects.filter(location__distance_lte=(query_point, D(m=1000)))

#     return render(request, 'map_search_results.html', {'results': results})
# @csrf_exempt
# def fetch_area(request,area):
#     # api_key = 'AIzaSyC-d-7RR_MQ45QLQXKSzOxviR2l11kN3wk'
#     url = 'https://maps.googleapis.com/maps/api/json?address=India&key=AIzaSyC-d-7RR_MQ45QLQXKSzOxviR2l11kN3wk'

#     response = requests.get(url)
#     data = response.json()
#     print(data)

    # if response.status_code == 200:
    #     return JsonResponse(data)
    #     # Extract and save location data to the database
    #     latitude = data['results'][0]['geometry']['location']['lat']
    #     longitude = data['results'][0]['geometry']['location']['lng']

    #     location = Location(latitude=latitude, longitude=longitude)
    #     location.save()

    # #     return JsonResponse({'message': 'Location data saved successfully.'})
    # else:
        # return JsonResponse({'message': response}, status=500)