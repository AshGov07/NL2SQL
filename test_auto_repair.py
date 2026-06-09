from schema_loader import SchemaLoader
from query_validator import QueryValidator
from sql_repair import SQLRepair

loader = SchemaLoader(
    host="localhost",
    user="root",
    password="Root",
    database="sakila"
)

schema_df = loader.get_schema_dataframe()

valid_tables = (
    schema_df["TABLE_NAME"]
    .unique()
    .tolist()
)

valid_columns = (
    schema_df["COLUMN_NAME"]
    .unique()
    .tolist()
)

sql = """
SELECT *
FROM inventory
JOIN film_category
ON inventory.film_id =
film_category.film_id
"""

try:

    QueryValidator.validate(
        sql,
        schema_df,
        loader.get_relationship_dataframe()
    )

    print("VALID FIRST TRY")

except Exception as e:

    print("Validation Failed:")
    print(e)

    repaired_sql = SQLRepair.repair_sql(
        sql,
        valid_tables,
        valid_columns
    )

    print("\nRepaired SQL:\n")
    print(repaired_sql)

    QueryValidator.validate(
        repaired_sql,
        schema_df,
        loader.get_relationship_dataframe()
    )

    print("\nVALID AFTER REPAIR")