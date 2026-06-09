from collections import deque


class RelationshipPathFinder:

    @staticmethod
    def build_graph(
        relationship_df
    ):

        graph = {}

        for _, row in relationship_df.iterrows():

            table = (
                row["TABLE_NAME"]
                .lower()
            )

            ref_table = (
                row[
                    "REFERENCED_TABLE_NAME"
                ]
                .lower()
            )

            if table not in graph:
                graph[table] = []

            if ref_table not in graph:
                graph[ref_table] = []

            graph[table].append(
                ref_table
            )

            graph[ref_table].append(
                table
            )

        return graph

    @staticmethod
    def expand_tables(
        selected_tables,
        relationship_df
    ):

        selected_tables = [
            table.lower()
            for table in selected_tables
        ]

        expanded = set(
            selected_tables
        )

        if len(selected_tables) < 2:
            return sorted(
                list(expanded)
            )

        for i in range(
            len(selected_tables)
        ):

            for j in range(
                i + 1,
                len(selected_tables)
            ):

                path = (
                    RelationshipPathFinder
                    .find_path(
                        selected_tables[i],
                        selected_tables[j],
                        relationship_df
                    )
                )

                if path:

                    expanded.update(
                        path
                    )

        return sorted(
            list(expanded)
        )


    @staticmethod
    def get_neighbors(
        table_name,
        relationship_df
    ):

        table_name = table_name.lower()

        neighbors = set()

        for _, row in relationship_df.iterrows():

            table = (
                row["TABLE_NAME"]
                .lower()
            )

            ref_table = (
                row["REFERENCED_TABLE_NAME"]
                .lower()
            )

            if table == table_name:

                neighbors.add(
                    ref_table
                )

            elif ref_table == table_name:

                neighbors.add(
                    table
                )

        return sorted(
            list(neighbors)
        )
    @staticmethod
    def expand_two_hops(
        tables,
        relationship_df
    ):

        expanded = set(
            table.lower()
            for table in tables
        )

        current_level = set(expanded)

        # --------------------------
        # Hop 1
        # --------------------------

        next_level = set()

        for table in current_level:

            neighbors = (
                RelationshipPathFinder
                .get_neighbors(
                    table,
                    relationship_df
                )
            )

            next_level.update(
                neighbors
            )

        expanded.update(
            next_level
        )

        # --------------------------
        # Hop 2
        # --------------------------

        second_level = set()

        for table in next_level:

            neighbors = (
                RelationshipPathFinder
                .get_neighbors(
                    table,
                    relationship_df
                )
            )

            second_level.update(
                neighbors
            )

        expanded.update(
            second_level
        )

        return sorted(
            list(expanded)
        )
    @staticmethod
    def expand_one_hop(
        tables,
        relationship_df
    ):

        expanded = set(
            table.lower()
            for table in tables
        )

        for table in tables:

            neighbors = (
                RelationshipPathFinder
                .get_neighbors(
                    table,
                    relationship_df
                )
            )

            expanded.update(
                neighbors
            )

        return sorted(
            list(expanded)
        )


    @staticmethod
    def find_missing_relationships(
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
            return []

        return path[1:-1]
    @staticmethod
    def explain_invalid_join(
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
            "Suggested path: "
            + " -> ".join(path)
        )

    @staticmethod
    def find_path(
        start_table,
        end_table,
        relationship_df
    ):

        start_table = (
            start_table.lower()
        )

        end_table = (
            end_table.lower()
        )

        graph = (
            RelationshipPathFinder
            .build_graph(
                relationship_df
            )
        )

        queue = deque(
            [[start_table]]
        )

        visited = set()

        while queue:

            path = queue.popleft()

            current = path[-1]

            if current == end_table:

                return path

            if current in visited:
                continue

            visited.add(
                current
            )

            for neighbor in graph.get(
                current,
                []
            ):

                new_path = (
                    path +
                    [neighbor]
                )

                queue.append(
                    new_path
                )

        return None