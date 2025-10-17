from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"

@app.route("/username/<name>")
def user_page(name):
    return f"<h1>{name} is learning Flask!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
