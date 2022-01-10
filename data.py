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








