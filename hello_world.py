from flask import Flask
from flask import render_template
from flask import request
from region_dict import Frastanz



app = Flask ("Bergapp")

# Code für Ausgangsseite mit Eingabe mithilfe der Website http://raspitips.de/flask-webapps-mit-python-erstellen/ erstellt
@app.route("/", methods=["GET", "POST"])
def formular_eingabe():
    return render_template("index.html")

dict = Frastanz

@app.route("/berge", methods=["GET", "POST"])
def berge_filtern():
    if request.method == "POST":
        ort = request.form["ausgangsort"]
        schwierigkeit = request.form["schwierigkeitslevel"]
        anreise = request.form["anreisemittel"]

        if ort == "Frastanz" and schwierigkeit == "leicht" and anreise == "Auto":
            for key, values in dict.items():
                for value in values:
                    berg = key
                    return berg

        else:
            error = "Deine Eingabe hat irgend einen Fehler"
            return error




#    return render_template("berge.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)



