import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Wczytanie danych
df = pd.read_csv('data/pogoda_polska.csv', encoding='utf-8-sig')

# Ustawienia generowania obrazka
df_small = df[['Temperatura', 'Temp_Odczuwalna', 'Cisnienie', 'Wilgotnosc', 'Predkosc_Wiatru', 'Zachmurzenie']].copy()
df_small.columns = ['Temp', 'Odczuw.', 'Ciśn.', 'Wilg.', 'Wiatr', 'Zachm.']

corr = df_small.corr()

plt.clf()
plt.figure(figsize=(10, 8))

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 12})

plt.subplots_adjust(left=0.2, bottom=0.25, right=0.95, top=0.9)

plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

plt.title("Analiza korelacji - Projekt Pogoda", pad=20, fontsize=15)


output_name = 'data/AnalizaZdjęcie.png'
plt.savefig(output_name, dpi=300)
print(f"--- GOTOWE! Sprawdź plik o nazwie: {output_name} ---")
plt.show()
