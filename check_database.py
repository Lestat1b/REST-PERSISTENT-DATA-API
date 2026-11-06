from database import engine
from sqlalchemy import inspect

print("\nDATABASE CONNECTION:")
print(engine.url)

print("\nDATABASE FILE:")
print(engine.url.database)

inspector = inspect(engine)

print("\nCURRENT TABLE COLUMNS:")

columns = inspector.get_columns("clinical_data")

for column in columns:
    print(column["name"], "-", column["type"])

print("\nDATABASE CHECK COMPLETE")