from sqlalchemy import insert
from db import connection
from model.Customer import customer_table
from requests import RegisterRequest


def create_customer_service(data: RegisterRequest):
    try:
        query = insert(customer_table)\
            .values(
            first_name = data.first_name,
            last_name = data.last_name,
            email = data.email,
            address = data.address,
            postcode=data.postcode,
            country = data.country
        )
        connection.execute(query)
        connection.commit()

    except Exception as e:
        print(e)
        connection.rollback()
