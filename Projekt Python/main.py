import requests
import pandas as pd
import time
import os

API_KEY = "84e337ef3dea2fcdbb2f01a3033528f1"
CITIES = [
    "Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", 
    "Lublin", "Białystok", "Katowice", "Gdynia", "Częstochowa", "Radom", "Toruń", 
    "Sosnowiec", "Rzeszów", "Kielce", "Gliwice", "Olsztyn", "Zabrze", "Bielsko-Biała", 
    "Bytom", "Zielona Góra", "Rybnik", "Ruda Śląska", "Opole", "Tychy", "Gorzów Wielkopolski", 
    "Elbląg", "Płock", "Dąbrowa Górnicza", "Wałbrzych", "Włocławek", "Tarnów", "Chorzów", 
    "Koszalin", "Kalisz", "Legnica", "Grudziądz", "Jaworzno", "Słupsk", "Jastrzębie-Zdrój", 
    "Nowy Sącz", "Jelenia Góra", "Siedlce", "Mysłowice", "Konin", "Piła", "Piotrków Trybunalski"
]

def fetch_weather_data():
    weather_data = []
    print(f"Rozpoczynam pobieranie danych dla {len(CITIES)} miast...")

    for city in CITIES:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},PL&appid={API_KEY}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data.append({
                    "Miasto": city,
                    "Temperatura": data['main']['temp'],
                    "Temp_Odczuwalna": data['main']['feels_like'],
                    "Cisnienie": data['main']['pressure'],
                    "Wilgotnosc": data['main']['humidity'],
                    "Predkosc_Wiatru": data['wind']['speed'],
                    "Zachmurzenie": data['clouds']['all'],
                    "Opis": data['weather'][0]['description']
                })
                print(f"✓ Pobrano: {city}")
            else:
                print(f"✗ Błąd dla {city}: {data.get('message', 'Nieznany błąd')}")
        
        except Exception as e:
            print(f"! Błąd połączenia dla {city}: {e}")
        
        time.sleep(0.1)


    if not os.path.exists('data'):
        os.makedirs('data')

    df = pd.DataFrame(weather_data)
    df.to_csv('data/pogoda_polska.csv', index=False, encoding='utf-8-sig')
    print("\n" + "="*30)
    print("SUKCES! Dane zapisane w: data/pogoda_polska.csv")
    print("="*30)

if __name__ == "__main__":
    fetch_weather_data()