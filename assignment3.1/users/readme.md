# WCSC Assignment 3.1 README -- users auth

### DECLARATION

In assignment 3, we used the reference implementation of `url_shortener` and `users_auth` from Canvas (assignment2-barebone). Our work is to deploy each service in on container via docker.

### Code

Run the python script and it will invoke a flask service on 5002 port

`python users.py`

## build

`docker build -t summerxia2009/wcsc_users .`

## run

We uploaded the packaged image to docker hub, which became a publicly accessible repository under my own docker hub account.

`docker pull summerxia2009/wcsc_users`

`docker run -p 5002:5002 summerxia2009/wcsc_users`

## test by postman on 127.0.0.1:5002

| Entrace      | Method | Return                   | Test by |
| ------------ | ------ | ------------------------ | ------- |
| /users       | POST   | "/users POST", 200       | postman |
| /users/login | POST   | "/users/login POST", 200 | postman |