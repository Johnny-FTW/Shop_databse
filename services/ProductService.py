from sqlalchemy import insert, exc
from db import connection
from model.Product import product_table
from requests import ProductADD
from psycopg2.errors import UniqueViolation


def create_product_service(data: ProductADD):
    try:
        query = insert(product_table)\
            .values(
            product_name = data.product_name,
            price = data.price)\
            .returning(product_table.c.product_id)
        result=connection.execute(query)
        connection.commit()
        return result.fetchone().product_id

    except exc.IntegrityError as e:
        connection.rollback()

        if isinstance(e.orig, UniqueViolation):
            raise Exception(f"Product already exists: product name: {data.product_name} product id: {data.product_id}")
        else:
            print(e)
