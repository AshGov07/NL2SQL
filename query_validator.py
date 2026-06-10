# # query_validator.py

# import re


# class QueryValidator:

#     @staticmethod
#     def validate(sql, schema_df):

#         sql_lower = sql.lower()

#         tables = set(
#             schema_df["TABLE_NAME"].str.lower()
#         )

#         columns = set(
#             schema_df["COLUMN_NAME"].str.lower()
#         )

#         # -----------------------------
#         # Validate tables
#         # -----------------------------

#         found_tables = re.findall(
#             r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
#             sql_lower
#         )

#         for table in found_tables:

#             if table not in tables:

#                 raise ValueError(
#                     f"Unknown table detected: {table}"
#                 )

#         # -----------------------------
#         # Validate columns
#         # -----------------------------

#         found_columns = re.findall(
#             r'([a-zA-Z_][a-zA-Z0-9_]*)\.',
#             sql
#         )

#         # aliases ignored in v1

#         return True

#         # -----------------------------
#         # Validate columns
#         # -----------------------------

        

#         found_column_candidates = re.findall(
#             r"select\s+(.*?)\s+from",
#             sql_lower,
#             re.DOTALL
#         )

#         if found_column_candidates:

#             select_part = found_column_candidates[0]

#             columns_found = re.findall(
#                 r"[a-zA-Z_][a-zA-Z0-9_]*",
#                 select_part
#             )

#             sql_keywords = {
#                 "select",
#                 "from",
#                 "distinct",
#                 "count",
#                 "sum",
#                 "avg",
#                 "min",
#                 "max",
#                 "as"
#             }

#             for col in columns_found:

#                 if col in sql_keywords:
#                     continue

#                 if col not in columns:

#                     raise ValueError(
#                         f"Unknown column detected: {col}"
#                     )





#version 2 (correctly working after phase 5b)
# query_validator.py

# import re

# class QueryValidator:

#     SQL_KEYWORDS = {
#         "select",
#         "from",
#         "where",
#         "join",
#         "inner",
#         "left",
#         "right",
#         "outer",
#         "on",
#         "group",
#         "by",
#         "order",
#         "having",
#         "limit",
#         "distinct",
#         "count",
#         "sum",
#         "avg",
#         "min",
#         "max",
#         "as",
#         "and",
#         "or",
#         "not",
#         "with",
#         "asc",
#         "desc"
#     }

#     @staticmethod
#     def validate(sql, schema_df):

#         sql_lower = sql.lower()

#         tables = set(
#             schema_df["TABLE_NAME"]
#             .str.lower()
#             .tolist()
#         )

#         columns = set(
#             schema_df["COLUMN_NAME"]
#             .str.lower()
#             .tolist()
#         )

#         # ----------------------------------------
#         # TABLE VALIDATION
#         # ----------------------------------------

#         found_tables = re.findall(
#             r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
#             sql_lower
#         )

#         for table in found_tables:

#             if table not in tables:

#                 raise ValueError(
#                     f"Unknown table detected: {table}"
#                 )

#         print("Table Validation Passed")

#         # ----------------------------------------
#         # COLUMN VALIDATION
#         # ----------------------------------------

#         select_match = re.search(
#             r"select\s+(.*?)\s+from",
#             sql_lower,
#             re.IGNORECASE | re.DOTALL
#         )

#         if select_match:

#             select_part = select_match.group(1)

#             candidate_columns = re.findall(
#                 r"[a-zA-Z_][a-zA-Z0-9_]*",
#                 select_part
#             )

#             for col in candidate_columns:

#                 if col in QueryValidator.SQL_KEYWORDS:
#                     continue

#                 if col not in columns:

#                     raise ValueError(
#                         f"Unknown column detected: {col}"
#                     )

#         print("Column Validation Passed")

#         return True



# query_validator.py

# from test_validator import cte_names
from _plotly_utils import basevalidators
import re
from cte_helper import CTEHelper


