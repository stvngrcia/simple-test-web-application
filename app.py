#!/usr/bin/python3
from flask import Flask, request, json

'''
initializing flask app.
'''
app = Flask(__name__)


@app.route("/test", methods=["POST"])
def test():
    '''
        Only accept a POST request with two arguments x and y
        it will then return a JSON object in the form of {"sum":x+y}
    '''
    data = request.get_json()
    result = {"sum": data["x"] + data["y"]}
    return (json.dumps(result) + "\n")


@app.errorhandler(500)
def handleInvalidRequests(error):
    '''
        Handles an invalid request that does not include x or y
    '''
    message = {"message": ("The browser (or proxy)" +
               "sent a request that this server could not understand.")}
    return (json.dumps(message) + "\n")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
