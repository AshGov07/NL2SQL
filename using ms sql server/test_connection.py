# # test_connection.py

# from sqlalchemy import create_engine
# import pandas as pd

# engine = create_engine(
#     "mssql+pyodbc://MLS-AI-PC/AdventureWorksDW2025"
#     "?driver=ODBC+Driver+17+for+SQL+Server"
#     "&trusted_connection=yes"
# )

# query = """
# SELECT TOP 5 *
# FROM DimCustomer
# """

# df = pd.read_sql(
#     query,
#     engine
# )

# print(df.head())
# print()
# print(df.columns.tolist())


from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mssql+pyodbc://MLS-AI-PC/AdventureWorksDW2025"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

df = pd.read_sql(
    "SELECT TOP 5 * FROM DimCustomer",
    engine
)

print(df.head())
print(df.columns.tolist())