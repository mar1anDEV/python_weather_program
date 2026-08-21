import urllib.request
import json
import sys



def load_config():
    try:
        with open("config.json") as f:
            config = json.load(f)
            return config['api_key']
            
    except (FileNotFoundError, KeyError):
            print("Fehler: config.json oder api_key nicht gefunden.")
            sys.exit()



def get_user_input_data():
     while True:
        user_input = input("Postleitzahl oder Standort eingeben (oder 'exit'):")

        if user_input.lower() == "exit":
            print("Program beendet.")
            sys.exit()
        if not user_input:
             print('Eingabe darf nicht leer sein.')
             continue
        if user_input.isdigit():
            postleitzahl_int = int(user_input)
            if 10000 <= postleitzahl_int <= 99999:
                 return postleitzahl_int
            else:
                 print("Postleitzahl ist ungültig, muss 5 Ziffern sein.")
        else:
             if user_input.replace(" ","").isalpha():
                  return user_input
             else:
                  print("Ungültiger Standort, nur Buchstaben eingeben")


def main():
    api_key = load_config()
    land = "DE"
    #value = get_user_input_data()
    value1 = 49477

    if isinstance(value1, int):
        url=f"https://api.openweathermap.org/data/2.5/weather?zip={value1},{land}&lang=de&units=metric&appid={api_key}"
    else:
        url=f"https://api.openweathermap.org/data/2.5/weather?q={value1}&lang=de&units=metric&appid={api_key}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            #print(data['main']['temp_max'])

    except Exception as e:
         print(f"Eine Fehler ist aufgetreten: {e}")
    if data:
        
        return data
    else:return None

weatherFetcher=main()




