from _plotly_utils import colors
class SemanticColumnClassifier:

    TIME_WORDS = {
        "date",
        "day",
        "month",
        "year",
        "quarter"
    }

    METRIC_WORDS = {
        "sales",
        "revenue",
        "profit",
        "amount",
        "quantity",
        "count",
        "total",
        "order",
        "orders",
        "quantity",
        "count",
        "customercount",
        "ordercount",
        "price",
        "cost",
        "discount",
        "margin",
        "score",
        "rating",
        "age"
    }

    @staticmethod
    def classify(column_name):

        col = column_name.lower()

        # if any(word in col for word in SemanticColumnClassifier.TIME_WORDS):
        #     return "TIME"

        # if any(word in col for word in SemanticColumnClassifier.METRIC_WORDS):
        #     return "METRIC"

        # return "ENTITY"



        if any(word in col for word in SemanticColumnClassifier.TIME_WORDS):
            return "TIME"

        if any(word in col for word in SemanticColumnClassifier.METRIC_WORDS):
            return "METRIC"

        return "ENTITY"