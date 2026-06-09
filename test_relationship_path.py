from schema_loader import SchemaLoader
from relationship_path_finder import (
    RelationshipPathFinder
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
print(
    relationship_df.to_string()
)
print(
    RelationshipPathFinder
    .expand_two_hops(
        ["film"],
        relationship_df
    )
)