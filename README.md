# Assignment：WSCS_flask_url_shortener

Web Service and Cloud-Based Service Assignment - 2022 - Group 28

- Summer Xia
- Tianhao Xu
- Yiming Xu

## Requirements

- flask
- sqlite

## Run

- Set environment variables for flask, if there are not `.flaskenv` and `.env` files.
  - `export FLASK_APP=./url_shortener
    export FLASK_ENV=development`
  - `export DATABASE_URL=:///db.sqlite3
    export ADMIN_PASSWORD=password
    export ADMIN_USERNAME=admin`
- Execute by `flask run` and go `http://127.0.0.1:5000/`
- <del>Login in account is defined in `.env` file with default USERNAME: `admin` and PASSWORD: `password`</del>

## User Login

- Login by `admin1` and `12345` for normal user or by `admin2` and `12345` for admin user.

- If no users exist, please create a user by making POST requist to `http://127.0.0.1:5000/user` with JSON raw Body: `{"name":"xxxxx","password":"xxxxx"}`

## Short URL

- POST to `http://127.0.0.1:5000/add_link` with "form-data" Body, `Key=originial_url` and `value=xxxx.com`

- PUT to `http://127.0.0.1:5000/<xxx>/update` with "form-data" Body, `Key=update_url` and `value=xxx`

- 

## Manual Table

- Default main page is `http://127.0.0.1:5000`, which will be omitted in the table below.

#### User service

| Entrace         | Method | Description               | Requirements                        | Test by           |
| --------------- | ------ | ------------------------- | ----------------------------------- | ----------------- |
| /login          | GET    | Login and return a JWT    | -                                   | postman & webpage |
| /user           | POST   | Create user               | -                                   | postman           |
| /user           | GET    | Get all users info        | - admin<br/>- token(login) required | postman           |
| /user/<user_id> | GET    | Get user info             | - admin<br/>- token(login) required | postman           |
| /user/<user_id> | PUT    | Promoted to administrator | - admin<br/>- token(login) required | postman           |
| /user/<user_id> | DELETE | Delete User               | - admin<br/>- token(login) required | postman           |

#### URL-Shortener

| Entrace             | Method | Description                                    | Requirements                      | P.S.               |
| ------------------- | ------ | ---------------------------------------------- | --------------------------------- | ------------------ |
| /                   | GET    | Index/main page                                | -                                 | postman  & webpage |
| /<short_url>        | GET    | Redirect to original url                       | - token(login) required           | postman            |
| /add_link           | POST   | Create a shorturl for original website         | - token required                  | postman            |
| /stats              | GET    | Show all statistics                            | - token required (free for debug) | postman  & webpage |
| /clear              | GET    | Clear all the  shorturls recorded by this user | - admin<br/>- token required      | postman            |
| /<short_url>/del    | GET    | Delete the shorturl                            | - admin<br/>- token required      | postman            |
| /<short_url>/update | PUT    | update a shorturl with a random choice         | - token required                  | postman            |
| /<short_url>/update | POST   | update a shorturl with a custom url            | - token required                  | postman            |
