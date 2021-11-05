from flask import Flask
from flask import render_template

app = Flask ("Bootstrap_Versuch")


@app.route("/")
def start():
    name = False
    cards = [
        {"titel": "Card 0", "inhalt": "Blubber"},
        {"titel": "Card 1", "inhalt": "Bla"},
        {"titel": "Card 2", "inhalt": "Käsekuchen"},
        {"titel": "Card 3", "inhalt": "Sülze"},
    ]
    return render_template("index.html", name=name, cards=cards)


if __name__ == "__main__":
    app.run(debug=True, port=5000)



