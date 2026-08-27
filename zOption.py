"""Hilfsfunktionen für Optionen zum Sammeln und Zurückgeben von Eingabewerten."""
from classComponent import Wetter
import sys
from fetchComponent import fetch
from farbenConfig import f_farbe
from printDesign import custom_display
from eOption import e_option as e_reuse


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
        d = w.to_dict()
        return p,d


def z_option():
    def get_city(arg):
        c = "Erste" if arg == 1 else "Zweite"
        while True:
            user_input = input(f_farbe(f"{c} Stadt eingeben (Postleitzahl oder Standort, oder 'exit'): ",'green'))
            if not user_input:
                print(f_farbe("Eingabe darf nicht leer sein",'red'))
                continue
            elif user_input.isdigit():
                postleitzahl_int = int(user_input)
                if 10000 <= postleitzahl_int <= 99999:
                    f_e = fetch(postleitzahl_int)
                    p_e = [e_wetter(f_e)[0],e_wetter(f_e)[1]]
                    return p_e
                else:
                    print(f_farbe("Postleitzahl ist ungültig, muss 5 Ziffern sein.",'red'))
                    continue
            elif user_input.lower() == "exit":
                print(f_farbe("Programm beendet",'yellow'))
                sys.exit()
            else:
                if user_input.replace(" ","").isalpha():
                    f_s = fetch(user_input)
                    p_s = [e_wetter(f_s)[0],e_wetter(f_s)[1]]
                    return p_s
                else:
                    print(f_farbe("Ungültiger Standort, nur Buchstaben eingeben",'red'))
    f = get_city(1)
    s = get_city(2)
    f_string = f[0]
    s_string = s[0]
    f_dict_city_val = str(f[1]['Stadt'])
    s_dict_city_val = str(s[1]['Stadt'])
    f_dict_temp_val = float(f[1]['Temperatur'])
    s_dict_temp_val = float(s[1]['Temperatur'])

    sum_temp = f_dict_temp_val - s_dict_temp_val

    city_warmer = f_dict_city_val if f_dict_temp_val > s_dict_temp_val else s_dict_city_val
    city_colder = f_dict_city_val if f_dict_temp_val < s_dict_temp_val else s_dict_city_val
    custom_display(showCustom=True,f_text=f_string,s_text=s_string,text=f"{city_warmer} ist {abs(sum_temp):.2f}°C wärmer und {city_colder} ist {abs(sum_temp):.2f}°C kälter")


                    
