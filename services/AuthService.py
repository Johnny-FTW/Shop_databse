import bcrypt
from sqlalchemy import select, join
from db import connection
from model.Customer import customer_password_table, customer_table
from requests import LoginRequest


def login_service(data: LoginRequest):
    query = select(customer_password_table.c.value)\
        .select_from(
        join(
            customer_table,
            customer_password_table,
            customer_table.c.customer_id == customer_password_table.c.customer_id
        )
    ).where(customer_table.c.email == data.email)

    result = connection.execute(query)
    customer = result.fetchone()

    if customer is None:
        raise Exception("Password or email is not valid")

    password = customer.value
    is_valid = bcrypt.checkpw(data.password.encode("utf8"), password.encode("utf8"))

    if not is_valid:
        raise Exception("Password or email is not valid")

    print("Login is OK")