from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flask! This is Activity 1!</p>"

if __name__ == "__main__":
    app.run(debug=True)
