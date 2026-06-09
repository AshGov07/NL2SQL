# test_relationships.py

from schema_loader import SchemaLoader

loader = SchemaLoader(
    host="localhost",
    user="root",
    password="Root",
    # database="classicmodels"
    database="sakila"
)

df = loader.get_relationship_dataframe()

print(df)