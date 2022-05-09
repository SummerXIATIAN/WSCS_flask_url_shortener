# WCSC Assignment 3.1 README -- url_shortener

### DECLARATION

In assignment 3, we used the reference implementation of `url_shortener` and `users_auth` from Canvas (assignment2-barebone). Our work is to deploy each service on container via docker.

### Code

Run the python script and it will invoke a flask service on 5001 port

`python url-shortener.py`

## build

`docker build -t summerxia2009/wcsc_url .`

## run

We uploaded the packaged image to docker hub, which became a publicly accessible repository under my own docker hub account.

`docker pull summerxia2009/wcsc_url`

`docker run -p 5001:5001 summerxia2009/wcsc_url`

## test by postman on 127.0.0.1:5001

| Entrace      | Method | Return             | Test by           |
| ------------ | ------ | ------------------ | ----------------- |
| /            | GET    | "/ GET", 200       | postman & webpage |
| /            | POST   | "/ POST", 201      | postman           |
| /            | DELETE | "/ DELETE", 404    | postman           |
| /<string_id> | GET    | "/:id GET", 301    | postman & webpage |
| /<string_id> | POST   | "/:id PUT", 200    | postman           |
| /<string_id> | DELETE | "/:id DELETE", 204 | postman           |