class QueryValidator:

    # SQL_KEYWORDS = {
    #     "select",
    #     "from",
    #     "where",
    #     "join",
    #     "inner",
    #     "left",
    #     "right",
    #     "outer",
    #     "on",
    #     "group",
    #     "by",
    #     "order",
    #     "having",
    #     "limit",
    #     "distinct",
    #     "count",
    #     "sum",
    #     "avg",
    #     "min",
    #     "max",
    #     "as",
    #     "and",
    #     "or",
    #     "not",
    #     "with",
    #     "asc",
    #     "desc"
    # }

    SQL_KEYWORDS = {
        "select",
        "from",
        "where",
        "join",
        "inner",
        "left",
        "right",
        "outer",
        "on",
        "group",
        "by",
        "order",
        "having",
        "limit",
        "distinct",
        "count",
        "sum",
        "avg",
        "min",
        "max",
        "as",
        "and",
        "or",
        "not",
        "is",
        "null",
        "with",
        "asc",
        "desc",
        "between",
        "like",
        "in",
        "exists",
        "month",
        "day",
        "year",
        "hour",
        "minute",
        "second",
        "interval",
        "date_add",
        "date_sub",
        "date_format",
        "curdate",
        "current_date",
        "now",
        "lag",
        "lead",
        "over",
        "partition",
        "row_number",
        "rank",
        "dense_rank",
        "case",
        "when",
        "then",
        "else",
        "end",

        "union",
        "all",

        "cross",

        "cast",
        "convert",

        "if",
        "ifnull",
        "coalesce",

        "true",
        "false",
        "concat",
        "round",
        "upper",
        "lower",
        "lag",
        "lead",
        "date_format"
    }

    #old version

    # @staticmethod
    # def validate_tables(sql_lower, tables):

    #     found_tables = re.findall(
    #         r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
    #         sql_lower
    #     )

    #     for table in found_tables:

    #         if table not in tables:

    #             raise ValueError(
    #                 f"Unknown table detected: {table}"
    #             )

    #     print("Table Validation Passed")



    @staticmethod
    def validate_tables(
        sql_lower,
        tables,
        cte_names=None
    ):
        print("ENTERED validate_tables")
        if cte_names is None:
            cte_names = set()

        found_tables = re.findall(
            r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            sql_lower
        )

        # ----------------------------- debugging -----------------------------
        cte_names = CTEHelper.extract_cte_names(
            sql_lower
        )

        print(
            "Found Tables:",
            found_tables
        )

        print(
            "CTE Tables:",
            cte_names
        )        
        # -------------------------------------------------

        for table in found_tables:

            # -----------------------------
            # Real schema table
            # -----------------------------

            if table in tables:
                continue

            # -----------------------------
            # CTE
            # WITH revenue AS (...)
            # SELECT * FROM revenue
            # -----------------------------

            if table in cte_names:
                continue

            raise ValueError(
                f"Unknown table detected: {table}"
            )

        print("Table Validation Passed")

    # @staticmethod
    # def validate_columns(
    #     sql,
    #     sql_lower,
    #     columns
    # ):

    #     select_match = re.search(
    #         r"select\s+(.*?)\s+from",
    #         sql_lower,
    #         re.IGNORECASE | re.DOTALL
    #     )

    #     if not select_match:
    #         return

    #     select_part = select_match.group(1)

    #     candidate_columns = re.findall(
    #         r"[a-zA-Z_][a-zA-Z0-9_]*",
    #         select_part
    #     )

    #     for col in candidate_columns:

    #         if col in QueryValidator.SQL_KEYWORDS:
    #             continue

    #         if col not in columns:

    #             raise ValueError(
    #                 f"Unknown column detected: {col}"
    #             )

    #     print("Column Validation Passed")

    # @staticmethod
    # def validate_columns(
    #     sql,
    #     sql_lower,
    #     columns
    # ):

    #     select_match = re.search(
    #         r"select\s+(.*?)\s+from",
    #         sql_lower,
    #         re.IGNORECASE | re.DOTALL
    #     )

    #     if not select_match:
    #         return

    #     select_part = select_match.group(1)

    #     candidate_columns = re.findall(
    #         r"[a-zA-Z_][a-zA-Z0-9_]*",
    #         select_part
    #     )

    #     # ----------------------------------
    #     # Skip qualified references
    #     # customer.customer_id
    #     # payment.amount
    #     # c.first_name
    #     # ----------------------------------

    #     qualified_columns = re.findall(
    #         r"(\w+)\.(\w+)",
    #         select_part
    #     )

    #     qualified_parts = set()

    #     for left_part, right_part in qualified_columns:

    #         qualified_parts.add(
    #             left_part.lower()
    #         )

    #         qualified_parts.add(
    #             right_part.lower()
    #         )
    
    #     for col in candidate_columns:

    #         col_lower = col.lower()

    #         # Skip SQL keywords

    #         if col_lower in QueryValidator.SQL_KEYWORDS:
    #             continue

    #         # Skip qualified references
    #         # These are validated separately by
    #         # validate_qualified_columns()

    #         if col_lower in qualified_parts:
    #             continue

    #         if col_lower not in columns:

    #             raise ValueError(
    #                 f"Unknown column detected: {col}"
    #             )

    #     print("Column Validation Passed")

    @staticmethod
    def validate_columns(
        sql,
        sql_lower,
        columns
    ):

        select_match = re.search(
            r"select\s+(.*?)\s+from",
            sql_lower,
            re.IGNORECASE | re.DOTALL
        )

        if not select_match:
            return

        select_part = select_match.group(1)

        candidate_columns = re.findall(
            r"[a-zA-Z_][a-zA-Z0-9_]*",
            select_part
        )

        # ----------------------------------
        # Qualified references
        # customer.customer_id
        # payment.amount
        # c.first_name
        # ----------------------------------

        # qualified_columns = re.findall(
        #     r"(\w+)\.(\w+)",
        #     select_part
        # )
        qualified_columns = re.findall(
            r'([a-zA-Z_][a-zA-Z0-9_]*)\.([a-zA-Z_][a-zA-Z0-9_]*)',
            sql
        )
        qualified_parts = set()

        for left_part, right_part in qualified_columns:

            qualified_parts.add(
                left_part.lower()
            )

            qualified_parts.add(
                right_part.lower()
            )

        # ----------------------------------
        # Column aliases
        # SUM(amount) AS total_revenue
        # MONTH(date) AS month_number
        # ----------------------------------

        alias_matches = re.findall(
            r"\bas\s+([a-zA-Z_][a-zA-Z0-9_]*)",
            select_part,
            re.IGNORECASE
        )

        aliases = {
            alias.lower()
            for alias in alias_matches
        }

        # ----------------------------------
        # SQL functions
        # ----------------------------------

        function_names = {
            "sum",
            "avg",
            "count",
            "min",
            "max",
            "date_format",
            "month",
            "year",
            "concat",
            "lag",
            "round",
            "coalesce",
            "upper",
            "lower",
            "distinct"
        }

        for col in candidate_columns:

            col_lower = col.lower()

            # SQL keywords

            if col_lower in QueryValidator.SQL_KEYWORDS:
                continue

            # SQL functions

            if col_lower in function_names:
                continue

            # Aliases

            if col_lower in aliases:
                continue

            # Qualified references
            # customer.customer_id
            # payment.amount

            if col_lower in qualified_parts:
                continue

            if col_lower not in columns:

                raise ValueError(
                    f"Unknown column detected: {col}"
                )

        print("Column Validation Passed")



    @staticmethod
    def validate(sql, schema_df,relationship_df):
        print("START validate")
        sql_lower = sql.lower()

        tables = set(
            schema_df["TABLE_NAME"]
            .str.lower()
            .tolist()
        )

        columns = set(
            schema_df["COLUMN_NAME"]
            .str.lower()
            .tolist()
        )
         #new update
        cte_names = CTEHelper.extract_cte_names(sql_lower)
        print("CTE Names:", cte_names)
        print("CALLING validate_tables")
        QueryValidator.validate_tables(
            sql_lower,
            tables,
            cte_names    #new change
        )
        
        aliases = QueryValidator.extract_aliases(sql_lower)

       
        # print("Aliases:", aliases)

        if len(aliases) == 0:

            QueryValidator.validate_columns(
                sql,
                sql_lower,
                columns
            )
        # QueryValidator.validate_columns(
        #     sql,
        #     sql_lower,
        #     columns
        # )

        

        QueryValidator.validate_qualified_columns(
            sql,
            aliases,
            schema_df
        )
        QueryValidator.validate_joins(
            sql,
            aliases,
            relationship_df,
            schema_df
        )
        return True
    
    # @staticmethod
    # def extract_aliases(sql_lower):

    #     aliases = {}

    #     matches = re.findall(
    #         r'(?:from|join)\s+(\w+)\s+(\w+)',
    #         sql_lower
    #     )

    #     for table, alias in matches:

    #         aliases[alias] = table

    #     return aliases


