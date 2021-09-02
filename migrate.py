import mysql.connector
from  dotenv  import  dotenv_values


creating_table_query =[]
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

creating_table_query.append("""
CREATE TABLE products
(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR (255),  
  article VARCHAR (255),
  unit VARCHAR (255),
  code VARCHAR (255),
  category_id INT
)
""")

creating_table_query.append("""
CREATE TABLE categories
(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR (255),  
  code VARCHAR (255)
  
)
""")
for query in creating_table_query:
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
