# # # sql_repair.py

# # import difflib


# # class SQLRepair:

# #     @staticmethod
# #     def closest_match(name, candidates):

# #         matches = difflib.get_close_matches(
# #             name.lower(),
# #             [c.lower() for c in candidates],
# #             n=1,
# #             cutoff=0.6
# #         )

# #         if matches:
# #             return matches[0]

# #         return None




# #phase 6A.1

# import re
# import difflib


# class SQLRepair:

#     @staticmethod
#     def closest_match(name, candidates):

#         matches = difflib.get_close_matches(
#             name.lower(),
#             [c.lower() for c in candidates],
#             n=1,
#             cutoff=0.6
#         )

#         if matches:
#             return matches[0]

#         return None

#     @staticmethod
#     def repair_table_names(sql, valid_tables):

#         repaired_sql = sql

#         found_tables = re.findall(
#             r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
#             sql,
#             re.IGNORECASE
#         )

#         for table in found_tables:

#             if table.lower() not in [
#                 t.lower()
#                 for t in valid_tables
#             ]:

#                 replacement = SQLRepair.closest_match(
#                     table,
#                     valid_tables
#                 )

#                 if replacement:

#                     repaired_sql = re.sub(
#                         rf'\b{table}\b',
#                         replacement,
#                         repaired_sql,
#                         flags=re.IGNORECASE
#                     )

#         return repaired_sql
    
#     @staticmethod
#     def repair_column_name(
#         column_name,
#         valid_columns
#     ):

#         return SQLRepair.closest_match(
#         column_name,
#         valid_columns
#     )



#     # @staticmethod
#     # def repair_column_references(
#     #     sql,
#     #     valid_columns
#     # ):

#     #     repaired_sql = sql

#     #     tokens = re.findall(
#     #         r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
#     #         sql
#     #     )

#     #     sql_keywords = {
#     #         "select",
#     #         "from",
#     #         "join",
#     #         "where",
#     #         "group",
#     #         "by",
#     #         "order",
#     #         "having",
#     #         "limit",
#     #         "and",
#     #         "or",
#     #         "on",
#     #         "as",
#     #         "sum",
#     #         "count",
#     #         "avg",
#     #         "min",
#     #         "max",
#     #         "distinct"
#     #     }

#     #     for token in tokens:

#     #         token_lower = token.lower()

#     #         if token_lower in sql_keywords:
#     #             continue

#     #         if token_lower in [
#     #             c.lower()
#     #             for c in valid_columns
#     #         ]:
#     #             continue

#     #         replacement = SQLRepair.closest_match(
#     #             token,
#     #             valid_columns
#     #         )

#     #         if replacement:

#     #             repaired_sql = re.sub(
#     #                 rf'\b{token}\b',
#     #                 replacement,
#     #                 repaired_sql,
#     #                 flags=re.IGNORECASE
#     #             )

#     #     return repaired_sql


#     @staticmethod
#     def repair_column_references(
#         sql,
#         valid_columns
#     ):

#         repaired_sql = sql

#         # ----------------------------------
#         # Extract table names from SQL
#         # ----------------------------------

#         found_tables = re.findall(
#             r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
#             sql,
#             re.IGNORECASE
#         )

#         table_names = {
#             table.lower()
#             for table in found_tables
#         }

#         # ----------------------------------
#         # SQL keywords
#         # ----------------------------------

#         sql_keywords = {
#             "select",
#             "from",
#             "join",
#             "where",
#             "group",
#             "by",
#             "order",
#             "having",
#             "limit",
#             "and",
#             "or",
#             "on",
#             "as",
#             "sum",
#             "count",
#             "avg",
#             "min",
#             "max",
#             "distinct"
#         }

#         # ----------------------------------
#         # Find all word tokens
#         # ----------------------------------

#         tokens = re.findall(
#             r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
#             sql
#         )

#         valid_columns_lower = {
#             c.lower()
#             for c in valid_columns
#         }

#         for token in tokens:

#             token_lower = token.lower()

#             # Skip SQL keywords

#             if token_lower in sql_keywords:
#                 continue

#             # Skip table names

#             if token_lower in table_names:
#                 continue

#             # Skip already-valid columns

#             if token_lower in valid_columns_lower:
#                 continue

#             replacement = SQLRepair.closest_match(
#                 token,
#                 valid_columns
#             )

#             if replacement:

#                 repaired_sql = re.sub(
#                     rf'\b{re.escape(token)}\b',
#                     replacement,
#                     repaired_sql,
#                     flags=re.IGNORECASE
#                 )

#         return repaired_sql
    
    



# sql_repair.py

from _plotly_utils.colors import sequential
from query_validator import QueryValidator
import re
import difflib
from cte_helper import CTEHelper

