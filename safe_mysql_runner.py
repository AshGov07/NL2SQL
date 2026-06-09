# safe_mysql_runner.py
#working version (before phase 6)
# from vanna.integrations.mysql import MySQLRunner
# from sql_guard import SQLGuard


# class SafeMySQLRunner(MySQLRunner):

#     async def run_sql(self, args, context):

#         SQLGuard.validate(args.sql)

#         return await super().run_sql(args, context)


# safe_mysql_runner.py

# from vanna.integrations.mysql import MySQLRunner

# from sql_guard import SQLGuard
# from query_validator import QueryValidator
# from sql_repair import SQLRepair
# from schema_loader import SchemaLoader


# class SafeMySQLRunner(MySQLRunner):

#     async def run_sql(self, args, context):

#         sql = args.sql

#         # ----------------------------------
#         # Security Validation
#         # ----------------------------------

#         SQLGuard.validate(sql)

#         # ----------------------------------
#         # Load Schema
#         # ----------------------------------

#         loader = SchemaLoader(
#             host=self.host,
#             user=self.user,
#             password=self.password,
#             database=self.database,
#             port=self.port
#         )

#         schema_df = loader.get_schema_dataframe()

#         relationship_df = (
#             loader.get_relationship_dataframe()
#         )

#         valid_tables = (
#             schema_df["TABLE_NAME"]
#             .unique()
#             .tolist()
#         )

#         valid_columns = (
#             schema_df["COLUMN_NAME"]
#             .unique()
#             .tolist()
#         )

#         # ----------------------------------
#         # Validate SQL
#         # ----------------------------------

#         try:

#             QueryValidator.validate(
#                 sql,
#                 schema_df,
#                 relationship_df
#             )

#         except Exception as e:

#             print(
#                 f"Validation Failed: {e}"
#             )

#             repaired_sql = (
#                 SQLRepair.repair_sql(
#                     sql,
#                     valid_tables,
#                     valid_columns
#                 )
#             )

#             print(
#                 "\nAuto Repaired SQL:\n"
#             )
#             print(repaired_sql)

#             QueryValidator.validate(
#                 repaired_sql,
#                 schema_df,
#                 relationship_df
#             )

#             args.sql = repaired_sql

#         # ----------------------------------
#         # Execute
#         # ----------------------------------

#         return await super().run_sql(
#             args,
#             context
#         )



# safe_mysql_runner.py

from vanna.integrations.mysql import MySQLRunner

from sql_guard import SQLGuard
from query_validator import QueryValidator
from sql_repair import SQLRepair
from schema_loader import SchemaLoader


class SafeMySQLRunner(MySQLRunner):

    async def run_sql(self, args, context):

        sql = args.sql

        print("\n" + "=" * 60)
        print("ORIGINAL SQL")
        print("=" * 60)
        print(sql)

        # ----------------------------------
        # Security Validation
        # ----------------------------------

        SQLGuard.validate(sql)

        # ----------------------------------
        # Load Schema Metadata
        # ----------------------------------

        loader = SchemaLoader(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )

        schema_df = loader.get_schema_dataframe()

        relationship_df = (
            loader.get_relationship_dataframe()
        )

        valid_tables = (
            schema_df["TABLE_NAME"]
            .unique()
            .tolist()
        )

        valid_columns = (
            schema_df["COLUMN_NAME"]
            .unique()
            .tolist()
        )

        # ----------------------------------
        # Validate SQL
        # ----------------------------------

        try:

            QueryValidator.validate(
                sql,
                schema_df,
                relationship_df
            )

            print("\nValidation Passed")

        except Exception as e:

            print("\nValidation Failed")
            print(e)

            # ----------------------------------
            # Auto Repair
            # ----------------------------------

            repaired_sql = SQLRepair.repair_sql(
                sql,
                valid_tables,
                valid_columns
            )

            print("\n" + "=" * 60)
            print("AUTO REPAIRED SQL")
            print("=" * 60)
            print(repaired_sql)

            # ----------------------------------
            # Revalidate
            # ----------------------------------

            QueryValidator.validate(
                repaired_sql,
                schema_df,
                relationship_df
            )

            print("\nRepair Validation Passed")

            args.sql = repaired_sql

        # ----------------------------------
        # Execute SQL
        # ----------------------------------

        print("\n" + "=" * 60)
        print("FINAL SQL EXECUTING")
        print("=" * 60)
        print(args.sql)

        return await super().run_sql(
            args,
            context
        )