# class VisualizationIntentDetector:

#     TREND_WORDS = {
#         "trend",
#         "growth",
#         "over time",
#         "monthly",
#         "yearly",
#         "daily"
#     }

#     RANKING_WORDS = {
#         "top",
#         "bottom",
#         "highest",
#         "lowest",
#         "best",
#         "worst"
#     }

#     CONTRIBUTION_WORDS = {
#         "contribution",
#         "share",
#         "percentage",
#         "percent",
#         "portion"
#     }

#     DISTRIBUTION_WORDS = {
#         "distribution",
#         "spread",
#         "frequency"
#     }

#     CORRELATION_WORDS = {
#         "relationship",
#         "correlation",
#         "impact"
#     }

#     COMPARISON_WORDS = {
#         "compare",
#         "comparison",
#         "versus",
#         "vs"
#     }

#     # @staticmethod
#     # def detect(question):

#     #     q = question.lower()

#     #     if any(word in q for word in VisualizationIntentDetector.TREND_WORDS):
#     #         return "TREND"

#     #     if any(word in q for word in VisualizationIntentDetector.RANKING_WORDS):
#     #         return "RANKING"

#     #     if any(word in q for word in VisualizationIntentDetector.CONTRIBUTION_WORDS):
#     #         return "CONTRIBUTION"

#     #     if any(word in q for word in VisualizationIntentDetector.DISTRIBUTION_WORDS):
#     #         return "DISTRIBUTION"

#     #     if any(word in q for word in VisualizationIntentDetector.CORRELATION_WORDS):
#     #         return "CORRELATION"

#     #     if any(word in q for word in VisualizationIntentDetector.COMPARISON_WORDS):
#     #         return "COMPARISON"

#     #     return "UNKNOWN"


#     @staticmethod
#     def detect(question):

#         q = question.lower()

#         # Highest priority

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.COMPARISON_WORDS
#         ):
#             return "COMPARISON"

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.CONTRIBUTION_WORDS
#         ):
#             return "CONTRIBUTION"

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.RANKING_WORDS
#         ):
#             return "RANKING"

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.DISTRIBUTION_WORDS
#         ):
#             return "DISTRIBUTION"

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.CORRELATION_WORDS
#         ):
#             return "CORRELATION"

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.TREND_WORDS
#         ):
#             return "TREND"

#         return "UNKNOWN"



#corect working with keyword match



# class VisualizationIntentDetector:

#     TREND_WORDS = {
#         "trend",
#         "growth",
#         "over time"
#     }

#     TIME_WORDS = {
#         "monthly",
#         "yearly",
#         "daily",
#         "quarterly"
#     }

#     RANKING_WORDS = {
#         "top",
#         "bottom",
#         "highest",
#         "lowest",
#         "best",
#         "worst"
#     }

#     CONTRIBUTION_WORDS = {
#         "contribution",
#         "share",
#         "percentage",
#         "percent",
#         "portion"
#     }

#     DISTRIBUTION_WORDS = {
#         "distribution",
#         "spread",
#         "frequency"
#     }

#     CORRELATION_WORDS = {
#         "relationship",
#         "correlation",
#         "impact"
#     }

#     COMPARISON_WORDS = {
#         "compare",
#         "comparison",
#         "versus",
#         "vs",
#         "by"
#     }

#     @staticmethod
#     def detect(question):

#         q = question.lower()

#         matched_intents = []

#         # ----------------------------------
#         # Contribution
#         # Highest business priority
#         # ----------------------------------

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.CONTRIBUTION_WORDS
#         ):
#             matched_intents.append(
#                 "CONTRIBUTION"
#             )

#         # ----------------------------------
#         # Ranking
#         # ----------------------------------

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.RANKING_WORDS
#         ):
#             matched_intents.append(
#                 "RANKING"
#             )

#         # ----------------------------------
#         # Distribution
#         # ----------------------------------

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.DISTRIBUTION_WORDS
#         ):
#             matched_intents.append(
#                 "DISTRIBUTION"
#             )

#         # ----------------------------------
#         # Correlation
#         # ----------------------------------

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.CORRELATION_WORDS
#         ):
#             matched_intents.append(
#                 "CORRELATION"
#             )

#         # ----------------------------------
#         # Explicit comparison
#         # ----------------------------------

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.COMPARISON_WORDS
#         ):
#             matched_intents.append(
#                 "COMPARISON"
#             )

#         # ----------------------------------
#         # Trend
#         # ----------------------------------

#         if any(
#             word in q
#             for word in VisualizationIntentDetector.TREND_WORDS
#         ):
#             matched_intents.append(
#                 "TREND"
#             )

#         # ----------------------------------
#         # Time + By
#         #
#         # Example:
#         # yearly revenue by territory
#         # monthly sales by category
#         # ----------------------------------

