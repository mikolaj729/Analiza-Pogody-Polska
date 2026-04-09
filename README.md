# Analiza Pogody Polska
Zadanie projektowa
Analiza Korelacji Parametrów Pogodowych w Polsce (Etap 2)

# Cel projektu
Celem aplikacji jest automatyczne pobieranie aktualnych danych meteorologicznych dla 50 największych miast w Polsce oraz analiza statystyczna zależności między różnymi parametrami pogodowymi.

# Struktura repozytorium
* **main.py** – Skrypt odpowiedzialny za komunikację z OpenWeather API, pobieranie danych i ich serializację do pliku CSV.
* **analiza.py** – Skrypt analityczny, który wczytuje dane z pliku CSV i generuje macierz korelacji Pearsona.
* **data/** – Folder przechowujący bazę danych oraz wygenerowane wizualizacje (automatyczna generacja folderu przez program main.py).
  * `pogoda_polska.csv` – Surowe dane pobrane z API.
  * `AnalizaZdjęcie.png` – Wykres heatmapy przedstawiający korelacje.

# Instrukcja uruchomienia
1. Pobierz repozytorium na dysk.
2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install pandas seaborn matplotlib requests
3. Uruchom program main.py
4. Uruchom program analiza.py
