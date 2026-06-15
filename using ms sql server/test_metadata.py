# from schema_loader import SchemaLoader

# loader = SchemaLoader(
#     server="MLS-AI-PC",
#     database="AdventureWorksDW2025"
# )

# df = loader.get_table_metadata()

# print(df.head(20))

# print(df.columns.tolist())


# import schema_loader

# print("Imported from:")
# print(schema_loader.__file__)


# from schema_loader import SchemaLoader

# loader = SchemaLoader(
#     server="MLS-AI-PC",
#     database="AdventureWorksDW2025"
# )

# df = loader.get_schema_dataframe()

# print(df.head())

# print(df.columns.tolist())

# print("Rows:", len(df))



# from schema_loader import SchemaLoader

# loader = SchemaLoader(
#     server="MLS-AI-PC",
#     database="AdventureWorksDW2025"
# )

# schema = loader.get_schema_context()

# print(schema[:3000])






# from schema_loader import SchemaLoader

# loader = SchemaLoader(
#     server="MLS-AI-PC",
#     database="AdventureWorksDW2025"
# )

# print(loader.get_relationship_dataframe())



# from schema_loader import SchemaLoader

# loader = SchemaLoader(
#     server="MLS-AI-PC",
#     database="AdventureWorksDW2025"
# )

# df = loader.get_relationship_dataframe()

# print(df.head(20))

# print(df.columns.tolist())

# print("Rows:", len(df))



from schema_loader import SchemaLoader
from relationship_path_finder import RelationshipPathFinder

loader = SchemaLoader(
    server="MLS-AI-PC",
    database="AdventureWorksDW2025"
)

relationship_df = loader.get_relationship_dataframe()

print(
    relationship_df[
        relationship_df["TABLE_NAME"]
        .str.lower()
        .eq("dimproductsubcategory")
    ]
)