from sqlalchemy import (
    Table,
    Integer,
    Column,
    DateTime,
    ForeignKey, func
)

from db import metadata
from model.Customer import customer_table
from model.Product import product_table


orders_table = Table(
    "orders_table",
    metadata,
    Column("order_id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey(customer_table.c.customer_id, ondelete="CASCADE", onupdate="CASCADE"),
           nullable=False),
    Column(("created_at"), DateTime (timezone=True), default=func.now())
)


order_items_table = Table(
    "order_items",
    metadata,
    Column("order_item_id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey(orders_table.c.order_id, ondelete="CASCADE", onupdate="CASCADE"),
           nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("product_id", Integer, ForeignKey(product_table.c.product_id, ondelete="CASCADE", onupdate="CASCADE"),
           nullable=False)
)