class SQLRepair:

    @staticmethod
    def closest_match(
        name,
        candidates
    ):

        matches = difflib.get_close_matches(
            name.lower(),
            [c.lower() for c in candidates],
            n=1,
            cutoff=0.6
        )

        if matches:
            return matches[0]

        return None

    @staticmethod
    def repair_table_names(
        sql,
        valid_tables
    ):

        repaired_sql = sql

        cte_names = CTEHelper.extract_cte_names(sql)

        cte_names = {
            cte.lower()
            for cte in cte_names
        }
        found_tables = re.findall(
            r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            sql,
            re.IGNORECASE
        )

        valid_tables_lower = {
            t.lower()
            for t in valid_tables
        }

        for table in found_tables:
            if table.lower() in cte_names:
                continue    

            if table.lower() not in valid_tables_lower:

                replacement = SQLRepair.closest_match(
                    table,
                    valid_tables
                )

                if replacement:

                    repaired_sql = re.sub(
                        rf'\b{re.escape(table)}\b',
                        replacement,
                        repaired_sql,
                        flags=re.IGNORECASE
                    )

        return repaired_sql

    @staticmethod
    def repair_column_name(
        column_name,
        valid_columns
    ):

        return SQLRepair.closest_match(
            column_name,
            valid_columns
        )

    @staticmethod
    def repair_column_references(
        sql,
        valid_columns
    ):

        repaired_sql = sql

        # ----------------------------------
        # Extract tables already present
        # ----------------------------------

        found_tables = re.findall(
            r'(?:from|join)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            sql,
            re.IGNORECASE
        )

        table_names = {
            t.lower()
            for t in found_tables
        }
        cte_names = CTEHelper.extract_cte_names(sql)

        cte_names = {
            cte.lower()
            for cte in cte_names
        }
        
        aliases = QueryValidator.extract_aliases(sql.lower())

        alias_names = set(aliases.keys())


        # ----------------------------------
        # Qualified references
        # Example:
        # f.title
        # c.customer_id
        # rental.rental_id
        # ----------------------------------

        qualified_columns = re.findall(
            # r'(\w+)\.(\w+)',
            r'([a-zA-Z_][a-zA-Z0-9_]*)\.([a-zA-Z_][a-zA-Z0-9_]*)',
            sql
        )

        # qualified_parts = set()

        # for left, right in qualified_columns:

        #     qualified_parts.add(
        #         left.lower()
        #     )

        #     qualified_parts.add(
        #         right.lower()
        #     )

        qualified_aliases = {left.lower() for left, right in qualified_columns}
        
        # ----------------------------------
        # SQL keywords
        # ----------------------------------

        # sql_keywords = {
        #     "select",
        #     "from",
        #     "join",
        #     "where",
        #     "group",
        #     "by",
        #     "order",
        #     "having",
        #     "limit",
        #     "and",
        #     "or",
        #     "on",
        #     "as",
        #     "sum",
        #     "count",
        #     "avg",
        #     "min",
        #     "max",
        #     "distinct",
        #     "with",
        #     "inner",
        #     "left",
        #     "right",
        #     "outer",
        #     "asc",
        #     "desc"
        # }
        # sql_keywords = {
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
        #     "is",
        #     "null",
        #     "with",
        #     "asc",
        #     "desc",
        #     "between",
        #     "like",
        #     "in",
        #     "exists"
        # }


        valid_columns_lower = {
            c.lower()
            for c in valid_columns
        }

        tokens = re.findall(
            r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
            sql
        )
        print("Repair Tokens:", tokens)
        for token in tokens:

            token_lower = token.lower()
            if token_lower in cte_names:
                continue    
            # Skip aliases

            if token_lower in alias_names:
                continue

            if token_lower in qualified_aliases:
                continue

            # Skip SQL keywords

            if token_lower in QueryValidator.SQL_KEYWORDS:
                continue

            # Skip table names

            if token_lower in table_names:
                continue

            # Skip valid columns

            if token_lower in valid_columns_lower:
                continue

            replacement = SQLRepair.closest_match(
                token,
                valid_columns
            )

            if replacement:

                repaired_sql = re.sub(
                    rf'\b{re.escape(token)}\b',
                    replacement,
                    repaired_sql,
                    flags=re.IGNORECASE
                )

        return repaired_sql

    @staticmethod
    def repair_sql(
        sql,
        valid_tables,
        valid_columns
    ):

        repaired_sql = SQLRepair.repair_table_names(
            sql,
            valid_tables
        )

        repaired_sql = SQLRepair.repair_column_references(
            repaired_sql,
            valid_columns
        )

        return repaired_sql