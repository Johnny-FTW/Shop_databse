from sqlalchemy import insert
from db import connection
from model.Product import product_table
from requests import ProductADD


def create_product_service(data: ProductADD):
    try:
        query = insert(product_table)\
            .values(
            product_name = data.product_name,
            price = data.price,
        )
        connection.execute(query)
        connection.commit()

    except Exception as e:
        print(e)
        connection.rollback()
