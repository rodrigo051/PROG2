from datetime import datetime
import json


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

def bergdaten_speichern(bergdaten):
    datei_name = "bergdaten.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, bergdaten)
    return zeitpunkt, bergdaten

def bergdaten_laden():
    datei_name = "bergdaten.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


#Dictionary für Bergauswahl

# berglist = {
#     "Gurtisspitze": {"Einzugsgebiet": ["Frastanz", "Satteins", "Schlins", "Schnifis"], "Schwierigkeit": "leicht", "Anreise": "Auto"},
#     "Sattelalpe": {"Einzugsgebiet": ["Frastanz", "Satteins", "Schlins", "Schnifis"], "Schwierigkeit": "leicht", "Anreise": "Auto"},
#     "Hohe Köpfe": {"Einzugsgebiet": ["Frastanz", "Satteins", "Schlins", "Schnifis"], "Schwierigkeit": "mittel", "Anreise": "Auto"},
#     "Drei Schwestern": {"Einzugsgebiet": ["Frastanz", "Satteins", "Liechtenstein"], "Schwierigkeit": "schwer", "Anreise": "Auto"},
#     "Zeawas Heil Spitz": {"Einzugsgebiet": ["Frastanz", "Satteins", "Schlins", "Schnifis"], "Schwierigkeit": "leicht", "Anreise": "ÖV"},
#     "Goppaschrofa": {"Einzugsgebiet": ["Frastanz", "Satteins", "Schlins", "Schnifis"], "Schwierigkeit": "mittel", "Anreise": "ÖV"},
#     "Hochgerach": {"Einzugsgebiet": ["Frastanz", "Satteins","Schlins", "Schnifis"], "Schwierigkeit": "schwer", "Anreise": "ÖV"}
# }






