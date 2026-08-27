"""
fetchAPIW.py
~~~~~~~~~~~~

Modul zum Abrufen von Wetterdaten von der OpenWeatherMap API.
Unterstützt Abfragen nach Postleitzahl oder Stadtnamen.

"""

import urllib.request
import json
import sys


def load_config():
    """
    Lädt den API-Schlüssel aus der config.json Datei.
    
    Returns:
        str: API-Schlüssel aus der Konfigurationsdatei.
        
    Raises:
        SystemExit: Wenn config.json oder api_key nicht gefunden wird.
    """
    try:
        with open("config.json") as f:
            config = json.load(f)
            return config['api_key']
            
    except (FileNotFoundError, KeyError):
            print("Fehler: config.json oder api_key nicht gefunden.")
            sys.exit()


def fetch(arg):
    """
    Ruft Wetterdaten von der OpenWeatherMap API ab.
    
    Args:
        arg (int or str): Postleitzahl (int) oder Stadtnamen (str).
    
    Returns:
        dict: API-Response mit Wetterdaten.
        None: Wenn ein Fehler auftritt.
    """
    api_key = load_config()
    land = "DE"
    
    # Konvertiere Umlaute für API-Kompatibilität
    if isinstance(arg, str):
        arg = arg.replace("ü", "ue").replace("ö", "oe").replace("ä", "ae").replace("ß","ss")
    
    # Konstruiere URL basierend auf Argument-Typ
    if isinstance(arg, int):
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={arg},{land}&lang=de&units=metric&appid={api_key}"
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={arg}&lang=de&units=metric&appid={api_key}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
        return None

