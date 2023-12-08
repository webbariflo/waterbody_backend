import json
from channels import generic
import asyncio
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
import requests
from channels.db import database_sync_to_async
from myapp. models import Weather
from django.utils import timezone

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         while True:
#             data = await self.receive()
#             await self.send(json.dumps(data))
            
#             await asyncio.sleep(5)
#     @sync_to_async
#     def receive(self):
# #         return 'HELLO'

# #     @sync_to_async
# #     def disconnect(self, close_code):
# #         pass
class WeatherConsumer(AsyncWebsocketConsumer):
    # A set to keep track of cities for which data has been fetched
    fetched_cities = set()

    async def connect(self):
        self.city = self.scope['url_route']['kwargs']['city']
        
        # Check if data for this city has already been fetched
        if self.city not in self.fetched_cities:
            await self.accept()
            self.fetched_cities.add(self.city)
            while True:
                await self.update_weather_data()
                await asyncio.sleep(10)
        else:
            await self.close()

    @database_sync_to_async
    def update_weather_data(self):
        api_key = "5de227dcd9d14b80bb39771618ef96d5"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}"

        response = requests.get(url)
        data = response.json()

        Weather.objects.create(
            name=data['name'],
            temperature=data['main']['temp'],
            feels_like=data['main']['feels_like'],
            temp_min=data['main']['temp_min'],
            temp_max=data['main']['temp_max'],
            pressure=data['main']['pressure'],
            humidity=data['main']['humidity'],
            main=data['weather'][0]['main'],
            description=data['weather'][0]['description'],
            icon=data['weather'][0]['icon'],
            wind_speed=data['wind']['speed'],
            wind_deg=data['wind']['deg'],
            time=timezone.now() 
        )



                    
# class WeatherConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.city = self.scope['url_route']['kwargs']['city']
#         await self.accept()

#         while True:
#             await self.update_weather_data()
#             await asyncio.sleep(10)
#             # await asyncio.sleep(3600)
    
    # @database_sync_to_async
    # def update_weather_data(self):
    #     api_key = "5de227dcd9d14b80bb39771618ef96d5"
    #     url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}"

    #     response = requests.get(url)
    #     data = response.json()

    #     weather_name = data['name']

    #     # Check if a record with the same name already exists
    #     existing_weather = Weather.objects.filter(name=weather_name).first()

    #     if not existing_weather:
    #         # If the record does not exist, create a new one
    #         Weather.objects.create(
    #             name=weather_name,
    #             temperature=data['main']['temp'],
    #             feels_like=data['main']['feels_like'],
    #             temp_min=data['main']['temp_min'],
    #             temp_max=data['main']['temp_max'],
    #             pressure=data['main']['pressure'],
    #             humidity=data['main']['humidity'],
    #             main=data['weather'][0]['main'],
    #             description=data['weather'][0]['description'],
    #             icon=data['weather'][0]['icon'],
    #             wind_speed=data['wind']['speed'],
    #             wind_deg=data['wind']['deg'],
    #             time=timezone.now() 
    #         )
# class WeatherConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.city = self.scope['url_route']['kwargs']['city']
#         await self.accept()

#         while True:
#             await self.update_weather_data()
#             await asyncio.sleep(10)
#             # await asyncio.sleep(3600)

#     @database_sync_to_async
#     def update_weather_data(self):
#         api_key = "5de227dcd9d14b80bb39771618ef96d5"
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}"

#         response = requests.get(url)
#         data = response.json()

#         Weather.objects.create(
#             name=data['name'],
#             temperature=data['main']['temp'],
#             feels_like=data['main']['feels_like'],
#             temp_min=data['main']['temp_min'],
#             temp_max=data['main']['temp_max'],
#             pressure=data['main']['pressure'],
#             humidity=data['main']['humidity'],
#             main=data['weather'][0]['main'],
#             description=data['weather'][0]['description'],
#             icon=data['weather'][0]['icon'],
#             wind_speed=data['wind']['speed'],
#             wind_deg=data['wind']['deg'],
#             time=timezone.now() 
#         )

            
# class WeatherConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.city = self.scope['url_route']['kwargs']['city'] 
#         await self.accept()
  
#         while True:
#             await self.update_weather_data()
#             await asyncio.sleep(10)
#     @database_sync_to_async
#     def update_weather_data(self):
            
#             api_key = "5de227dcd9d14b80bb39771618ef96d5"
#             url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}"

#             response = requests.get(url)
#             data = response.json()
            
            
#             Weather.objects.create(
#                 name = data['name'], 
#                 temperature = data['main']['temp'],
#                 feels_like = data['main']['feels_like'],
#                 temp_min = data['main']['temp_min'],
#                 temp_max = data['main']['temp_max'],
#                 pressure = data['main']['pressure'],
#                 humidity = data['main']['humidity'],
#                 main = data['weather'][0]['main'],
#                 description= data['weather'][0]['description'],
#                 icon = data['weather'][0]['icon'],
#                 wind_speed = data['wind']['speed'],
#                 wind_deg = data['wind']['deg']
#             )
#             success_message = {
#                 'type': 'success',
#                 'message': f'successfully update data {self.city}'
#             }
#             await self.send(text_data=json.dumps(success_message))
            



# class WeatherConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.city = self.scope['url_route']['kwargs']['city'] 
#         await self.accept()
  
#         while True:
#             api_key = "5de227dcd9d14b80bb39771618ef96d5"
#             url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}"

#             response = requests.get(url)
#             data = response.json()
                        
#             await self.send(text_data=json.dumps({
#                 'name' :data['name'], 
#                 'temperature': data['main']['temp'],
#                 'humidity': data['main']['humidity'],
#                 'feels': data['main']['feels_like'],
#                 'description': data['weather'][0]['description'],
#             }))
            
#             await asyncio.sleep(10)

            

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#         # Connect to OpenWeatherMap API and send updates to clients
#         while True:
#             # Replace {city} with the desired city name
#             city = "Bhubaneswar"
#             api_key = "5de227dcd9d14b80bb39771618ef96d5"
#             url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

#             response = requests.get(url)
#             data = response.json()

#             # Send weather data to the client
#             await self.send(text_data=json.dumps({
#                 'name' :data['name'], 
#                 'temperature': data['main']['temp'],
#                 'humidity': data['main']['humidity'],
#                 'feels': data['main']['feels_like'],
#                 'description': data['weather'][0]['description'],
#             }))

#             # Sleep for some time before fetching updates again
#             await asyncio.sleep(60)  # Sleep for 5 minutes (adjust as needed)

        
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         self.send(text_data=json.dumps({"message": message}))




