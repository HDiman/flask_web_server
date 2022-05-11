from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center" >Hello, Whole World!</h1>' \
           '<p>This is paragraph</p>' \
           '<img src="https://media2.giphy.com/media/3o6ZtelrVAOD5EcmCQ/giphy.mp4?cid=790b7611b18f29dd8ee8ef2ccb90299f8abcaf10af72545f&rid=giphy.mp4&ct=g">' \
           '<img src="https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8bWFufGVufDB8fDB8fA%3D%3D&w=1000&q=80">'

def make_bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'
    return wrapper

def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return '<em>' + func(*args, **kwargs) + '</em>'
    return wrapper

def make_underlined(func):
    def wrapper(*args, **kwargs):
        return '<u>' + func(*args, **kwargs) + '</u>'
    return wrapper


@app.route("/buy")
@make_bold
@make_emphasis
@make_underlined
def buy():
    return "Buy! "

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)