#         if (
#             any(
#                 word in q
#                 for word in VisualizationIntentDetector.TIME_WORDS
#             )
#             and
#             " by " in f" {q} "
#         ):
#             matched_intents.append(
#                 "COMPARISON"
#             )

#         # ----------------------------------
#         # Priority Resolution
#         # ----------------------------------

#         priority_order = [

#             "CONTRIBUTION",

#             "RANKING",

#             "DISTRIBUTION",

#             "CORRELATION",

#             "COMPARISON",

#             "TREND"
#         ]

#         for intent in priority_order:

#             if intent in matched_intents:

#                 return intent

#         return "UNKNOWN"

# from visualization_synonyms import (
#     VisualizationSynonyms
# )


# class VisualizationIntentDetector:

#     @staticmethod
#     def detect(question):

#         q = question.lower()

#         scores = {}

#         for intent, words in (
#             VisualizationSynonyms
#             .INTENT_SYNONYMS
#             .items()
#         ):

#             score = 0

#             for word in words:

#                 if word in q:
#                     score += 1

#             scores[intent] = score

#         best_intent = max(
#             scores,
#             key=scores.get
#         )

#         if scores[best_intent] > 0:
#             return best_intent

#         return "UNKNOWN"



class VisualizationIntentDetector:

    TREND_WORDS = {

        "trend",
        "growth",

        "evolution",
        "evolve",
        "evolved",

        "changed",
        "change",
        "changing",

        "increase",
        "increasing",

        "decrease",
        "decreasing",

        "movement",
        "progression",

        "historical",
        "history",

        "over time",

        "journey",
        "trajectory"
    }

    RANKING_WORDS = {

        "top",
        "bottom",

        "highest",
        "lowest",

        "best",
        "worst",

        "largest",
        "biggest",

        "leading",

        "rank",
        "ranking",

        "most revenue",
        "most sales",

        "top-performing",
        "highest-performing",
        "rank",
    "ranking",
    "leaderboard",
    "sorted",
    "sort",
    "least",
    "most",
    "largest",
    "smallest",
    "outperforming",
    "prominent"
    }

    CONTRIBUTION_WORDS = {

        "contribution",

        "contribute",
        "contributes",

        "share",
        "portion",

        "percentage",
        "percent",

        "composition",

        "allocation",

        "breakdown",
        "break down",

        "market share",

        "drive",
        "drives",
        "fraction",
        "split",
        "breakdown",
        "allocation",
        "divide",
        "proportion",
        "stake",
        "fraction",
        "split",
        "breakdown",
        "allocation",
        "divide",
        "proportion",
        "stake",
        "market share",
        "account for",
        "bulk of",
        "contributor",
        "contribution",
        "feeding into",
        "primary contributor",
        "major contributor",
        "account for",
        "bulk of",
        "feeding into",
        "primary contributor",
        "major contributor"
    }

    DISTRIBUTION_WORDS = {

        "distribution",
        "spread",
        "frequency",
        "histogram",
         "variance",
    "dispersion",
    "density",
    "bucket",
    "range",
    "recurrence"
    }

    CORRELATION_WORDS = {

        "relationship",
        "correlation",

        "impact",
        "effect",

        "association",
        "dependency",

        "influence"
    }

    COMPARISON_WORDS = {

        "compare",
        "comparison",

        "versus",
        "vs",

        "against",

        "side by side",
        "side-by-side",

        "relative to",

        "perform better",
        "compare performance",

        "effectiveness",
        "contrast",
    "juxtapose",
    "paired",
    "against",
    "between",
    "side-by-side"
    }

    @staticmethod
    def detect(question):

        q = question.lower()

        # if any(
        #     phrase in q
        #     for phrase in VisualizationIntentDetector.COMPARISON_WORDS
        # ):
        #     return "COMPARISON"

        # if any(
        #     phrase in q
        #     for phrase in VisualizationIntentDetector.CONTRIBUTION_WORDS
        # ):
        #     return "CONTRIBUTION"

        # if any(
        #     phrase in q
        #     for phrase in VisualizationIntentDetector.RANKING_WORDS
        # ):
        #     return "RANKING"


        if any(phrase in q for phrase in VisualizationIntentDetector.CONTRIBUTION_WORDS):
            return "CONTRIBUTION"

        if any(
            phrase in q
            for phrase in VisualizationIntentDetector.RANKING_WORDS
        ):
            return "RANKING"

        if any(
            phrase in q
            for phrase in VisualizationIntentDetector.COMPARISON_WORDS
        ):
            return "COMPARISON"

        if any(
            phrase in q
            for phrase in VisualizationIntentDetector.DISTRIBUTION_WORDS
        ):
            return "DISTRIBUTION"

        if any(
            phrase in q
            for phrase in VisualizationIntentDetector.CORRELATION_WORDS
        ):
            return "CORRELATION"

        if any(
            phrase in q
            for phrase in VisualizationIntentDetector.TREND_WORDS
        ):
            return "TREND"

        return "UNKNOWN"