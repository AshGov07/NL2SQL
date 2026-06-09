from schema_loader import SchemaLoader

from schema_retriever import (
    SchemaRetriever
)

MYSQL_CONFIG = {
    "host": "localhost",
    "database": "sakila",
    "user": "root",
    "password": "Root",
    "port": 3306
}

loader = SchemaLoader(
    host=MYSQL_CONFIG["host"],
    user=MYSQL_CONFIG["user"],
    password=MYSQL_CONFIG["password"],
    database=MYSQL_CONFIG["database"],
    port=MYSQL_CONFIG["port"]
)

schema_df = (
    loader.get_schema_dataframe()
)

print(
    schema_df.columns.tolist()
)

relationship_df = (
    loader.get_relationship_dataframe()
)
# print(
#     relationship_df.to_string()
# )

# print(
#     schema_df.columns.tolist()
# )

table_meta = (
    loader
    .get_table_metadata()
)

print(
    table_meta
)

questions = [

    "Show customer emails",

    "Show films rented by customers",

    "Show actors in films"
]

for question in questions:

    tables = (
        SchemaRetriever
        .retrieve_and_expand(
            question,
            schema_df,
            relationship_df
        )
    )

    # print("\n")
    # print("=" * 50)

    # print(
    #     f"Question: {question}"
    # )

    # print(
    #     f"Expanded Tables: {tables}"
    # )

    print("\n")
    print("=" * 60)
    print("RETRIEVED SCHEMA")
    print("=" * 60)

    print(
        loader.get_schema_context(
            [
                "customer",
                "payment",
                "rental"
            ]
        )
    )