import mysql.connector
from  dotenv  import  dotenv_values


config  =  dotenv_values ( ".env" ) 
create_db_query = f"CREATE DATABASE {config['DATABASE']}"

connection = mysql.connector.connect(
    user = config['USER'],
    password = config['PASSWORD'], 
    host = config['HOST']
    )
with connection.cursor() as cursor:
    cursor.execute(create_db_query)

connection = mysql.connector.connect(
    user = config['USER'],
    password = config['PASSWORD'], 
    host = config['HOST'],
    database = config['DATABASE']
)

create_products_table = """
CREATE TABLE products
(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR (255),  
  article VARCHAR (255),
  unit VARCHAR (255),
  code VARCHAR (255),
  category_id INT
)
"""

create_categories_table = """
CREATE TABLE categories
(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR (255),  
  code VARCHAR (255)
  
)
"""

with connection.cursor() as cursor:
    cursor.execute(create_products_table)
    connection.commit()

with connection.cursor() as cursor:
    cursor.execute(create_categories_table)
    connection.commit()
