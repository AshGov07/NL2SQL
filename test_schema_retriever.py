from schema_loader import (
    SchemaLoader
)

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

questions = [

    "Show all customers",

    "Show customer emails",

    "Show top rented films",

    "Show revenue by category"
]

for q in questions:

    tables = (
        SchemaRetriever
        .retrieve_tables(
            q,
            schema_df
        )
    )

    print("\n")
    print(q)

    print(
        "Tables:",
        tables
    )