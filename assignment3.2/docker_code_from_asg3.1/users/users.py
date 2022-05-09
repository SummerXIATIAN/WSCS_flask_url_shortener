#!/bin/env python3

# USERS.py
#   by Tim Müller
#
# Created:
#   07 Mar 2022, 14:40:28
# Last edited:
#   19 Apr 2022, 16:04:52
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
#   of assignment 2, since it is obviously not a real user service.
#

from flask import Flask, request


### ENTRYPOINT ###
# Setup the application as a Flask app
app = Flask(__name__)





### API FUNCTIONS ###
# We mark this function to be called whenever the user provides the users URL ("/users") and the specified HTTP method.
@app.route("/users", methods=['POST'])
def users():
    """
        Handles managing users.

        Handles the 'users' path (/users).
        One method (POST) is supported, identified by its HTTP method.
        Because this is a bare-bone implementation, the function simply
        returns its "success" status-code and some identifier to know it has
        been called.
    """

    # Switch on the method used
    if request.method == "POST":
        return "/users POST", 200

    # No need to worry about other requests; flask will automatically return a
    #   405 if the method is not in the list of methods at the top of the function



# We mark this function to be called whenever the user provides the login URL ("/users/login") and the specified HTTP method.
@app.route("/users/login", methods=['POST'])
def login():
    """
        Handles logging users in or out.

        Handles the 'login' path (/users/login).
        One method (POST) is supported, identified by its HTTP method.
        Because this is a bare-bone implementation, the function simply
        returns its "success" status-code and some identifier to know it has
        been called.
    """

    # Switch on the method used
    if request.method == "POST":
        return "/users/login POST", 200

    # No need to worry about other requests; flask will automatically return a
    #   405 if the method is not in the list of methods at the top of the function

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)