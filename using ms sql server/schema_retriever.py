import re
from relationship_path_finder import (
    RelationshipPathFinder
)

class SchemaRetriever:


    BUSINESS_TERMS = {

    # ----------------------------
    # Customer
    # ----------------------------

    "customer": ["dimcustomer"],
    "customers": ["dimcustomer"],

    # ----------------------------
    # Sales / Revenue
    # ----------------------------

    "sale": ["factinternetsales"],
    "sales": ["factinternetsales"],
    "revenue": ["factinternetsales"],
    "income": ["factinternetsales"],

    # ----------------------------
    # Orders
    # ----------------------------

    "order": ["factinternetsales"],
    "orders": ["factinternetsales"],

    # ----------------------------
    # Products
    # ----------------------------

    "product": ["dimproduct"],
    "products": ["dimproduct"],

    # ----------------------------
    # Categories
    # ----------------------------

    "category": [
        "dimproductcategory",
        "dimproductsubcategory"
    ],

    "categories": [
        "dimproductcategory",
        "dimproductsubcategory"
    ],

    "subcategory": [
        "dimproductsubcategory"
    ],

    "subcategories": [
        "dimproductsubcategory"
    ],

    # ----------------------------
    # Territory
    # ----------------------------

    "territory": [
        "dimsalesterritory"
    ],

    "territories": [
        "dimsalesterritory"
    ],

    "region": [
        "dimsalesterritory"
    ],

    "regions": [
        "dimsalesterritory"
    ],

    # ----------------------------
    # Promotion
    # ----------------------------

    "promotion": [
        "dimpromotion"
    ],

    "promotions": [
        "dimpromotion"
    ],

    "discount": [
        "dimpromotion"
    ],

    # ----------------------------
    # Time Intelligence
    # ----------------------------

    "year": [
        "dimdate"
    ],

    "years": [
        "dimdate"
    ],

    "yearly": [
        "dimdate"
    ],

    "annual": [
        "dimdate"
    ],

    "month": [
        "dimdate"
    ],

    "months": [
        "dimdate"
    ],

    "monthly": [
        "dimdate"
    ],

    "quarter": [
        "dimdate"
    ],

    "quarters": [
        "dimdate"
    ],

    "quarterly": [
        "dimdate"
    ],

    "date": [
        "dimdate"
    ],

    "dates": [
        "dimdate"
    ],

    # ----------------------------
    # Trend Analysis
    # ----------------------------

    "growth": [
        "dimdate"
    ],

    "trend": [
        "dimdate"
    ],

    "increase": [
        "dimdate"
    ],

    "decrease": [
        "dimdate"
    ],

    "decline": [
        "dimdate"
    ],

    "declining": [
        "dimdate"
    ],

    # ----------------------------
    # Geography
    # ----------------------------

    "geography": [
        "dimgeography"
    ],

    "location": [
        "dimgeography"
    ],

    "country": [
        "dimgeography"
    ],

    "city": [
        "dimgeography"
    ],

    "state": [
        "dimgeography"
    ],

    # ----------------------------
    # Currency
    # ----------------------------

    "currency": [
        "dimcurrency"
    ],

    # ----------------------------
    # Inventory
    # ----------------------------

    "inventory": [
        "factproductinventory"
    ],

    "stock": [
        "factproductinventory"
    ]
}
    
    @staticmethod
    def normalize_name(text):

        text = text.lower()

        text = re.sub(r"^dim", "", text)
        text = re.sub(r"^fact", "", text)

        if text.endswith("ies"):
            text = text[:-3] + "y"

        elif text.endswith("s"):
            text = text[:-1]

        return text

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

        # tokens = set(
        #     re.findall(
        #         r"\w+",
        #         question
        #     )
        # )

        # for table, column in column_names:

        #     if (
        #         column.lower()
        #         in tokens
        #     ):

        #         selected_tables.add(
        #             table.lower()
        #         )

        tokens = set(
            re.findall(
                r"\w+",
                question
            )
        )  

        for token in tokens:

            if token in SchemaRetriever.BUSINESS_TERMS:

                selected_tables.update(
                    SchemaRetriever.BUSINESS_TERMS[token]
                )

        # ----------------------------------
# Compound business rules
# ----------------------------------

        if "customer" in tokens and (
            "sales" in tokens or
            "revenue" in tokens
        ):
            selected_tables.add("factinternetsales")

        if "product" in tokens and (
            "sales" in tokens or
            "revenue" in tokens
        ):
            selected_tables.add("factinternetsales")

        if (
            "year" in tokens or
            "yearly" in tokens or
            "monthly" in tokens or
            "quarterly" in tokens or
            "growth" in tokens or
            "trend" in tokens
        ):
            selected_tables.add("dimdate")

        if (
            "category" in tokens or
            "categories" in tokens
        ):
            selected_tables.add("dimproductcategory")
            selected_tables.add("dimproductsubcategory")
        
        normalized_tokens = {
            SchemaRetriever.normalize_name(
                token
            )
            for token in tokens
        }

        for table in table_names:

            normalized_table = (
                SchemaRetriever
                .normalize_name(table)
            )

            if normalized_table in normalized_tokens:

                selected_tables.add(table)
        print("TOKENS:", tokens)
        print("TABLES:", table_names[:20])
        return sorted(
            list(selected_tables)
        )
