- # Assignment 1：WSCS_flask_url_shortener
  
  Web Service and Cloud-Based Service Assignment 1 - 2022 - Group 28
  
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
  - Login in account is defined in `.env` file with default USERNAME: `admin` and PASSWORD: `password`
