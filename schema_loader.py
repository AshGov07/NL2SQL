# from vanna.integrations.mysql import MySQLRunner
# import pandas as pd


# class SchemaLoader:

#     def __init__(self, runner):
#         self.runner = runner

#     def get_schema_context(self):

#         query = """
#         SELECT
#             TABLE_NAME,
#             COLUMN_NAME,
#             DATA_TYPE
#         FROM INFORMATION_SCHEMA.COLUMNS
#         WHERE TABLE_SCHEMA = DATABASE()
#         ORDER BY TABLE_NAME, ORDINAL_POSITION;
#         """

#         import pymysql

#         conn = pymysql.connect(
#             host=self.runner.host,
#             user=self.runner.user,
#             password=self.runner.password,
#             database=self.runner.database,
#             port=self.runner.port
#         )

#         df = pd.read_sql(query, conn)

#         schema_text = []

#         current_table = None

#         for _, row in df.iterrows():

#             table = row["TABLE_NAME"]

#             if table != current_table:

#                 current_table = table

#                 schema_text.append(f"\n{table}")
#                 schema_text.append("-" * len(table))

#             schema_text.append(
#                 f"{row['COLUMN_NAME']} ({row['DATA_TYPE']})"
#             )

#         conn.close()

#         return "\n".join(schema_text)






















# schema_loader.py ( good working before sqlalchemy)

# import pandas as pd
# import pymysql


# class SchemaLoader:

#     def __init__(
#         self,
#         host,
#         user,
#         password,
#         database,
#         port=3306
#     ):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.port = port

#     # def get_schema_context(self):

#     #     query = """
#     #     SELECT
#     #         TABLE_NAME,
#     #         COLUMN_NAME,
#     #         DATA_TYPE
#     #     FROM INFORMATION_SCHEMA.COLUMNS
#     #     WHERE TABLE_SCHEMA = DATABASE()
#     #     ORDER BY TABLE_NAME, ORDINAL_POSITION;
#     #     """

#     #     conn = pymysql.connect(
#     #         host=self.host,
#     #         user=self.user,
#     #         password=self.password,
#     #         database=self.database,
#     #         port=self.port
#     #     )

#     #     df = pd.read_sql(query, conn)

#     #     schema_text = []

#     #     current_table = None

#     #     for _, row in df.iterrows():

#     #         table = row["TABLE_NAME"]

#     #         if table != current_table:

#     #             current_table = table

#     #             schema_text.append("\n")
#     #             schema_text.append(table)
#     #             schema_text.append("-" * len(table))

#     #         schema_text.append(
#     #             f"{row['COLUMN_NAME']} ({row['DATA_TYPE']})"
#     #         )

#     #     conn.close()

#     #     return "\n".join(schema_text)

#     def get_schema_context(
#     self,
#     selected_tables=None
# ):

#         query = """
#         SELECT
#             TABLE_NAME,
#             COLUMN_NAME,
#             DATA_TYPE
#         FROM INFORMATION_SCHEMA.COLUMNS
#         WHERE TABLE_SCHEMA = DATABASE()
#         ORDER BY TABLE_NAME, ORDINAL_POSITION;
#         """

#         conn = pymysql.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database,
#             port=self.port
#         )

#         df = pd.read_sql(
#             query,
#             conn
#         )

#         # ----------------------------------
#         # Schema Retrieval Filter
#         # ----------------------------------

#         if selected_tables:

#             selected_tables = {
#                 table.lower()
#                 for table in selected_tables
#             }

#             df = df[
#                 df["TABLE_NAME"]
#                 .str.lower()
#                 .isin(selected_tables)
#             ]

#         schema_text = []

#         current_table = None

#         for _, row in df.iterrows():

#             table = row["TABLE_NAME"]

#             if table != current_table:

#                 current_table = table

#                 schema_text.append("\n")
#                 schema_text.append(table)
#                 schema_text.append(
#                     "-" * len(table)
#                 )

#             schema_text.append(
#                 f"{row['COLUMN_NAME']} "
#                 f"({row['DATA_TYPE']})"
#             )

#         conn.close()

#         return "\n".join(
#             schema_text
#         )


#     #phase 3- FK discovery
#     def get_relationships(self):

#         query = """
#         SELECT
#             TABLE_NAME,
#             COLUMN_NAME,
#             REFERENCED_TABLE_NAME,
#             REFERENCED_COLUMN_NAME
#         FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
#         WHERE TABLE_SCHEMA = DATABASE()
#         AND REFERENCED_TABLE_NAME IS NOT NULL
#         ORDER BY TABLE_NAME;
#         """

#         conn = pymysql.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database,
#             port=self.port
#         )

#         df = pd.read_sql(query, conn)

#         conn.close()

#         relationships = []

#         for _, row in df.iterrows():

#             relationships.append(
#                 f"{row['TABLE_NAME']}.{row['COLUMN_NAME']} "
#                 f"-> "
#                 f"{row['REFERENCED_TABLE_NAME']}."
#                 f"{row['REFERENCED_COLUMN_NAME']}"
#             )

#         return "\n".join(relationships) 

#     #phase 5c
#     def get_relationship_dataframe(self):

