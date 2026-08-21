from fetchAPIW import weatherFetcher
import math

def destructure():
    if weatherFetcher:
        data = {
            'city': weatherFetcher['name'],
            'winfo': weatherFetcher['weather'][0]['main'],
            'longitude': weatherFetcher['coord']['lon'],
            'latitude': weatherFetcher['coord']['lat'],
            'country': weatherFetcher['sys']['country'],
            'temperature': weatherFetcher['main']['temp']
        }
        return data
    return False

class Wetter:
    def __init__(self, city, postcode=None, latitude=None, longitude=None, country=None, temperature=None, winfo=None):
        self.stadt = city
        self.postleitzahl = postcode
        self.latitude = latitude
        self.longitude = longitude
        self.land = country
        self.temperatur = temperature
        self.winfo = winfo

    def schreib(self):
        print(f"Stadt: {self.stadt.capitalize()}")
        print(f"Latitude: {self.latitude}")  
        print(f"Longitude: {self.longitude}")  
        print(f"Land: {self.land}")
        print(f"Temperatur: {self.temperatur}°C")  
        print(f"Es ist: {self.winfo.capitalize()}")

    def compare_cities(self, other_city):  
        print(f"\n==== COMPARE {self.stadt} AND {other_city.stadt} ====")
        
        if self.temperatur > other_city.temperatur:
            print(f"{self.stadt} is warmer: {self.temperatur}°C")
            print(f"{other_city.stadt}: {other_city.temperatur}°C")
        else:
            print(f"{other_city.stadt} is warmer: {other_city.temperatur}°C")
            print(f"{self.stadt}: {self.temperatur}°C")

wetter1 = Wetter(
    city="Ibbenbüren",
    latitude=52.26,
    longitude=7.71,
    country="DE",
    temperature=16.8,
    winfo="Clouds"
)

wetter2 = Wetter(
    city="Berlin",
    latitude=52.52,
    longitude=13.40,
    country="DE",
    temperature=18.5,
    winfo="Sunny"
)

# Use them
wetter1.schreib()
wetter1.compare_cities(wetter2)  