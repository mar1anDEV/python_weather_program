"""Haupt-Einstiegspunkt der Wetteranwendung."""
import sys
from eOption import e_option
from classComponent import Wetter
from zOption import z_option
from haversine import haversine

def f_farbe(text, farbe):
        farben = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'cyan': '\033[96m'
        }
        reset = '\033[0m'
        return farben.get(farbe,'') + text + reset

def e_wetter(arg: object)-> object:
        w = Wetter(
            city=arg['name'],
            latitude=arg['coord']['lat'],
            longitude=arg['coord']['lon'],
            country=arg['sys']['country'],
            temperature=arg['main']['temp'],
            winfo=arg['weather'][0]['main']
        )
        return w

def main():
    """Startet das Wetter-Menü und steuert die Auswahl der Funktionen."""

    

    while True:
        print(f_farbe("\n" + "="*50,'cyan'))
        print(f_farbe("WETTER-ANWENDUNG - MENÜ",'cyan'))
        print(f_farbe("="*50,'cyan'))
        print(f_farbe("1. Wetterdaten der aktuellen Stadt anzeigen",'green'))
        print(f_farbe("2. Wetter zwischen zwei Städten vergleichen",'cyan'))
        print(f_farbe("3. Beenden",'yellow'))
        
        wahl = input(f_farbe("\nBitte wähle eine Option (1-3): ",'blue'))
        if not wahl:
            print(f_farbe("Eingabe darf nicht leer sein",'red'))
            continue

        elif wahl.isdigit() and wahl in ["1","2","3"]:
            wahl_int = int(wahl)
            if wahl_int == 1:
                e_option()
                return True
            elif wahl_int == 2:
                z_option()
                return True
            else:
                print("Program beendet")
                sys.exit()

        else:
            print(f_farbe("❌ Bitte gib eine Zahl ein (1-3)",'red'))
            continue   
main()