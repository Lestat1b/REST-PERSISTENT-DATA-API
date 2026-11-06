# update_database.py

from database import engine
from sqlalchemy import inspect, text

inspector = inspect(engine)

existing_columns = [
    column["name"]
    for column in inspector.get_columns("clinical_data")
]

required_columns = {
    "blood_pressure": "TEXT",
    "heart_rate": "INTEGER",
    "temperature": "FLOAT",
}

with engine.begin() as connection:

    for column_name, column_type in required_columns.items():

        if column_name not in existing_columns:

            connection.execute(text(
                f"ALTER TABLE clinical_data "
                f"ADD COLUMN {column_name} {column_type}"
            ))

            print(f"Added column: {column_name}")

        else:
            print(f"Column already exists: {column_name}")

print("Database update complete!")