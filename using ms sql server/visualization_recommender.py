# class VisualizationRecommender:

#     @staticmethod
#     def recommend(question):

#         q = question.lower()

#         if "trend" in q:
#             return "line"

#         if "top" in q:
#             return "horizontal_bar"

#         if "contribution" in q:
#             return "pie"

#         if "percentage" in q:
#             return "pie"

#         if "distribution" in q:
#             return "histogram"

#         if "territory" in q and "year" in q:
#             return "grouped_bar"

#         return "bar"




# from chart_types import ChartTypes

# from visualization_intent_detector import (
#     VisualizationIntentDetector
# )

# from visualization_shape_detector import (
#     VisualizationShapeDetector
# )


# class VisualizationRecommender:

#     @staticmethod
#     def recommend(
#         question,
#         df
#     ):

#         intent = (
#             VisualizationIntentDetector
#             .detect(question)
#         )

#         shape = (
#             VisualizationShapeDetector
#             .detect(df)
#         )

#         print(
#             f"Intent={intent}"
#         )

#         print(
#             f"Shape={shape}"
#         )

#         # ----------------------------
#         # TREND
#         # ----------------------------

#         if (
#             intent == "TREND"
#             and
#             shape == "TIME_SERIES"
#         ):
#             return ChartTypes.LINE

#         # ----------------------------
#         # RANKING
#         # ----------------------------

#         if (
#             intent == "RANKING"
#             and
#             shape == "CATEGORY_METRIC"
#         ):
#             return ChartTypes.HORIZONTAL_BAR

#         # ----------------------------
#         # CONTRIBUTION
#         # ----------------------------

#         if (
#             intent == "CONTRIBUTION"
#             and
#             shape == "CATEGORY_METRIC"
#         ):
#             return ChartTypes.PIE

#         # ----------------------------
#         # COMPARISON
#         # ----------------------------

#         if (
#             intent == "COMPARISON"
#             and
#             shape == "CATEGORY_CATEGORY_METRIC"
#         ):
#             return ChartTypes.GROUPED_BAR

#         # ----------------------------
#         # DISTRIBUTION
#         # ----------------------------

#         if intent == "DISTRIBUTION":
#             return ChartTypes.HISTOGRAM

#         # ----------------------------
#         # CORRELATION
#         # ----------------------------

#         if (
#             intent == "CORRELATION"
#             and
#             shape == "NUMERIC_NUMERIC"
#         ):
#             return ChartTypes.SCATTER

#         return ChartTypes.BAR




from multiprocessing import sharedctypes
from chart_types import ChartTypes

from visualization_intent_detector import (
    VisualizationIntentDetector
)

from visualization_shape_detector import (
    VisualizationShapeDetector
)


