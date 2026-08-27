"""Modellklasse für die Speicherung und Ausgabe von Wetterdaten."""


class Wetter:
    """
    Wetterinformationen für einen bestimmten Ort.
    
    Attributes:
        stadt (str): Stadtname.
        postleitzahl (str): Postleitzahl.
        latitude (float): Breitengrad.
        longitude (float): Längengrad.
        land (str): Ländercode.
        temperatur (float): Temperatur in Celsius.
        winfo (str): Wetterbeschreibung.
    """

    def __init__(self, city,latitude, longitude, country, temperature, winfo):
        """Initialisiert ein Wetter-Objekt mit allen relevanten Daten."""
        self.stadt = city
        self.latitude = latitude
        self.longitude = longitude
        self.land = country
        self.temperatur = temperature
        self.winfo = winfo
 
    def to_string(self)-> str:
        """Gibt formatierte Wetterinformationen in der Konsole aus."""
        return f'''
        Stadt: {self.stadt.capitalize()}
        Latitude:{self.latitude}
        Longitude:{self.longitude}
        Land:{self.land}
        Temperatur:{self.temperatur}°C
        Es ist:{self.winfo.capitalize()}
'''    
    def to_dict(self) -> dict:
        return {
            'Stadt' : self.stadt.capitalize(),
            'Latitude': self.latitude,
            'Longitude': self.longitude,
            'Land': self.land,
            'Temperatur': f"{self.temperatur}",
            'Es ist':  self.winfo.capitalize()
        }
