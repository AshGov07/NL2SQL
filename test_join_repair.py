from schema_loader import SchemaLoader

from join_repair_suggester import (
    JoinRepairSuggester
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

relationship_df = (
    loader.get_relationship_dataframe()
)

print("\nPATH")

print(
    JoinRepairSuggester.suggest_path(
        "inventory",
        "film_category",
        relationship_df
    )
)

print("\nMISSING TABLES")

print(
    JoinRepairSuggester.suggest_missing_tables(
        "inventory",
        "film_category",
        relationship_df
    )
)