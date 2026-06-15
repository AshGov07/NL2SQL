# from vanna.integrations.plotly import PlotlyChartGenerator
# from visualization_recommender import VisualizationRecommender

# class CustomPlotlyChartGenerator:

#     def __init__(self):
#         self.base_generator = PlotlyChartGenerator()

#     def generate_chart(
#         self,
#         question,
#         df,
#         title
#     ):
#         chart_type = (
#             VisualizationRecommender
#             .recommend(
#                 question,
#                 df
#             )
#         )

#         print(
#             f"Recommended Chart: {chart_type}"
#         )

#         ...



from chart_types import ChartTypes
from vanna.integrations.plotly import PlotlyChartGenerator

from visualization_recommender import (
    VisualizationRecommender
)


class CustomPlotlyChartGenerator:

    def __init__(self):

        self.base_generator = (
            PlotlyChartGenerator()
        )

    def generate_chart(
        self,
        df,
        title="Chart"
    ):
        print("\n===== CUSTOM GENERATOR =====")
        print("TITLE:", title)
        print("COLUMNS:", df.columns.tolist())
        print("============================")


        # print("FORCED SCATTER")

        import plotly.express as px

        # fig = px.scatter(
        #     df,
        #     x=df.columns[0],
        #     y=df.columns[1],
        #     title=title
        # )   

        # return fig.to_dict()

        chart_type = VisualizationRecommender.recommend(
    title,
    df
)       

#         chart_type = (
#     VisualizationRecommender
#     .recommend(
#         title,
#         df
#     )
# )

        print(
            "RECOMMENDED:",
            chart_type
        )

#         return (
#             self.base_generator
#             .generate_chart(
#                 df,
#                 title
#             )
#         )


        if chart_type == ChartTypes.SCATTER:

            fig = px.scatter(
                df,
                x=df.columns[0],
                y=df.columns[1],
                title=title
            )

        elif chart_type == ChartTypes.LINE:

            fig = px.line(
                df,
                x=df.columns[0],
                y=df.columns[1],
            title=title
        )

        elif chart_type == ChartTypes.PIE:

            fig = px.pie(
                df,
                names=df.columns[0],
                values=df.columns[1],
                title=title
            )

        elif chart_type == ChartTypes.HORIZONTAL_BAR:

            fig = px.bar(
                df,
                x=df.columns[1],
                y=df.columns[0],
                orientation="h",
                title=title
            )

        else:

            fig = px.bar(
                df,
                x=df.columns[0],
                y=df.columns[1],
                title=title
            )

        import json
        return json.loads(fig.to_json())
        # return fig.to_dict()