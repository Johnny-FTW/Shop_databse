from sqlalchemy import (
    Table,
    Integer,
    Text,
    Column,
)

from db import metadata

customer_table = Table(
    "customers",
    metadata,
    Column("customer_id", Integer, primary_key=True),
    Column("first_name", Text, nullable=False),
    Column("last_name", Text, nullable=False),
    Column("country", Text, nullable=False),
)

