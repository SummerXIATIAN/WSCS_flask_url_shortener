#!/bin/env python3

# URL SHORTENER.py
#   by Tim Müller
#
# Created:
#   03 Mar 2022, 14:25:23
# Last edited:
#   19 Apr 2022, 16:05:06
# Auto updated?
#   Yes
#
# Description:
#   Implements a barebone framework to containerize in assignment 3.
#   Build with the Flask (https://flask.palletsprojects.com/en/2.0.x/)
#   framework.
#
#   We only provide the bare flask skeleton with a couple of code paths like
#   you would find in a fully-fledged service.
#   You should only use this framework if you have no (working) implementation
#   of assignment 2, since it is obviously not a real URL-shortening service.
#

from flask import Flask, request


### ENTRYPOINT ###
# Setup the application as a Flask app
app = Flask(__name__)





### API FUNCTIONS ###
# We mark this function to be called whenever the user provides the root URL ("/") and one of the specified HTTP methods.
@app.route("/", methods=['GET', 'POST', 'DELETE'])
def root():
    """
        Handles everything that falls under the API root (/).
        Three methods (GET, POST and DELETE) are supported, each of which is
        identified by its HTTP method.
        Because this is a bare-bone implementation, each function simply
        returns its "success" status-code and some identifier to know which one
        has been called.
        You can extend these functions to work with the authentication JWT you
        obtained from your authorization service.
    """

    # Switch on the method used
    if request.method == "GET":
        return "/ GET", 200

    elif request.method == "POST":
        return "/ POST", 201

    elif request.method == "DELETE":
        return "/ DELETE", 404

    # No need to worry about other requests; flask will automatically return a
    #   405 if the method is not in the list of methods at the top of the function



# We mark this function to be called for any URL that is nested under the root ("/:id").
# The syntax of the identifier is '<string:id>', which tells flask it's a string (=any non-slash text) that is named 'id'
@app.route("/<string:id>", methods=['GET', 'PUT', 'DELETE'])
def url(id):
    """
        Handles everything that falls under a URL that is an identifier (/:id).
        Three methods (GET, POST and DELETE) are supported, each of which is
        identified by its HTTP method.
        Because this is a bare-bone implementation, each function simply
        returns its "success" status-code and some identifier to know which one
        has been called.
        You can extend these functions to work with the authentication JWT you
        obtained from your authorization service.
    """

    # Switch on the method used
    if request.method == "GET":
        return "/:id GET", 301

    elif request.method == "PUT":
        return "/:id PUT", 200

    elif request.method == "DELETE":
        return "/:id DELETE", 204

    # No need to worry about other requests; flask will automatically return a
    #   405 if the method is not in the list of methods at the top of the function

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)