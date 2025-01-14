from flask import flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World, Welcome to our Apple!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
