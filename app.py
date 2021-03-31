from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'use http://localhost:8000/get_request...'


@app.route('/get_request')
def get_request():
    """
    get params and show them
    :return: formatted key-value pairs
    """
    asd = ""
    for key, value in request.args.items():
        asd += key + "=" + value + "; "
    return asd


@app.errorhandler(404)
def not_found(error):
    return "404 not found"


@app.errorhandler(500)
def internal_error(error):
    return "500 internal error"


if __name__ == '__main__':
    app.run(host="localhost", port=8000)
