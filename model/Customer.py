from sqlalchemy import (
    Table,
    Integer,
    Text,
    Column,
    DateTime,
    func,
    ForeignKey
)

from db import metadata

customer_table = Table(
    "customers",
    metadata,
    Column("customer_id", Integer, primary_key=True),
    Column("first_name", Text, nullable=False),
    Column("last_name", Text, nullable=False),
    Column("email", Text, nullable=False),
    Column("address", Text, nullable=False),
    Column("postcode", Text,nullable=False),
    Column("country", Text, nullable=False),
    Column("created_at", DateTime(timezone=True), default=func.now()),
)

customer_password_table = Table(
    "customer_passwords",
    metadata,
    Column("customer_password_id", Integer, primary_key=True),
    Column("value", Text, nullable=False),
    Column("customer_id", Integer, ForeignKey(customer_table.c.customer_id, ondelete="CASCADE", onupdate="CASCADE"), nullable=False),
    Column("created_at", DateTime(timezone=True), default=func.now()),
)

