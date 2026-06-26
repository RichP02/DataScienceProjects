import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

carpeta_actual = Path(__file__).parent
vendidos = pd.read_csv(carpeta_actual / 'sales.csv')

vendidos = vendidos.drop(columns = 'Rank')
vendidos.isnull().sum()
vendidos[vendidos.isnull().any(axis=1)]
vendidos['Year'] = vendidos['Year'].ffill()
vendidos['Publisher'] = vendidos['Publisher'].bfill()

ventas_por_genero = vendidos.groupby('Genre')['Global_Sales'].sum()

plt.figure(figsize=(12, 6))
ventas_por_genero.plot(kind = 'bar', color = 'skyblue')
plt.title('Ventas Globales por Género')
plt.xlabel('Género')
plt.ylabel('Ventas Globales (en millones)')
plt.xticks(rotation = 45)
plt.show()

publisher = vendidos['Publisher'].value_counts()
publishers_top = publisher.sort_values(ascending=False).head(10)
publishers_top = publishers_top[::-1]

x = publishers_top.values
y = publishers_top.index

plt.barh(y, x, color='skyblue')
plt.ylabel('Editores')
plt.title('Top 10 editores')
plt.show()

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
na_sizes = vendidos.groupby('Genre')['NA_Sales'].sum()
na_sizes.plot(kind='bar')
plt.xlabel('Genre')
plt.ylabel('NA_Sales')
plt.title('NA_Sales by Genre')

plt.subplot(2, 3, 2)
eu_sizes = vendidos.groupby('Genre')['EU_Sales'].sum()
eu_sizes.plot(kind='bar')
plt.xlabel('Genre')
plt.ylabel('EU_Sales')
plt.title('EU_Sales by Genre')

plt.subplot(2, 3, 3)
jp_sizes = vendidos.groupby('Genre')['JP_Sales'].sum()
jp_sizes.plot(kind='bar')
plt.xlabel('Genre')
plt.ylabel('JP_Sales')
plt.title('JP_Sales by Genre')

plt.subplot(2, 3, 4)
other_sizes = vendidos.groupby('Genre')['Other_Sales'].sum()
other_sizes.plot(kind='bar')
plt.xlabel('Genre')
plt.ylabel('Other_Sales')
plt.title('Other_Sales by Genre')

plt.subplot(2, 3, 5)
global_sizes = vendidos.groupby('Genre')['Global_Sales'].sum()
global_sizes.plot(kind='bar')
plt.xlabel('Genre')
plt.ylabel('Global_Sales')
plt.title('Global_Sales by Genre')

plt.tight_layout()
plt.show()