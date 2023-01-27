from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1>Hello World!</h1>' \



if __name__ == "__main__":
    # Run the app in debug mode to auto-reload/debug
    app.run(debug=True)
    