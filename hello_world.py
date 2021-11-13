from flask import Flask
from flask import render_template
from flask import request
import region_dict


app = Flask ("Berge")

# Code für Ausgangsseite mit Eingabe mithilfe der Website http://raspitips.de/flask-webapps-mit-python-erstellen/ erstellt
@app.route("/", methods=["GET", "POST"])
def formular_eingabe():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)



