from calendar import month

import pandas as pd

def obtenerMonedas():
    dataFrame = pd.read_csv("data/CambiosMonedas.csv")
    monedas = dataFrame["Moneda"].tolist()
    return list(set(monedas))

def graficar(): pass

def estadisticas(): pass

print(obtenerMonedas())