from flask import Flask
from flask import render_template
from flask import request
import data


app = Flask ("Bergapp")

# Code für Ausgangsseite mit Eingabe mithilfe der Website http://raspitips.de/flask-webapps-mit-python-erstellen/ erstellt
@app.route("/", methods=["GET", "POST"])
def formular_eingabe():
    return render_template("index.html")



# @app.route("/berge", methods=["GET", "POST"])
# def berge_filtern():
#     if request.method == "POST":
#         ort = request.form["ausgangsort"]
#         schwierigkeit = request.form["schwierigkeitslevel"]
#         anreise = request.form["anreisemittel"]
#
#         filtered_list = []
#         for berge, attribute in berglist.items():
#             if anreise == attribute["Anreise"] and schwierigkeit == attribute["Schwierigkeit"] and ort in attribute["Einzugsgebiet"]:
#                 filtered_list.append(berge)
#
#         return render_template("berge.html", bergliste=filtered_list)

@app.route("/berge", methods=["GET", "POST"])
def berge_filtern():
    if request.method == "POST":
        berg = request.form["berggipfel"]
        dauer = request.form["laufzeit"]
        distanz = request.form["zurueckgelegte_distanz"]

        bergdaten = {
                "Berg": berg,
                "Dauer": dauer,
                "Distanz": distanz
            }

        bergdaten = data.bergdaten_speichern(bergdaten)
    return render_template('berge.html', berginfos=bergdaten)





        # else:
        #     error = "Deine Eingabe hat irgendeinen Fehler"
        #     return error




#    return render_template("berge.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)