class VisualizationRecommender:

    @staticmethod
    def recommend(
        question,
        df
    ):

        intent = (
            VisualizationIntentDetector
            .detect(question)
        )

        shape = (
            VisualizationShapeDetector
            .detect(df)
        )

        print(
            f"Intent={intent}"
        )

        print(
            f"Shape={shape}"
        )

        # # ----------------------------------
        # # Trend Analysis
        # #
        # # Example:
        # # Monthly revenue trend
        # # ----------------------------------

        # if (
        #     intent == "TREND"
        #     and
        #     shape == "TIME_SERIES"
        # ):
        #     return ChartTypes.LINE

        # # ----------------------------------
        # # Comparison
        # #
        # # Example:
        # # Compare yearly revenue by territory
        # # Compare sales by category and month
        # # ----------------------------------

        # # if (
        # #     intent == "COMPARISON"
        # #     and
        # #     shape == "TIME_CATEGORY_METRIC"
        # # ):
        # #     return ChartTypes.GROUPED_BAR

        # # if (
        # #     intent == "COMPARISON"
        # #     and
        # #     shape == "CATEGORY_CATEGORY_METRIC"
        # # ):
        # #     return ChartTypes.GROUPED_BAR

        # if intent == "COMPARISON":
        #     return ChartTypes.GROUPED_BAR

        # # ----------------------------------
        # # Ranking
        # #
        # # Example:
        # # Top customers by sales
        # # ----------------------------------

        # if (
        #     intent == "RANKING"
        #     and
        #     shape == "CATEGORY_METRIC"
        # ):
        #     return ChartTypes.HORIZONTAL_BAR

        # # ----------------------------------
        # # Contribution
        # #
        # # Example:
        # # Revenue contribution by category
        # # ----------------------------------

        # if (
        #     intent == "CONTRIBUTION"
        #     and
        #     shape == "CATEGORY_METRIC"
        # ):
        #     return ChartTypes.PIE

        # # ----------------------------------
        # # Distribution
        # #
        # # Example:
        # # Sales distribution
        # # ----------------------------------

        # if (
        #     intent == "DISTRIBUTION"
        # ):
        #     return ChartTypes.HISTOGRAM

        # # ----------------------------------
        # # Correlation
        # #
        # # Example:
        # # Revenue vs Discount
        # # ----------------------------------

        # if (
        #     intent == "CORRELATION"
        #     and
        #     shape == "NUMERIC_NUMERIC"
        # ):
        #     return ChartTypes.SCATTER

        # # ----------------------------------
        # # Smart Fallbacks
        # # ----------------------------------

        # if shape == "TIME_SERIES":
        #     return ChartTypes.LINE

        # if shape == "CATEGORY_METRIC":
        #     return ChartTypes.BAR

        # if shape == "TIME_CATEGORY_METRIC":
        #     return ChartTypes.GROUPED_BAR

        # if shape == "CATEGORY_CATEGORY_METRIC":
        #     return ChartTypes.GROUPED_BAR

        # if shape == "NUMERIC_NUMERIC":
        #     return ChartTypes.SCATTER

        # return ChartTypes.BAR



        # ----------------------------------
        # Trend Analysis
        #
        # Example:
        # Monthly revenue trend
        # ----------------------------------

        if (
            intent == "TREND"
            and
            shape == "TIME_SERIES"
        ):
            return ChartTypes.LINE


        # ----------------------------------
        # Numeric vs Numeric
        #
        # Example:
        # Price vs Quantity
        # Revenue vs Profit
        # Discount vs Sales
        # ----------------------------------

        if shape == "NUMERIC_NUMERIC":
            return ChartTypes.SCATTER


        # ----------------------------------
        # Comparison
        #
        # Example:
        # Compare yearly revenue by territory
        # Compare sales by category and month
        # Compare promotion effectiveness
        # ----------------------------------

        if intent == "COMPARISON":
            return ChartTypes.GROUPED_BAR


        # ----------------------------------
        # Ranking
        #
        # Example:
        # Top customers by sales
        # ----------------------------------

        if (
            intent == "RANKING"
            and
            shape == "CATEGORY_METRIC"
        ):
            return ChartTypes.HORIZONTAL_BAR


        # ----------------------------------
        # Contribution
        #
        # Example:
        # Revenue contribution by category
        # ----------------------------------

        if (
            intent == "CONTRIBUTION"
            and
            shape == "CATEGORY_METRIC"
        ):
            return ChartTypes.PIE


        # ----------------------------------
        # Distribution
        #
        # Example:
        # Sales distribution
        # ----------------------------------

        if intent == "DISTRIBUTION":
            return ChartTypes.HISTOGRAM


        # ----------------------------------
        # Correlation
        #
        # Example:
        # Revenue vs Discount
        # ----------------------------------

        if (
            intent == "CORRELATION"
            and
            shape == "NUMERIC_NUMERIC"
        ):
            return ChartTypes.SCATTER


        # ----------------------------------
        # Smart Fallbacks
        # ----------------------------------

        if shape == "TIME_SERIES":
            return ChartTypes.LINE

        if shape == "CATEGORY_METRIC":
            return ChartTypes.BAR

        if shape == "TIME_CATEGORY_METRIC":
            return ChartTypes.GROUPED_BAR

        if shape == "CATEGORY_CATEGORY_METRIC":
            return ChartTypes.GROUPED_BAR

        if shape == "NUMERIC_NUMERIC":
            return ChartTypes.SCATTER

        return ChartTypes.BAR