from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
import data
import grafik
from plotly.offline import plot
import matplotlib.pyplot as plt




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
    #mit return redirect wird die url mit der Auflistung der Berge aufgerufen


# Code der die Auflistung der Berge vornimmt und alle Berge mit den dazughörigen Daten (Dauer, Distanz) als Liste ausgibt
@app.route("/auflistung_berge", methods=["GET", "POST"])
def auflisten():
    bergdaten = data.bergdaten_laden()
    return render_template('berge.html', berginfos=bergdaten)
    #mit den berginfos wird dem template berge.html das gesamte Dictionary übergeben, welches in Jinja dann weiterbearbeitet wird


# Code für die Berechnung und Ausgabe der Gesamtdauer, Gesamtstrecke und der Durchschnittsdauer
@app.route("/auflistung_tourdaten", methods=["GET", "POST"])
def auflisten_tourdaten():
    bergdaten = data.bergdaten_laden()
    datenliste = list(bergdaten.values())
    for berge in datenliste:
        dauer = berge['Dauer']
        strecke = berge['Distanz']

    return render_template('tourdaten.html', test=dauer, test1=strecke)


@app.route("/grafische_uebersicht", methods=["GET", "POST"])
def grafische_darstellung():
    plt = grafik.diagramm()
    div = plot(plt, output_type="div")

    return render_template('diagramm.html', diagramm=div)



if __name__ == "__main__":
    app.run(debug=True, port=5000)



