import bcrypt
from sqlalchemy import insert
from db import connection
from model.Customer import customer_table, customer_password_table
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
        ).returning(customer_table.c.customer_id)
        result = connection.execute(query)

        new_customer_id = result.fetchone().customer_id

        salt = bcrypt.gensalt(15)

        password =bcrypt.hashpw(data.password.encode("utf8"),salt)

        query = insert(customer_password_table)\
            .values(value = password.decode("utf8"), customer_id=new_customer_id)


        connection.execute(query)

        connection.commit()

        return new_customer_id

    except Exception as e:
        print(e)
        connection.rollback()
