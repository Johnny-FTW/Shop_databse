from dotenv import dotenv_values
from model.Customer import customer_table
from model.Order import orders_table, order_detail_ID_table
from model.Product import product_table

config = dotenv_values("./.env")
environment = config.get("ENVIRONMENT")


def create_tables(engine, metadata):
    if environment.lower() == "development":
        metadata.drop_all(engine, checkfirst=True)
    metadata.create_all(engine, checkfirst=True)

# customer_table
# orders_table
# order_detail_ID_table
# product_table
