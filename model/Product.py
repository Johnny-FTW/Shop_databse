from sqlalchemy import (
    Table,
    Integer,
    Text,
    Column,
)
from db import metadata

product_table = Table(
    "products",
    metadata,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", Text, nullable=False),
    Column("price", Integer, nullable=False),
)
