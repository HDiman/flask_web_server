from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/buy")
def buy():
    return "Buy!"

if __name__ == "__main__":
    app.run()