#         query = """
#         SELECT
#             TABLE_NAME,
#             COLUMN_NAME,
#             REFERENCED_TABLE_NAME,
#             REFERENCED_COLUMN_NAME
#         FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
#         WHERE TABLE_SCHEMA = DATABASE()
#         AND REFERENCED_TABLE_NAME IS NOT NULL;
#         """

#         conn = pymysql.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database,
#             port=self.port
#         )

#         df = pd.read_sql(query, conn)

#         conn.close()

#         return df
    
#     #phase4B automatic business logic

#     def get_schema_dataframe(self):

#         # query = """
#         # SELECT
#         #     TABLE_NAME,
#         #     COLUMN_NAME,
#         #     DATA_TYPE
#         # FROM INFORMATION_SCHEMA.COLUMNS
#         # WHERE TABLE_SCHEMA = DATABASE()
#         # """

#         query = """
#         SELECT
#             c.TABLE_NAME,
#             c.COLUMN_NAME,
#             c.DATA_TYPE,
#             t.TABLE_TYPE
#         FROM INFORMATION_SCHEMA.COLUMNS c
#         JOIN INFORMATION_SCHEMA.TABLES t
#             ON c.TABLE_SCHEMA = t.TABLE_SCHEMA
#             AND c.TABLE_NAME = t.TABLE_NAME
#         WHERE c.TABLE_SCHEMA = DATABASE()
#         """

#         conn = pymysql.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database,
#             port=self.port
#         )

#         df = pd.read_sql(query, conn)

#         conn.close()

#         return df
    


#     def get_table_metadata(self):

#         query = """
#         SELECT
#             TABLE_NAME,
#             TABLE_TYPE
#         FROM INFORMATION_SCHEMA.TABLES
#         WHERE TABLE_SCHEMA = DATABASE()
#         """

#         conn = pymysql.connect(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database,
#             port=self.port
#         )

#         df = pd.read_sql(
#             query,
#             conn
#         )

#         conn.close()

#         return df



from sqlalchemy import create_engine
import pandas as pd
# import pymysql

class SchemaLoader:

    def __init__(
        self,
        host,
        user,
        password,
        database,
        port=3306
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

        self.engine = create_engine(
            f"mysql+pymysql://"
            f"{user}:{password}"
            f"@{host}:{port}"
            f"/{database}"
        )
    


    def get_schema_context(self,selected_tables=None):

        query = """
        SELECT
            TABLE_NAME,
            COLUMN_NAME,
            DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = DATABASE()
        ORDER BY TABLE_NAME, ORDINAL_POSITION;
        """

        df = pd.read_sql(
            query,
            self.engine
        )

        if selected_tables:

            selected_tables = {
                table.lower()
                for table in selected_tables
            }

            df = df[
                df["TABLE_NAME"]
                .str.lower()
                .isin(selected_tables)
            ]

        schema_text = []

        current_table = None

        for _, row in df.iterrows():

            table = row["TABLE_NAME"]

            if table != current_table:

                current_table = table

                schema_text.append("\n")
                schema_text.append(table)
                schema_text.append(
                    "-" * len(table)
                )

            schema_text.append(
                f"{row['COLUMN_NAME']} "
                f"({row['DATA_TYPE']})"
            )

        return "\n".join(schema_text)

    
    def get_relationships(self):

        query = """
        SELECT
            TABLE_NAME,
            COLUMN_NAME,
            REFERENCED_TABLE_NAME,
            REFERENCED_COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE TABLE_SCHEMA = DATABASE()
        AND REFERENCED_TABLE_NAME IS NOT NULL
        ORDER BY TABLE_NAME;
        """

        df = pd.read_sql(
            query,
            self.engine
        )

        relationships = []

        for _, row in df.iterrows():

            relationships.append(
                f"{row['TABLE_NAME']}.{row['COLUMN_NAME']} "
                f"-> "
                f"{row['REFERENCED_TABLE_NAME']}."
                f"{row['REFERENCED_COLUMN_NAME']}"
            )

        return "\n".join(relationships)
    


    def get_relationship_dataframe(self):

        query = """
        SELECT
            TABLE_NAME,
            COLUMN_NAME,
            REFERENCED_TABLE_NAME,
            REFERENCED_COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE TABLE_SCHEMA = DATABASE()
        AND REFERENCED_TABLE_NAME IS NOT NULL;
        """

        df = pd.read_sql(
            query,
            self.engine
        )

        return df
    
    def get_schema_dataframe(self):

        query = """
        SELECT
            c.TABLE_NAME,
            c.COLUMN_NAME,
            c.DATA_TYPE,
            t.TABLE_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS c
        JOIN INFORMATION_SCHEMA.TABLES t
            ON c.TABLE_SCHEMA = t.TABLE_SCHEMA
            AND c.TABLE_NAME = t.TABLE_NAME
        WHERE c.TABLE_SCHEMA = DATABASE()
        """

        df = pd.read_sql(
            query,
            self.engine
        )

        return df
    
    def get_table_metadata(self):

        query = """
        SELECT
            TABLE_NAME,
            TABLE_TYPE
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_SCHEMA = DATABASE()
        """

        df = pd.read_sql(
            query,
            self.engine
        )

        return df