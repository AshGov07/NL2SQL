# from semantic_column_classifier import (
#     SemanticColumnClassifier
# )


# class VisualizationShapeDetector:

#     @staticmethod
#     def detect(df):

#         column_types = []

#         for col in df.columns:

#             column_types.append(
#                 SemanticColumnClassifier.classify(col)
#             )

#         # if (
#         #     column_types.count("TIME") >= 1
#         #     and
#         #     column_types.count("METRIC") >= 1
#         # ):
#         #     return "TIME_SERIES"

#         if (
#             column_types.count("TIME") >= 1
#             and
#             column_types.count("ENTITY") >= 1
#             and
#             column_types.count("METRIC") >= 1
#         ):
#             return "TIME_CATEGORY_METRIC"

#         if (
#             column_types.count("ENTITY") == 1
#             and
#             column_types.count("METRIC") == 1
#         ):
#             return "CATEGORY_METRIC"

#         if (
#             column_types.count("ENTITY") >= 2
#             and
#             column_types.count("METRIC") >= 1
#         ):
#             return "CATEGORY_CATEGORY_METRIC"

#         numeric_count = len(
#             df.select_dtypes(
#                 include="number"
#             ).columns
#         )

#         if numeric_count >= 2:
#             return "NUMERIC_NUMERIC"

#         return "UNKNOWN"













from semantic_column_classifier import (
    SemanticColumnClassifier
)


class VisualizationShapeDetector:

    @staticmethod
    def detect(df):

        column_types = []

        for col in df.columns:

            column_types.append(
                SemanticColumnClassifier.classify(col)
            )

        print(
            "Column Types:",
            column_types
        )

        # ----------------------------------
        # Time + Category + Metric
        #
        # Example:
        # Year, Territory, Revenue
        # Month, Category, Sales
        # ----------------------------------

        if (
            column_types.count("TIME") >= 1
            and
            column_types.count("ENTITY") >= 1
            and
            column_types.count("METRIC") >= 1
        ):
            return "TIME_CATEGORY_METRIC"

        # ----------------------------------
        # Time Series
        #
        # Example:
        # Month, Revenue
        # Year, Sales
        # ----------------------------------

        if (
            column_types.count("TIME") >= 1
            and
            column_types.count("METRIC") >= 1
        ):
            return "TIME_SERIES"

        # ----------------------------------
        # Category + Metric
        #
        # Example:
        # Customer, Revenue
        # Product, Sales
        # ----------------------------------

        if (
            column_types.count("ENTITY") == 1
            and
            column_types.count("METRIC") == 1
        ):
            return "CATEGORY_METRIC"

        # ----------------------------------
        # Category + Category + Metric
        #
        # Example:
        # Territory, Category, Revenue
        # ----------------------------------

        if (
            column_types.count("ENTITY") >= 2
            and
            column_types.count("METRIC") >= 1
        ):
            return "CATEGORY_CATEGORY_METRIC"

        # ----------------------------------
        # Numeric vs Numeric
        #
        # Example:
        # Discount, Revenue
        # ----------------------------------

        numeric_count = len(
            df.select_dtypes(
                include="number"
            ).columns
        )

        if numeric_count >= 2:

            return "NUMERIC_NUMERIC"

        return "UNKNOWN"