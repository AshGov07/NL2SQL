# # metric_discovery.py

# class MetricDiscovery:

#     REVENUE_COLUMNS = {
#         "price",
#         "priceeach",
#         "unitprice",
#         "amount",
#         "revenue",
#         "totalamount"
#     }

#     QUANTITY_COLUMNS = {
#         "quantity",
#         "quantityordered",
#         "qty"
#     }

#     CUSTOMER_COLUMNS = {
#         "customerid",
#         "customernumber"
#     }

#     ORDER_COLUMNS = {
#         "ordernumber",
#         "orderid"
#     }

#     @staticmethod
#     def generate(schema_df):

#         metrics = []

#         for table_name, group in schema_df.groupby("TABLE_NAME"):

#             columns = {
#                 c.lower()
#                 for c in group["COLUMN_NAME"].tolist()
#             }

#             # Revenue Discovery

#             quantity_col = None
#             price_col = None

#             for col in columns:

#                 if col in MetricDiscovery.QUANTITY_COLUMNS:
#                     quantity_col = col

#                 if col in MetricDiscovery.REVENUE_COLUMNS:
#                     price_col = col

#             if quantity_col and price_col:

#                 metrics.append(
#                     f"""
# Revenue =
# SUM({table_name}.{quantity_col} *
# {table_name}.{price_col})
# """
#                 )

#             # Payment Discovery

#             if "amount" in columns:

#                 metrics.append(
#                     f"""
# Total Amount =
# SUM({table_name}.amount)
# """
#                 )

#             # Customer Count

#             if (
#                 "customernumber" in columns
#                 or
#                 "customerid" in columns
#             ):
#                 metrics.append(
#                     f"""
# Customer Count =
# COUNT(DISTINCT
# {table_name}.customerNumber)
# """
#                 )

#             # Order Count

#             if (
#                 "ordernumber" in columns
#                 or
#                 "orderid" in columns
#             ):
#                 metrics.append(
#                     f"""
# Order Count =
# COUNT(DISTINCT
# {table_name}.orderNumber)
# """
#                 )

#         return "\n".join(metrics)





# metric_discovery.py

class MetricDiscovery:

    REVENUE_COLUMNS = {
        "price",
        "priceeach",
        "unitprice",
        "amount",
        "revenue",
        "totalamount"
    }

    QUANTITY_COLUMNS = {
        "quantity",
        "quantityordered",
        "qty"
    }

    CANONICAL_TABLES = {
        "Customer Count": "customers",
        "Order Count": "orders",
        "Total Amount": "payments",
        "Revenue": "orderdetails"
    }

    @staticmethod
    def generate(schema_df):

        metric_map = {}

        for table_name, group in schema_df.groupby("TABLE_NAME"):

            columns = {
                c.lower()
                for c in group["COLUMN_NAME"].tolist()
            }

            # --------------------------------------------------
            # Revenue
            # --------------------------------------------------

            quantity_col = None
            price_col = None

            for col in columns:

                if col in MetricDiscovery.QUANTITY_COLUMNS:
                    quantity_col = col

                if col in MetricDiscovery.REVENUE_COLUMNS:
                    price_col = col

            if (
                table_name ==
                MetricDiscovery.CANONICAL_TABLES["Revenue"]
                and
                quantity_col
                and
                price_col
            ):

                metric_map["Revenue"] = f"""
Revenue =
SUM({table_name}.{quantity_col} *
{table_name}.{price_col})
"""

            # --------------------------------------------------
            # Total Amount
            # --------------------------------------------------

            if (
                table_name ==
                MetricDiscovery.CANONICAL_TABLES["Total Amount"]
                and
                "amount" in columns
            ):

                metric_map["Total Amount"] = f"""
Total Amount =
SUM({table_name}.amount)
"""

            # --------------------------------------------------
            # Customer Count
            # --------------------------------------------------

            if (
                table_name ==
                MetricDiscovery.CANONICAL_TABLES["Customer Count"]
                and
                "customernumber" in columns
            ):

                metric_map["Customer Count"] = f"""
Customer Count =
COUNT(DISTINCT {table_name}.customerNumber)
"""

            # --------------------------------------------------
            # Order Count
            # --------------------------------------------------

            if (
                table_name ==
                MetricDiscovery.CANONICAL_TABLES["Order Count"]
                and
                "ordernumber" in columns
            ):

                metric_map["Order Count"] = f"""
Order Count =
COUNT(DISTINCT {table_name}.orderNumber)
"""

        # --------------------------------------------------
        # Derived Metrics
        # --------------------------------------------------

        if (
            "Revenue" in metric_map
            and
            "Order Count" in metric_map
        ):

            metric_map["Average Order Value"] = """
Average Order Value =
Revenue / Order Count
"""

        return "\n".join(metric_map.values())