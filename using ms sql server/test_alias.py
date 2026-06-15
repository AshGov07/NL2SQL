from schema_loader import SchemaLoader
from query_validator import QueryValidator

loader = SchemaLoader(
    server="MLS-AI-PC",
    database="AdventureWorksDW2025"
)

schema_df = loader.get_schema_dataframe()
relationship_df = loader.get_relationship_dataframe()

sql = """
SELECT
    d.SalesTerritoryRegion
FROM
    DimSalesTerritory AS d
"""

QueryValidator.validate(
    sql,
    schema_df,
    relationship_df
)

print("VALID")