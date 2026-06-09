from schema_loader import SchemaLoader
from query_validator import QueryValidator

loader = SchemaLoader(
    host="localhost",
    user="root",
    password="Root",
    database="classicmodels"
)

schema_df = loader.get_schema_dataframe()
relationship_df = loader.get_relationship_dataframe()

sql = """
SELECT c.customerName
FROM customers c
JOIN orders o
ON c.customerName = o.orderNumber
"""

QueryValidator.validate(
    sql,
    schema_df,
    relationship_df
)

print("VALID")