from typing import List
from sqlalchemy import insert, select, join, func
from db import connection
from model.Order import orders_table, order_detail_ID_table
from model.Product import product_table
from requests import RegisterOrder


def create_order_service(data: RegisterOrder):
    try:
        query = insert(orders_table)\
            .values(customer_id = data.customer_id)\
            .returning(orders_table.c.order_id)

        result = connection.execute(query)
        connection.commit()
        return result.fetchone().order_id

    except Exception as e:
        connection.rollback()
        print(e)


def create_order_service_detail(data: RegisterOrder):
    try:
        query = insert(order_detail_ID_table)\
            .values(
            order_id= data.order_id,
            quantity = data.quantity,
            product_id = data.product_id

        )
        connection.execute(query)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(e)


# overview
# select order_detail_id, product_name, quantity,price, quantity*price as total
# from "orders_details_IDs" as o
# left join products as p using(product_id)
# where order_id = 1;


def show_order(order_id: int) -> List[dict]:
    query = select( product_table.c.product_name,order_detail_ID_table.c.quantity, product_table.c.price,
                    (product_table.c.price*order_detail_ID_table.c.quantity).label("total"))\
        .select_from(join(order_detail_ID_table, product_table))\
        .where(order_detail_ID_table.c.order_id == order_id)
    result = connection.execute(query)
    return result.fetchall()


# select order_id, sum(quantity*price) as total_price
# from "orders_details_IDs" as o
# left join products as p using(product_id)
# where order_id = 1
# group by order_id;

def show_total_price(order_id: int):
    query = select(func.sum(product_table.c.price*order_detail_ID_table.c.quantity).label("total_price")) \
        .select_from(join(order_detail_ID_table, product_table))\
        .where(order_detail_ID_table.c.order_id == order_id)\
        .group_by(order_detail_ID_table.c.order_id)
    result = connection.execute(query)
    return result.fetchone()


