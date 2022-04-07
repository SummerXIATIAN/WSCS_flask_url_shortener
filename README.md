# Assignment 1：WSCS_flask_url_shortener

Web Service and Cloud-Based Service Assignment 1 - 2022 - Group 28

- Summer Xia
- Tianhao Xu
- Yiming Xu

## Description

In this project, we created a REST URL-shortener service that can generate and store unique short IDs for each new url. It serves three purposes:

- **generate**: We first check the correctness of a new url, and if it is correct, we generate a unique short ID for it by combining three random characters and letters. By clicking the short url, users can go to the original website.
- **stats**: Users can change the shord ID or delete any short url stored in the database; we keep track of how many times the user change it.
- **clear**: Delete all of the short urls in the database.

## Prerequisites

- flask
- sqlite

## Run

- create the database in sqlite and update `SQLALCHEMY_DATABASE_URI`, `ADMIN_USERNAME` and `ADMIN_PASSWORD` in `setting.py`.
- run `flask run` in root directory.
