import json
import plotly.express as px
from plotly.offline import plot

# Ploty Diagramme wiederum mithilfe der Demos erarbeitet
# Code für die Erstellung des plots mit den Daten der Berge und der jeweiligen Strecke
def diagramm():
    with open('bergdaten.json') as openfile:
        daten = json.load(openfile)

    xwerte = []
    ywerte = []

    for datum, berge in daten.items():
        xwerte.append(berge['Berg'])
        ywerte.append(float(berge['Distanz']))

    fig = px.bar(x=xwerte, y=ywerte)
    div = plot(fig, output_type="div")
    return div

# Code für die Erstellung des zweiten plots mit den Daten der Berge und der jeweiligen Dauer
def diagramm1():
    with open('bergdaten.json') as openfile:
        daten = json.load(openfile)

    xwerte = []
    ywerte = []

    for datum, berge in daten.items():
        xwerte.append(berge['Berg'])
        ywerte.append(float(berge['Dauer']))

    fig = px.bar(x=xwerte, y=ywerte)
    div1 = plot(fig, output_type="div")
    return div1



