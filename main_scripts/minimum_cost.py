import math
import json
from geopy.geocoders import Nominatim
from openrouteservice import convert
import requests

class MinimumCost:
    def __init__(self, address, power):
        self.address = address
        self.power = power

    @staticmethod
    def get_api_key():
        with open('keys.json','r') as f:
            x = json.load(f)
        return x['key']

    @staticmethod
    def a2c(address):
        """convert address to coordinates"""
        locator = Nominatim(user_agent="myUserAgent", timeout=5)
        location = locator.geocode(address)
        return (location.latitude, location.longitude)
    
    @staticmethod
    def c2a(coords):
        """convert coordinates to address"""
        #cords = (lat, lon)
        locator = Nominatim(user_agent="myUserAgent", timeout=5)
        location = locator.reverse(coords, exactly_one=True)
        return location.address

    @staticmethod
    def haversine(y1, x1, y2, x2):
        """haversine distance between two points"""
        R = 6371000
        y1, x1, y2, x2 = map(math.radians, [y1, x1, y2, x2])
        dlat = y2 - y1
        dlon = x2 - x1
        a = math.sin(dlat/2)**2 + math.cos(y1) * math.cos(y2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return R * c

    @staticmethod
    def get_route(start, end, profile='driving-car'):
        """find the shortest route between two points"""
        # api call 
        headers = {
            'Authorization': MinimumCost.get_api_key(),
            'Content-Type': 'application/json'
        }
        body = {
            'coordinates': [start, end],
            'profile': profile,
            'format': 'geojson',
            'radiuses': [1000, 1000]
        }
        url = f"https://api.openrouteservice.org/v2/directions/{profile}"
        
        response = requests.post(url, json=body, headers=headers)
        return response.json()['routes'][0]['summary']['distance']

    @staticmethod
    def minimum_distance(df, x, y):
        """find the coordinates of the 5 closest points (transformer stations) to a given coordinate point"""
        distance_li = [(e, n, MinimumCost.haversine(x, y, n, e)) for n, e in zip(df['y'], df['x'])]
        sorted_list = sorted(distance_li, key=lambda x: x[2])        
        return sorted_list[:5]

    @staticmethod
    def min_route(df, lat, lng):
        """find the closest route given a list of coordinates to a specified coordinate"""
        distances = [MinimumCost.get_route((lat, lng), (n, e)) for n, e in zip(df['y'], df['x'])]
        min_val = min(distances)
        index = distances.index(min_val)
        return index, min_val
