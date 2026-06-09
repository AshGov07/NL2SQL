from relationship_path_finder import (
    RelationshipPathFinder
)


class JoinRepairSuggester:

    @staticmethod
    def suggest_path(
        left_table,
        right_table,
        relationship_df
    ):

        path = (
            RelationshipPathFinder.find_path(
                left_table,
                right_table,
                relationship_df
            )
        )

        if not path:

            return (
                f"No relationship path exists "
                f"between {left_table} "
                f"and {right_table}"
            )

        return (
            " -> ".join(path)
        )

    @staticmethod
    def suggest_missing_tables(
        left_table,
        right_table,
        relationship_df
    ):

        missing_tables = (
            RelationshipPathFinder
            .find_missing_relationships(
                left_table,
                right_table,
                relationship_df
            )
        )

        return missing_tables