# OLD ALIASES EXTRACTOR (before last update)

    # @staticmethod
    # def extract_aliases(sql_lower):

    #     aliases = {}

    #     # sql_keywords = {
    #     #     "where",
    #     #     "group",
    #     #     "order",
    #     #     "having",
    #     #     "limit",
    #     #     "join",
    #     #     "inner",
    #     #     "left",
    #     #     "right",
    #     #     "outer",
    #     #     "on",
    #     #     "and",
    #     #     "or",
    #     #     "not",
    #     #     "by",
    #     #     "asc",
    #     #     "desc"
    #     # }

    #     matches = re.findall(
    #         r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)'
    #         r'(?:\s+([a-zA-Z_][a-zA-Z0-9_]*))?',
    #         sql_lower,
    #         re.IGNORECASE
    #     )

    #     for table_name, alias in matches:

    #         if not alias:
    #             continue

    #         if alias.lower() in QueryValidator.SQL_KEYWORDS:
    #             continue

    #         aliases[alias.lower()] = table_name.lower()

    #     print("Aliases:", aliases)

    #     return aliases
    



    @staticmethod
    def extract_aliases(sql_lower):

        aliases = {}

        # ----------------------------------
        # Normal aliases
        #
        # FROM customer c
        # JOIN payment p
        # ----------------------------------

        normal_matches = re.findall(
            r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)'
            r'(?:\s+([a-zA-Z_][a-zA-Z0-9_]*))?',
            sql_lower,
            re.IGNORECASE
        )

        for table_name, alias in normal_matches:

            if not alias:
                continue

            if alias.lower() in QueryValidator.SQL_KEYWORDS:
                continue

            aliases[alias.lower()] = table_name.lower()

        # ----------------------------------
        # Derived table aliases
        #
        # JOIN (
        #    SELECT ...
        # ) fr
        #
        # FROM (
        #    SELECT ...
        # ) cr
        # ----------------------------------

        derived_matches = re.findall(
            r'\)\s+(?:as\s+)?([a-zA-Z_][a-zA-Z0-9_]*)',
            sql_lower,
            re.IGNORECASE
        )

        for alias in derived_matches:

            if alias.lower() in QueryValidator.SQL_KEYWORDS:
                continue

            aliases[alias.lower()] = "__derived__"

        print("Aliases:", aliases)

        return aliases






    # @staticmethod
    # def validate_qualified_columns(
    #     sql,
    #     aliases,
    #     schema_df
    # ):  

    #     qualified_columns = re.findall(
    #         r'(\w+)\.(\w+)',
    #         sql
    #     )

    #     for alias, column in qualified_columns:

    #         alias = alias.lower()
    #         column = column.lower()

    #         if alias not in aliases:

    #             raise ValueError(
    #                 f"Unknown alias detected: {alias}"
    #             )

    #         table = aliases[alias]

    #         exists = (
    #             (
    #                 schema_df["TABLE_NAME"]
    #                 .str.lower() == table
    #             )
    #             &
    #             (
    #                 schema_df["COLUMN_NAME"]
    #                 .str.lower() == column
    #             )
    #         ).any()

    #         if not exists:

    #             raise ValueError(
    #                 f"Unknown column {table}.{column}"
    #             )

    #     print("Qualified Column Validation Passed")


    @staticmethod
    def validate_qualified_columns(
        sql,
        aliases,
        schema_df
    ):

        # qualified_columns = re.findall(
        #     r'(\w+)\.(\w+)',
        #     sql
        # )

        qualified_columns = re.findall(
            r'([a-zA-Z_][a-zA-Z0-9_]*)\.([a-zA-Z_][a-zA-Z0-9_]*)'   ,
            sql
        )

        from cte_helper import CTEHelper

        cte_names = CTEHelper.extract_cte_names(
            sql
        )

        tables = set(
            schema_df["TABLE_NAME"]
            .str.lower()
            .tolist()
        )

        for alias, column in qualified_columns:

            alias = alias.lower()
            column = column.lower()

            if alias in cte_names:
                continue
            # ----------------------------------
            # Alias reference
            # Example:
            # c.customer_id
            # ----------------------------------

            #old last working regex 

            # if alias in aliases:

            #     table = aliases[alias]

            # # ----------------------------------
            # # Direct table reference
            # # Example:
            # # customer.customer_id
            # # ----------------------------------

            # elif alias in tables:

            #     table = alias

            # else:

            #     raise ValueError(
            #         f"Unknown alias detected: {alias}"
            #     )


            #new update

            if alias in aliases:

                table = aliases[alias]

                # ----------------------------------
                # Derived table alias
                #
                # JOIN (
                #    SELECT ...
                # ) r
                # ----------------------------------

                if table == "__derived__":
                    continue

            elif alias in tables:

                table = alias

            else:

                raise ValueError(
                    f"Unknown alias detected: {alias}"
                )

            exists = (
                (
                    schema_df["TABLE_NAME"]
                    .str.lower() == table
                )
                &
                (
                    schema_df["COLUMN_NAME"]
                    .str.lower() == column
                )
            ).any()

            if not exists:

                raise ValueError(
                    f"Unknown column {table}.{column}"
                )

        print("Qualified Column Validation Passed")
    
    # @staticmethod
    # def validate_joins(sql,aliases,relationship_df):
    #     join_conditions = re.findall(
    #         r'(\w+)\.(\w+)\s*=\s*(\w+)\.(\w+)',
    #         sql,
    #         re.IGNORECASE
    #     )

    #     for left_alias, left_col, right_alias, right_col in join_conditions:

    #         left_alias = left_alias.lower()
    #         right_alias = right_alias.lower()

    #         left_col = left_col.lower()
    #         right_col = right_col.lower()

    #         if left_alias not in aliases:
    #             raise ValueError(
    #                 f"Unknown alias: {left_alias}"
    #             )

    #         if right_alias not in aliases:
    #             raise ValueError(
    #                 f"Unknown alias: {right_alias}"
    #             )

    #         left_table = aliases[left_alias]
    #         right_table = aliases[right_alias]

    #         valid = False

    #         for _, row in relationship_df.iterrows():

    #             table_name = row["TABLE_NAME"].lower()
    #             column_name = row["COLUMN_NAME"].lower()

    #             ref_table = row[
    #                 "REFERENCED_TABLE_NAME"
    #             ].lower()

    #             ref_column = row[
    #                 "REFERENCED_COLUMN_NAME"
    #             ].lower()

    #             forward_match = (
    #                 table_name == left_table
    #                 and column_name == left_col
    #                 and ref_table == right_table
    #                 and ref_column == right_col
    #             )

    #             reverse_match = (
    #                 table_name == right_table
    #                 and column_name == right_col
    #                 and ref_table == left_table
    #                 and ref_column == left_col
    #             )

    #             if forward_match or reverse_match:

    #                 valid = True
    #                 break

    #         if not valid:

    #             raise ValueError(
    #                 f"Invalid join detected: "
    #                 f"{left_table}.{left_col} = "
    #                 f"{right_table}.{right_col}"
    #             )

    #     print("Join Validation Passed")



    @staticmethod
    def validate_joins(
        sql,
        aliases,
        relationship_df,
        schema_df
    ):

        join_conditions = re.findall(
            r'(\w+)\.(\w+)\s*=\s*(\w+)\.(\w+)',
            sql,
            re.IGNORECASE
        )

        tables = set(
            schema_df["TABLE_NAME"]
            .str.lower()
            .tolist()
        )

        for left_alias, left_col, right_alias, right_col in join_conditions:

            left_alias = left_alias.lower()
            right_alias = right_alias.lower()

            left_col = left_col.lower()
            right_col = right_col.lower()

            # ----------------------------------
            # Resolve left side
            # ----------------------------------

            if left_alias in aliases:

                left_table = aliases[left_alias]

                # Derived table new update
                if left_table == "__derived__":
                    continue

            elif left_alias in tables:

                left_table = left_alias

            else:

                raise ValueError(
                    f"Unknown alias: {left_alias}"
                )

            # ----------------------------------
            # Resolve right side
            # ----------------------------------

            if right_alias in aliases:

                right_table = aliases[right_alias]
                
                # Derived table new update
                if right_table == "__derived__":
                    continue

            elif right_alias in tables:

                right_table = right_alias

            else:

                raise ValueError(
                    f"Unknown alias: {right_alias}"
                )

            valid = False

            for _, row in relationship_df.iterrows():

                table_name = row[
                    "TABLE_NAME"
                ].lower()

                column_name = row[
                    "COLUMN_NAME"
                ].lower()

                ref_table = row[
                    "REFERENCED_TABLE_NAME"
                ].lower()

                ref_column = row[
                    "REFERENCED_COLUMN_NAME"
                ].lower()

                forward_match = (
                    table_name == left_table
                    and column_name == left_col
                    and ref_table == right_table
                    and ref_column == right_col
                )

                reverse_match = (
                    table_name == right_table
                    and column_name == right_col
                    and ref_table == left_table
                    and ref_column == left_col
                )

                if forward_match or reverse_match:

                    valid = True
                    break

            if not valid:

                # raise ValueError(
                #     f"Invalid join detected: "
                #     f"{left_table}.{left_col} = "
                #     f"{right_table}.{right_col}"
                # )




                from relationship_path_finder import (RelationshipPathFinder)

                suggestion = (
                    RelationshipPathFinder
                    .explain_invalid_join(
                        left_table,
                        right_table,
                        relationship_df
                    )
                )

                raise ValueError(
                    f"Invalid join detected: "
                    f"{left_table}.{left_col} = "
                    f"{right_table}.{right_col}\n"
                    f"{suggestion}"
                )

        print("Join Validation Passed")