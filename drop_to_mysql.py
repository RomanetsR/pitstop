import mysql.connector
import json
from  dotenv  import  dotenv_values


config  =  dotenv_values ( ".env" ) 

categories = {
    'Автогума, диски, цепи': '1d6f5bec-d49c-11e4-8586-002590aa75d3',
    'Аксесуари та інше': 'a5aa1e6f-d49b-11e4-8586-002590aa75d3',
    'Акумулятори': '11722ecb-d49c-11e4-8586-002590aa75d3'
}

connection = mysql.connector.connect(
    user = config['USER'], 
    password = config['PASSWORD'], 
    host = config['HOST'], 
    database = config['DATABASE']
    )

for name in categories:

    with open(name + '.json', encoding='utf-8', newline='') as file:

        products = json.load(file)

    categories_query = """
        INSERT INTO categories ( name, code )
        VALUES ( %s, %s )
    """
    with connection.cursor() as cursor:
        cursor.execute(categories_query, (name, categories[name]))
        connection.commit()

    with connection.cursor() as cursor:
        cursor.execute("SELECT last_insert_id()")
        category_id = cursor.fetchone()[0]

    for product in products:
        products_query = """
                        INSERT INTO products ( name, article, unit, code, category_id )
                        VALUES
                        (%s, %s, %s, %s, %s)
                        """

        with connection.cursor() as cursor:
            cursor.execute(products_query, (product['Name'], product['Article'], product['Unit'], product['Code'], category_id))
            connection.commit()
