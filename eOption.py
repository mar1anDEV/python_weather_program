"""Funktionen für die Benutzereingabe beim Wetterprogramm."""
from classComponent import Wetter
import sys
from fetchComponent import fetch
from farbenConfig import f_farbe
from printDesign import custom_display
def e_wetter(arg: object)-> object:
        w = Wetter(
            city=arg['name'],
            latitude=arg['coord']['lat'],
            longitude=arg['coord']['lon'],
            country=arg['sys']['country'],
            temperature=arg['main']['temp'],
            winfo=arg['weather'][0]['main']
        )
        p = w.to_string()
        return p

def e_option():
    """Liest eine Stadt oder Postleitzahl ein und ruft bei Bedarf den Fetch auf."""
    while True:
          user_input = input(f_farbe("Postleitzahl oder Standort eingeben (oder 'exit'):",'green'))
          if user_input.isdigit():
               postleitzahl_int = int(user_input)
               if 10000 <= postleitzahl_int <= 99999:
                     e_fetch_int = fetch(postleitzahl_int)
                     display = e_wetter(e_fetch_int)
                     custom_display(display)
                     return True
               else:
                    print(f_farbe("Postleitzahl ist ungültig, muss 5 Ziffern sein.",'red'))
                    continue
          elif user_input.lower() == "exit":
                print(f_farbe("Program beendet",'yellow'))
                sys.exit()
          elif not user_input:
               print(f_farbe("Eingabe darf nicht leer sein",'red'))
               continue
          else:
                if user_input.replace(" ","").isalpha():
                    e_fetch_str = fetch(user_input)
                    display = e_wetter(e_fetch_str)
                    custom_display(text=display)
                    return True
                else:
                      print(f_farbe("Ungültiger Standort, nur Buchstaben eingeben",'red'))
               
