from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import data
import grafik

# sehr vieles in der App konnte mihilfe der Demos aus PROG2 erarbeitet werden, was sehr hilfreich war
app = Flask ("Bergapp")

# Code für Ausgangsseite mit Eingabe
@app.route("/", methods=["GET", "POST"])
def formular_eingabe():
    return render_template("index.html")

# Code für die Speicherung der Eingabe vom Berggipfel, der Dauer und der Strecke
@app.route("/berge", methods=["GET", "POST"])
def berge_filtern():
    if request.method == "POST":
        berg = request.form["berggipfel"]
        dauer = request.form["laufzeit"]
        distanz = request.form["zurueckgelegte_distanz"]

        bergdaten = {
                "Berg": berg,
                "Dauer": int(dauer),
                "Distanz": float(distanz)
            }

        data.bergdaten_speichern(bergdaten)

    return redirect(url_for('auflisten'))
    # mit return redirect wird die url mit der Auflistung der Berge aufgerufen

# Code der die Auflistung der Berge vornimmt und alle Berge mit den dazughörigen Daten (Dauer, Distanz) als Liste ausgibt
@app.route("/auflistung_berge", methods=["GET", "POST"])
def auflisten():
    bergdaten = data.bergdaten_laden()
    for key, values in bergdaten.items():
        bergdaten[key].update({'Datum': key.split('.')[0]}) # Datum wird nach . gesplitet, um die Millisekungen zu entfernen

    return render_template('berge.html', berginfos=bergdaten)
    # mit den berginfos wird dem template berge.html das gesamte Dictionary übergeben, welches in Jinja dann weiterbearbeitet wird

# Code für die Berechnung und Ausgabe der Gesamtdauer, Gesamtstrecke und der Durchschnittsdauer
@app.route("/auflistung_tourdaten", methods=["GET", "POST"])
def auflisten_tourdaten():
    bergdaten = data.bergdaten_laden()
    datenliste = list(bergdaten.values())
    dauer = 0
    strecke = 0
    # Berechnungen für die gesamte Dauer und Distanz der Bergtouren
    for berge in datenliste:
        dauer = dauer + berge['Dauer']
        strecke = strecke + berge['Distanz']
    # Berechnungen des Dauerdurchschnitts und des Streckedurchschnitts
    dauerdurchschnitt = dauer / len(datenliste)
    dauerdurchschnitt = "{:.1f}".format(dauerdurchschnitt) # Formatierung auf eine Kommastelle
    streckendurchschnitt = strecke / len(datenliste)
    streckendurchschnitt = "{:.1f}".format(streckendurchschnitt) # Formatierung auf eine Kommastelle

    return render_template('tourdaten.html', dauer=dauer, strecke=strecke, dauerdurchschnitt=dauerdurchschnitt, streckendurchschnitt=streckendurchschnitt)
    # Attribute oben werden an tourdaten.html übergeben

# Code für die Darstellung der zurückgelegten Dauer u. Strecken in einem Plotly-Balkendiagramm
@app.route("/grafische_uebersicht", methods=["GET", "POST"])
def grafische_darstellung():
    div = grafik.diagramm()
    div1 = grafik.diagramm1()

    return render_template('diagramm.html', viz_div=div, viz_div1=div1)
    # Weitergabe der Diagramme an diagramm.html


if __name__ == "__main__":
    app.run(debug=True, port=5000)



