import pandas as pd
from schema_loader import SchemaLoader

loader = SchemaLoader(
    server="MLS-AI-PC",
    database="AdventureWorksDW2025"
)

query = """
SELECT TOP 10
    DimCustomer.CustomerKey,
    DimCustomer.FirstName,
    DimCustomer.LastName,
    SUM(FactInternetSales.SalesAmount) AS TotalSales
FROM FactInternetSales
JOIN DimCustomer
    ON FactInternetSales.CustomerKey = DimCustomer.CustomerKey
GROUP BY
    DimCustomer.CustomerKey,
    DimCustomer.FirstName,
    DimCustomer.LastName
ORDER BY TotalSales DESC
"""

df = pd.read_sql(query, loader.engine)

print(df.head())