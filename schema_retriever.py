import re
from relationship_path_finder import (
    RelationshipPathFinder
)

class SchemaRetriever:


    @staticmethod
    def retrieve_and_expand(
        question,
        schema_df,
        relationship_df
    ):

        selected_tables = (
            SchemaRetriever
            .retrieve_tables(
                question,
                schema_df
            )
        )

        expanded_tables = (
            RelationshipPathFinder
            .expand_tables(
                selected_tables,
                relationship_df
            )
        )

        return expanded_tables




    @staticmethod
    def retrieve_tables(
        question,
        schema_df
    ):

        question = question.lower()

        selected_tables = set()

        # table_names = (
        #     schema_df["TABLE_NAME"]
        #     .str.lower()
        #     .unique()
        #     .tolist()
        # )
        table_names = (
            schema_df[
                schema_df["TABLE_TYPE"]
                == "BASE TABLE"
            ]["TABLE_NAME"]
            .str.lower()
            .unique()
            .tolist()
        )
        # column_names = (
        #     schema_df[
        #         ["TABLE_NAME", "COLUMN_NAME"]
        #     ]
        #     .values
        # )

        column_names = (
            schema_df[
                schema_df["TABLE_TYPE"]
                == "BASE TABLE"
            ][
                ["TABLE_NAME", "COLUMN_NAME"]
            ]
            .values
        )

        # ----------------------------------
        # Match table names
        # ----------------------------------

        for table in table_names:

            if table in question:

                selected_tables.add(
                    table
                )

        # ----------------------------------
        # Match column names
        # ----------------------------------

        tokens = set(
            re.findall(
                r"\w+",
                question
            )
        )

        for table, column in column_names:

            if (
                column.lower()
                in tokens
            ):

                selected_tables.add(
                    table.lower()
                )

        return sorted(
            list(selected_tables)
        )