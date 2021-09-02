# pitstop
This project copies data from the https://pitstop.rv.ua/ website to your MySql database.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install (requests, mysql.connector, json, dotenv).

## Сreate .env file
In the project folder, create a file named ".env" with the data on connecting to the MySql server.
An example of the data is in the file ".env.example".

## Requests to create databases and tables
Run file migrate.py.
This file will create an "rvpitstop" database and two tables on your MySql server.
Table settings:
    categories(id, name, code)
    products(id, name, article,	unit, code, category_id)

## Creating json
Run file "download_products.py"
This file will create several ".json" files with data by products categories.
Files name "(category name).json"

## Insert data to MySql server
Run file "insert_to_database.py"
This file will upload the data to your database.
