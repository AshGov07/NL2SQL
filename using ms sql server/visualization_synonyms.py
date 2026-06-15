# class VisualizationSynonyms:

#     INTENT_SYNONYMS = {

#         "TREND": {

#     "trend",
#     "growth",
#     "evolution",
#     "evolve",
#     "evolved",
#     "changed",
#     "change",
#     "changing",

#     "increase",
#     "increasing",

#     "decrease",
#     "decreasing",

#     "movement",
#     "progression",
#     "historical",
#     "history",

#     "over time",
#     "journey",
#     "trajectory"
# },

#         # "RANKING": {

#         #     "top",
#         #     "bottom",
#         #     "highest",
#         #     "lowest",
#         #     "best",
#         #     "worst",
#         #     "biggest",
#         #     "largest",
#         #     "leading",
#         #     "rank",
#         #     "ranking",
#         #     "strongest",
#         #     "weakest",
#         #     "top-performing",
#         #     "highest-performing"
#         # },
#         "RANKING": {

#     "top",
#     "bottom",

#     "highest",
#     "lowest",

#     "best",
#     "worst",

#     "largest",
#     "biggest",

#     "leading",

#     "rank",
#     "ranking",

#     "most revenue",
#     "most sales",

#     "top-performing",
#     "highest-performing"
# },

#         # "CONTRIBUTION": {

#         #     "contribution",
#         #     "share",
#         #     "portion",
#         #     "percentage",
#         #     "percent",
#         #     "composition",
#         #     "allocation",
#         #     "breakdown",
#         #     "mix",
#         #     "market share"
#         # },

#         "CONTRIBUTION": {

#     "contribution",

#     "contributes",
#     "contribute",

#     "share",
#     "portion",

#     "percentage",
#     "percent",

#     "composition",

#     "allocation",

#     "breakdown",
#     "break down",

#     "market share",

#     "drive",
#     "drives"
# },

#         # "COMPARISON": {

#         #     "compare",
#         #     "comparison",
#         #     "versus",
#         #     "vs",
#         #     "against",
#         #     "side by side",
#         #     "relative to",
#         #     "relative performance"
#         # },
#         "COMPARISON": {

#     "compare",
#     "comparison",

#     "versus",
#     "vs",

#     "against",

#     "side by side",
#     "side-by-side",

#     "relative to",

#     "perform better",
#     "compare performance",

#     "effectiveness"
# },

#         "DISTRIBUTION": {

#             "distribution",
#             "spread",
#             "frequency",
#             "histogram"
#         },

#         "CORRELATION": {

#             "relationship",
#             "correlation",
#             "impact",
#             "effect",
#             "association",
#             "dependency",
#             "influence"
#         }
#     }




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

        # ----------------------------------
        # Trend Analysis
        # ----------------------------------

        if (
            intent == "TREND"
            and
            shape == "TIME_SERIES"
        ):
            return ChartTypes.LINE

        # ----------------------------------
        # Comparison
        # ----------------------------------

        if intent == "COMPARISON":
            return ChartTypes.GROUPED_BAR

        # ----------------------------------
        # Ranking
        # ----------------------------------

        if (
            intent == "RANKING"
            and
            shape == "CATEGORY_METRIC"
        ):
            return ChartTypes.HORIZONTAL_BAR

        # ----------------------------------
        # Contribution
        # ----------------------------------

        if (
            intent == "CONTRIBUTION"
            and
            shape == "CATEGORY_METRIC"
        ):
            return ChartTypes.PIE

        # ----------------------------------
        # Distribution
        # ----------------------------------

        if intent == "DISTRIBUTION":
            return ChartTypes.HISTOGRAM

        # ----------------------------------
        # Correlation
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