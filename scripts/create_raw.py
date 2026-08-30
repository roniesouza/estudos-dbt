from pathlib import Path

import duckdb


database_path = Path(__file__).parent.parent / "lab.duckdb"

with duckdb.connect(database_path) as connection:
    connection.execute("""
        create schema if not exists raw
    """)

    connection.execute("""
        create or replace table raw.orders as

        select *
        from (
            values
                (1, 101, date '2026-08-20', 'completed', 150.00),
                (2, 102, date '2026-08-21', 'completed', 89.90),
                (3, 101, date '2026-08-22', 'cancelled', 200.00),
                (4, 103, date '2026-08-23', 'completed', 45.50)
        ) as orders (
            order_id,
            customer_id,
            order_date,
            status,
            amount
        )
    """)