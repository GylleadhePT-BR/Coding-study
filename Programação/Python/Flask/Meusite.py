from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Esse eu é site"

@app.route("/contatos")
def contatos():
    return "Albertinho , paulo , junioot"
        

if __name__ == "__main__":
    app.run(debug=True)