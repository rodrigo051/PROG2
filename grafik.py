import json
import matplotlib.pyplot as plt

def diagramm():
    with open('bergdaten.json') as openfile:
        daten = json.load(openfile)

    xwerte = []
    ywerte = []

    for datum, berge in daten.items:
        xwerte = xwerte.append(berge['Berg'])
        ywerte = ywerte.append(float(berge['Distanz']))


    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(xwerte, ywerte)
    plt.suptitle('Berge mit Strecke')
    return plt

    # plt.bar(xwerte, ywerte, color='blue')
    # plt.style.use('seaborn-darkgrid')
    # palette = plt.get_cmap('Set1')
    # plt.title('Übersicht Berge inkl. Kilometer', loc='center', fontsize=12, fontweight=0, color='black')
    # plt.xlabel('Berg')
    # plt.ylabel('Distanz')

