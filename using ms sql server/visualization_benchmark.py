# benchmark_cases = [

#     (
#         "Show monthly revenue trend",
#         "line"
#     ),

#     (
#         "Show top 10 customers by sales",
#         "horizontal_bar"
#     ),

#     (
#         "Show revenue contribution by category",
#         "pie"
#     ),

#     (
#         "Compare yearly revenue by territory",
#         "grouped_bar"
#     ),

#     (
#         "Show sales distribution",
#         "histogram"
#     )
# ]




import pandas as pd

from visualization_recommender import (
    VisualizationRecommender
)

# benchmark_cases = [

#     {
#         "question":
#         "Show monthly revenue trend",

#         "df":
#         pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Revenue": [1000, 2000]
#         }),

#         "expected":
#         "line"
#     },

#     {
#         "question":
#         "Show top 10 customers by sales",

#         "df":
#         pd.DataFrame({
#             "Customer": ["A", "B"],
#             "Sales": [100, 200]
#         }),

#         "expected":
#         "horizontal_bar"
#     },

#     {
#         "question":
#         "Show revenue contribution by category",

#         "df":
#         pd.DataFrame({
#             "Category": ["A", "B"],
#             "Revenue": [100, 200]
#         }),

#         "expected":
#         "pie"
#     },

#     {
#         "question":
#         "Compare yearly revenue by territory",

#         "df":
#         pd.DataFrame({
#             "Year": [2023, 2023],
#             "Territory": ["East", "West"],
#             "Revenue": [100, 200]
#         }),

#         "expected":
#         "grouped_bar"
#     },

#     {
#         "question":
#         "Show sales distribution",

#         "df":
#         pd.DataFrame({
#             "Sales": [10, 20, 30, 40]
#         }),

#         "expected":
#         "histogram"
#     }
# ]

#100% with harder questions
# benchmark_cases = [

#     # ==================================================
#     # TREND (10)
#     # ==================================================

#     {
#         "question": "Show monthly revenue trend",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Show yearly revenue trend",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Year": [2023, 2024],
#             "Revenue": [10000, 15000]
#         })
#     },

#     {
#         "question": "Show quarterly sales trend",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Quarter": ["Q1", "Q2"],
#             "Sales": [1000, 1500]
#         })
#     },

#     {
#         "question": "Show daily order trend",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Date": ["2024-01-01", "2024-01-02"],
#             "Orders": [50, 75]
#         })
#     },

#     {
#         "question": "Show monthly customer growth",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "CustomerCount": [100, 120]
#         })
#     },

#     {
#         "question": "Show yearly profit growth",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Year": [2023, 2024],
#             "Profit": [10000, 12000]
#         })
#     },

#     {
#         "question": "Show revenue trend over time",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Show monthly product sales trend",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Sales": [200, 250]
#         })
#     },

#     {
#         "question": "Show yearly territory revenue trend",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Year": [2023, 2024],
#             "Revenue": [5000, 7000]
#         })
#     },

#     {
#         "question": "Show quarterly order quantity trend",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Quarter": ["Q1", "Q2"],
#             "Quantity": [100, 140]
#         })
#     },

#     # ==================================================
#     # RANKING (10)
#     # ==================================================

#     {
#         "question": "Show top 10 customers by sales",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Customer": ["A", "B"],
#             "Sales": [1000, 2000]
#         })
#     },

#     {
#         "question": "Show top 20 products by revenue",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Product": ["P1", "P2"],
#             "Revenue": [5000, 7000]
#         })
#     },

#     {
#         "question": "Show highest selling product categories",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Category": ["Bike", "Accessory"],
#             "Sales": [3000, 1000]
#         })
#     },

#     {
#         "question": "Show best performing territories",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Revenue": [8000, 6000]
#         })
#     },

#     {
#         "question": "Show lowest performing territories",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Revenue": [2000, 6000]
#         })
#     },

#     {
#         "question": "Show bottom 10 customers by sales",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Customer": ["A", "B"],
#             "Sales": [100, 200]
#         })
#     },

#     {
#         "question": "Show top promotions by revenue",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Promotion": ["Promo1", "Promo2"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Show highest profit products",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Product": ["P1", "P2"],
#             "Profit": [1000, 1500]
#         })
#     },

#     {
#         "question": "Show best sales regions",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Region": ["North", "South"],
#             "Sales": [9000, 6000]
#         })
#     },

#     {
#         "question": "Show top employees by sales",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Employee": ["John", "Mary"],
#             "Sales": [4000, 5000]
#         })
#     },

#     # ==================================================
#     # CONTRIBUTION (7)
#     # ==================================================

#     {
#         "question": "Show revenue contribution by category",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Category": ["A", "B"],
#             "Revenue": [60, 40]
#         })
#     },

#     {
#         "question": "Show percentage contribution by territory",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Revenue": [70, 30]
#         })
#     },

#     {
#         "question": "Show sales share by promotion",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Promotion": ["A", "B"],
#             "Sales": [80, 20]
#         })
#     },

#     {
#         "question": "Show product contribution to revenue",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Product": ["P1", "P2"],
#             "Revenue": [50, 50]
#         })
#     },

#     {
#         "question": "Show category share of revenue",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Category": ["A", "B"],
#             "Revenue": [30, 70]
#         })
#     },

#     {
#         "question": "Show revenue percentage by region",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Region": ["North", "South"],
#             "Revenue": [45, 55]
#         })
#     },

#     {
#         "question": "Show territory contribution to total sales",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Sales": [25, 75]
#         })
#     },

#     # ==================================================
#     # COMPARISON (8)
#     # ==================================================

#     {
#         "question": "Compare yearly revenue by territory",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Year": [2023, 2023],
#             "Territory": ["East", "West"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Compare monthly sales by category",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Jan"],
#             "Category": ["A", "B"],
#             "Sales": [100, 200]
#         })
#     },

#     {
#         "question": "Compare revenue by territory and promotion",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Promotion": ["P1", "P2"],
#             "Revenue": [1000, 1200]
#         })
#     },

#     {
#         "question": "Compare sales by product category and year",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Category": ["Bike", "Accessory"],
#             "Year": [2024, 2024],
#             "Sales": [1000, 500]
#         })
#     },

#     {
#         "question": "Compare yearly profit by territory",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Year": [2023, 2023],
#             "Territory": ["East", "West"],
#             "Profit": [1000, 1500]
#         })
#     },

#     {
#         "question": "Compare quarterly sales by category",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Quarter": ["Q1", "Q1"],
#             "Category": ["A", "B"],
#             "Sales": [100, 120]
#         })
#     },

#     {
#         "question": "Compare territory performance by year",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Year": [2024, 2024],
#             "Revenue": [5000, 4000]
#         })
#     },

#     {
#         "question": "Compare promotion revenue by region",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Promotion": ["P1", "P2"],
#             "Region": ["North", "South"],
#             "Revenue": [500, 700]
#         })
#     },

#     # ==================================================
#     # DISTRIBUTION (3)
#     # ==================================================

#     {
#         "question": "Show sales distribution",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "Sales": [10, 20, 30, 40, 50]
#         })
#     },

#     {
#         "question": "Show order amount distribution",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "OrderAmount": [100, 150, 200, 250]
#         })
#     },

#     {
#         "question": "Show customer age distribution",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "Age": [20, 25, 30, 35]
#         })
#     },

#     # ==================================================
#     # CORRELATION (3)
#     # ==================================================

#     {
#         "question": "Show relationship between discount and sales",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Discount": [0, 5, 10],
#             "Sales": [100, 90, 80]
#         })
#     },

#     {
#         "question": "Show correlation between price and quantity",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Price": [10, 20, 30],
#             "Quantity": [100, 70, 40]
#         })
#     },

#     {
#         "question": "Show impact of discount on revenue",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Discount": [0, 5, 10],
#             "Revenue": [1000, 900, 800]
#         })
#     },

#     # ==================================================
# # PHASE 4.1 NATURAL LANGUAGE STRESS TESTS
# # ==================================================

# # TREND

# {
#     "question": "How has revenue changed over time?",
#     "expected": "line",
#     "df": pd.DataFrame({
#         "Year": [2023, 2024],
#         "Revenue": [1000, 1500]
#     })
# },

# {
#     "question": "How has sales evolved over the years?",
#     "expected": "line",
#     "df": pd.DataFrame({
#         "Year": [2023, 2024],
#         "Sales": [1000, 2000]
#     })
# },

# {
#     "question": "Show me the revenue journey month by month",
#     "expected": "line",
#     "df": pd.DataFrame({
#         "Month": ["Jan", "Feb"],
#         "Revenue": [1000, 2000]
#     })
# },

# {
#     "question": "Is revenue increasing or decreasing?",
#     "expected": "line",
#     "df": pd.DataFrame({
#         "Month": ["Jan", "Feb"],
#         "Revenue": [1000, 1500]
#     })
# },

# {
#     "question": "Track customer growth over time",
#     "expected": "line",
#     "df": pd.DataFrame({
#         "Month": ["Jan", "Feb"],
#         "CustomerCount": [100, 120]
#     })
# },

# # RANKING

# {
#     "question": "Who are our biggest customers?",
#     "expected": "horizontal_bar",
#     "df": pd.DataFrame({
#         "Customer": ["A", "B"],
#         "Revenue": [5000, 7000]
#     })
# },

# {
#     "question": "Which customers generate the most revenue?",
#     "expected": "horizontal_bar",
#     "df": pd.DataFrame({
#         "Customer": ["A", "B"],
#         "Revenue": [6000, 8000]
#     })
# },

# {
#     "question": "Show the largest customers",
#     "expected": "horizontal_bar",
#     "df": pd.DataFrame({
#         "Customer": ["A", "B"],
#         "Revenue": [1000, 2000]
#     })
# },

# {
#     "question": "Which territories perform best?",
#     "expected": "horizontal_bar",
#     "df": pd.DataFrame({
#         "Territory": ["East", "West"],
#         "Revenue": [9000, 5000]
#     })
# },

# {
#     "question": "Show our leading territories",
#     "expected": "horizontal_bar",
#     "df": pd.DataFrame({
#         "Territory": ["East", "West"],
#         "Revenue": [7000, 4000]
#     })
# },

# # CONTRIBUTION

# {
#     "question": "Which categories drive most revenue?",
#     "expected": "pie",
#     "df": pd.DataFrame({
#         "Category": ["Bikes", "Accessories"],
#         "Revenue": [80, 20]
#     })
# },

# {
#     "question": "What contributes most to sales?",
#     "expected": "pie",
#     "df": pd.DataFrame({
#         "Category": ["A", "B"],
#         "Sales": [70, 30]
#     })
# },

# {
#     "question": "Break down revenue by category",
#     "expected": "pie",
#     "df": pd.DataFrame({
#         "Category": ["A", "B"],
#         "Revenue": [60, 40]
#     })
# },

# {
#     "question": "Show revenue composition",
#     "expected": "pie",
#     "df": pd.DataFrame({
#         "Category": ["A", "B"],
#         "Revenue": [55, 45]
#     })
# },

# {
#     "question": "Show market share by region",
#     "expected": "pie",
#     "df": pd.DataFrame({
#         "Region": ["North", "South"],
#         "Revenue": [65, 35]
#     })
# },

# # COMPARISON

# {
#     "question": "How do territories compare?",
#     "expected": "grouped_bar",
#     "df": pd.DataFrame({
#         "Territory": ["East", "West"],
#         "Year": [2024, 2024],
#         "Revenue": [1000, 1500]
#     })
# },

# {
#     "question": "Show category performance side by side",
#     "expected": "grouped_bar",
#     "df": pd.DataFrame({
#         "Category": ["A", "B"],
#         "Revenue": [1000, 1200]
#     })
# },

# {
#     "question": "Compare regions across years",
#     "expected": "grouped_bar",
#     "df": pd.DataFrame({
#         "Year": [2023, 2023],
#         "Region": ["North", "South"],
#         "Revenue": [1000, 1500]
#     })
# },

# {
#     "question": "Show side-by-side revenue comparison",
#     "expected": "grouped_bar",
#     "df": pd.DataFrame({
#         "Region": ["East", "West"],
#         "Revenue": [1000, 1200]
#     })
# },

# {
#     "question": "Compare promotion effectiveness",
#     "expected": "grouped_bar",
#     "df": pd.DataFrame({
#         "Promotion": ["Promo1", "Promo2"],
#         "Revenue": [1000, 1200]
#     })
# },

# # DISTRIBUTION

# {
#     "question": "How are sales spread out?",
#     "expected": "histogram",
#     "df": pd.DataFrame({
#         "Sales": [10,20,30,40,50]
#     })
# },

# {
#     "question": "Visualize customer age spread",
#     "expected": "histogram",
#     "df": pd.DataFrame({
#         "Age": [20,25,30,35,40]
#     })
# },

# {
#     "question": "Show frequency of order amounts",
#     "expected": "histogram",
#     "df": pd.DataFrame({
#         "OrderAmount": [100,150,200,250,300]
#     })
# },

# # CORRELATION

# {
#     "question": "Does discount impact revenue?",
#     "expected": "scatter",
#     "df": pd.DataFrame({
#         "Discount": [0,5,10],
#         "Revenue": [1000,900,800]
#     })
# },

# {
#     "question": "Analyze price versus quantity",
#     "expected": "scatter",
#     "df": pd.DataFrame({
#         "Price": [10,20,30],
#         "Quantity": [100,70,40]
#     })
# },

# {
#     "question": "Does price affect sales?",
#     "expected": "scatter",
#     "df": pd.DataFrame({
#         "Price": [10,20,30],
#         "Sales": [1000,800,600]
#     })
# },

# {
#     "question": "Show correlation between order quantity and revenue",
#     "expected": "scatter",
#     "df": pd.DataFrame({
#         "Quantity": [10,20,30],
#         "Revenue": [1000,2000,3000]
#     })
# }
# ]

#100% with nl like simulation and not nl (not used sql)

benchmark_cases = [

    # ==================================================
    # TREND (10)
    # ==================================================

    {
        "question": "Plot the change in revenue on a month-by-month basis",
        "expected": "line",
        "df": pd.DataFrame({
            "Month": ["Jan", "Feb"],
            "Revenue": [1000, 2000]
        })
    },

    {
        "question": "What is the trajectory of our revenue year over year?",
        "expected": "line",
        "df": pd.DataFrame({
            "Year": [2023, 2024],
            "Revenue": [10000, 15000]
        })
    },

    {
        "question": "Graph the progression of sales across quarters",
        "expected": "line",
        "df": pd.DataFrame({
            "Quarter": ["Q1", "Q2"],
            "Sales": [1000, 1500]
        })
    },

    {
        "question": "Display the daily pattern of order volume",
        "expected": "line",
        "df": pd.DataFrame({
            "Date": ["2024-01-01", "2024-01-02"],
            "Orders": [50, 75]
        })
    },

    {
        "question": "Illustrate how our customer base expands over the months",
        "expected": "line",
        "df": pd.DataFrame({
            "Month": ["Jan", "Feb"],
            "CustomerCount": [100, 120]
        })
    },

    {
        "question": "Chart the multi-year trajectory of our profits",
        "expected": "line",
        "df": pd.DataFrame({
            "Year": [2023, 2024],
            "Profit": [10000, 12000]
        })
    },

    {
        "question": "Show the continuous timeline of revenue generation",
        "expected": "line",
        "df": pd.DataFrame({
            "Month": ["Jan", "Feb"],
            "Revenue": [1000, 2000]
        })
    },

    {
        "question": "Graph the chronological shifts in monthly product sales",
        "expected": "line",
        "df": pd.DataFrame({
            "Month": ["Jan", "Feb"],
            "Sales": [200, 250]
        })
    },

    {
        "question": "How does the territory revenue shift year over year?",
        "expected": "line",
        "df": pd.DataFrame({
            "Year": [2023, 2024],
            "Revenue": [5000, 7000]
        })
    },

    {
        "question": "Plot the over-time progression of quarterly item counts",
        "expected": "line",
        "df": pd.DataFrame({
            "Quarter": ["Q1", "Q2"],
            "Quantity": [100, 140]
        })
    },

    # ==================================================
    # RANKING (10)
    # ==================================================

    {
        "question": "List the top 10 buyers sorted by total sales value",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Customer": ["A", "B"],
            "Sales": [1000, 2000]
        })
    },

    {
        "question": "Rank the top 20 revenue-generating products",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Product": ["P1", "P2"],
            "Revenue": [5000, 7000]
        })
    },

    {
        "question": "Which specific item categories have the highest sales volume?",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Category": ["Bike", "Accessory"],
            "Sales": [3000, 1000]
        })
    },

    {
        "question": "Order the regions based on highest financial performance",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Revenue": [8000, 6000]
        })
    },

    {
        "question": "Identify the territories with the lowest revenue numbers",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Revenue": [2000, 6000]
        })
    },

    {
        "question": "Which 10 customers have spent the least amount of money?",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Customer": ["A", "B"],
            "Sales": [100, 200]
        })
    },

    {
        "question": "Compare and rank marketing campaigns by generated income",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Promotion": ["Promo1", "Promo2"],
            "Revenue": [1000, 2000]
        })
    },

    {
        "question": "Sort our product list by total profit margins",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Product": ["P1", "P2"],
            "Profit": [1000, 1500]
        })
    },

    {
        "question": "Find the highest producing sales areas",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Region": ["North", "South"],
            "Sales": [9000, 6000]
        })
    },

    {
        "question": "Create a leaderboard of account executives by deals closed",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Employee": ["John", "Mary"],
            "Sales": [4000, 5000]
        })
    },

    # ==================================================
    # CONTRIBUTION (7)
    # ==================================================

    {
        "question": "What fraction of overall revenue comes from each category?",
        "expected": "pie",
        "df": pd.DataFrame({
            "Category": ["A", "B"],
            "Revenue": [60, 40]
        })
    },

    {
        "question": "Display the regional split of our incoming revenue streams",
        "expected": "pie",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Revenue": [70, 30]
        })
    },

    {
        "question": "Show how total sales volume is divided among active promos",
        "expected": "pie",
        "df": pd.DataFrame({
            "Promotion": ["A", "B"],
            "Sales": [80, 20]
        })
    },

    {
        "question": "Visualize individual product shares within total earnings",
        "expected": "pie",
        "df": pd.DataFrame({
            "Product": ["P1", "P2"],
            "Revenue": [50, 50]
        })
    },

    {
        "question": "What is the category breakdown for incoming revenue?",
        "expected": "pie",
        "df": pd.DataFrame({
            "Category": ["A", "B"],
            "Revenue": [30, 70]
        })
    },

    {
        "question": "Graph the relative percentage allocation of revenue across regions",
        "expected": "pie",
        "df": pd.DataFrame({
            "Region": ["North", "South"],
            "Revenue": [45, 55]
        })
    },

    {
        "question": "Show the geometric breakdown of territory stakes in our gross sales",
        "expected": "pie",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Sales": [25, 75]
        })
    },

    # ==================================================
    # COMPARISON (8)
    # ==================================================

    {
        "question": "Contrast annual earnings figures across distinct territories",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Year": [2023, 2023],
            "Territory": ["East", "West"],
            "Revenue": [1000, 2000]
        })
    },

    {
        "question": "Graph a side-by-side view of monthly sales per segment",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Month": ["Jan", "Jan"],
            "Category": ["A", "B"],
            "Sales": [100, 200]
        })
    },

    {
        "question": "Juxtapose territory revenue splits across different campaign types",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Promotion": ["P1", "P2"],
            "Revenue": [1000, 1200]
        })
    },

    {
        "question": "Plot category sales data broken out by target year",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Category": ["Bike", "Accessory"],
            "Year": [2024, 2024],
            "Sales": [1000, 500]
        })
    },

    {
        "question": "Evaluate year-by-year profit margins between geographical sectors",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Year": [2023, 2023],
            "Territory": ["East", "West"],
            "Profit": [1000, 1500]
        })
    },

    {
        "question": "Display side-by-side product group performance for this quarter",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Quarter": ["Q1", "Q1"],
            "Category": ["A", "B"],
            "Sales": [100, 120]
        })
    },

    {
        "question": "Map out regional sales milestones relative to each fiscal year",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Year": [2024, 2024],
            "Revenue": [5000, 4000]
        })
    },

    {
        "question": "Compare financial gains from marketing events across multiple areas",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Promotion": ["P1", "P2"],
            "Region": ["North", "South"],
            "Revenue": [500, 700]
        })
    },

    # ==================================================
    # DISTRIBUTION (3)
    # ==================================================

    {
        "question": "What is the overall shape and spread of transaction sizes?",
        "expected": "histogram",
        "df": pd.DataFrame({
            "Sales": [10, 20, 30, 40, 50]
        })
    },

    {
        "question": "Plot a frequency binning of our typical checkout values",
        "expected": "histogram",
        "df": pd.DataFrame({
            "OrderAmount": [100, 150, 200, 250]
        })
    },

    {
        "question": "Show the density and concentration of client age groups",
        "expected": "histogram",
        "df": pd.DataFrame({
            "Age": [20, 25, 30, 35]
        })
    },

    # ==================================================
    # CORRELATION (3)
    # ==================================================

    {
        "question": "Does giving a higher markdown correspond to larger checkout sales?",
        "expected": "scatter",
        "df": pd.DataFrame({
            "Discount": [0, 5, 10],
            "Sales": [100, 90, 80]
        })
    },

    {
        "question": "Plot retail price points against the quantity of items purchased",
        "expected": "scatter",
        "df": pd.DataFrame({
            "Price": [10, 20, 30],
            "Quantity": [100, 70, 40]
        })
    },

    {
        "question": "Is there a measurable pattern between markdown levels and absolute revenue?",
        "expected": "scatter",
        "df": pd.DataFrame({
            "Discount": [0, 5, 10],
            "Revenue": [1000, 900, 800]
        })
    },

    # ==================================================
    # PHASE 4.1 NATURAL LANGUAGE STRESS TESTS
    # ==================================================

    # TREND

    {
        "question": "What directional patterns exist for income over consecutive periods?",
        "expected": "line",
        "df": pd.DataFrame({
            "Year": [2023, 2024],
            "Revenue": [1000, 1500]
        })
    },

    {
        "question": "Can you graph the progressive trajectory of sales across fiscal years?",
        "expected": "line",
        "df": pd.DataFrame({
            "Year": [2023, 2024],
            "Sales": [1000, 2000]
        })
    },

    {
        "question": "Give me a step-by-step breakdown of how earnings look each month",
        "expected": "line",
        "df": pd.DataFrame({
            "Month": ["Jan", "Feb"],
            "Revenue": [1000, 2000]
        })
    },

    {
        "question": "Are our gross income figures moving upward or downward?",
        "expected": "line",
        "df": pd.DataFrame({
            "Month": ["Jan", "Feb"],
            "Revenue": [1000, 1500]
        })
    },

    {
        "question": "Plot the monthly registration pace of our user base",
        "expected": "line",
        "df": pd.DataFrame({
            "Month": ["Jan", "Feb"],
            "CustomerCount": [100, 120]
        })
    },

    # RANKING

    {
        "question": "Identify our VIP accounts that yield the highest volume",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Customer": ["A", "B"],
            "Revenue": [5000, 7000]
        })
    },

    {
        "question": "Which specific client entries top our internal billing reports?",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Customer": ["A", "B"],
            "Revenue": [6000, 8000]
        })
    },

    {
        "question": "List the highest-spending customers from maximum to minimum",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Customer": ["A", "B"],
            "Revenue": [1000, 2000]
        })
    },

    {
        "question": "Which geographic zones are outperforming the rest?",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Revenue": [9000, 5000]
        })
    },

    {
        "question": "Isolate the most prominent regional groups by income metrics",
        "expected": "horizontal_bar",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Revenue": [7000, 4000]
        })
    },

    # CONTRIBUTION

    {
        "question": "Which merchandise clusters account for the bulk of gross receipts?",
        "expected": "pie",
        "df": pd.DataFrame({
            "Category": ["Bikes", "Accessories"],
            "Revenue": [80, 20]
        })
    },

    {
        "question": "What is the primary operational category feeding into overall metrics?",
        "expected": "pie",
        "df": pd.DataFrame({
            "Category": ["A", "B"],
            "Sales": [70, 30]
        })
    },

    {
        "question": "Divide total corporate proceeds dynamically across departments",
        "expected": "pie",
        "df": pd.DataFrame({
            "Category": ["A", "B"],
            "Revenue": [60, 40]
        })
    },

    {
        "question": "Plot the internal structural proportions making up total cash intake",
        "expected": "pie",
        "df": pd.DataFrame({
            "Category": ["A", "B"],
            "Revenue": [55, 45]
        })
    },

    {
        "question": "Display geographic territory presence using territorial market share",
        "expected": "pie",
        "df": pd.DataFrame({
            "Region": ["North", "South"],
            "Revenue": [65, 35]
        })
    },

    # COMPARISON

    {
        "question": "Contrast different regional boundaries side by side",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Territory": ["East", "West"],
            "Year": [2024, 2024],
            "Revenue": [1000, 1500]
        })
    },

    {
        "question": "Plot paired performance blocks for our primary segments",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Category": ["A", "B"],
            "Revenue": [1000, 1200]
        })
    },

    {
        "question": "Cross-analyze regional yield variations multi-annually",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Year": [2023, 2023],
            "Region": ["North", "South"],
            "Revenue": [1000, 1500]
        })
    },

    {
        "question": "Graph paired bars comparing regional incoming funds",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Region": ["East", "West"],
            "Revenue": [1000, 1200]
        })
    },

    {
        "question": "Juxtapose conversion metrics between distinct special deals",
        "expected": "grouped_bar",
        "df": pd.DataFrame({
            "Promotion": ["Promo1", "Promo2"],
            "Revenue": [1000, 1200]
        })
    },

    # DISTRIBUTION

    {
        "question": "What does the overall variance look like for total sales buckets?",
        "expected": "histogram",
        "df": pd.DataFrame({
            "Sales": [10, 20, 30, 40, 50]
        })
    },

    {
        "question": "Graph the dispersion range of client age demographics",
        "expected": "histogram",
        "df": pd.DataFrame({
            "Age": [20, 25, 30, 35, 40]
        })
    },

    {
        "question": "Map the recurrence rates of distinct ticket totals",
        "expected": "histogram",
        "df": pd.DataFrame({
            "OrderAmount": [100, 150, 200, 250, 300]
        })
    },

    # CORRELATION

    {
        "question": "Is there a direct link between discounting items and realized gains?",
        "expected": "scatter",
        "df": pd.DataFrame({
            "Discount": [0, 5, 10],
            "Revenue": [1000, 900, 800]
        })
    },

    {
        "question": "Do changes in item price directly dictate customer purchasing volumes?",
        "expected": "scatter",
        "df": pd.DataFrame({
            "Price": [10, 20, 30],
            "Quantity": [100, 70, 40]
        })
    },

    {
        "question": "Plot sticker price points relative to gross sales performance",
        "expected": "scatter",
        "df": pd.DataFrame({
            "Price": [10, 20, 30],
            "Sales": [1000, 800, 600]
        })
    },

    {
        "question": "Graph the visual interplay between shipping totals and overall income",
        "expected": "scatter",
        "df": pd.DataFrame({
            "Quantity": [10, 20, 30],
            "Revenue": [1000, 2000, 3000]
        })
    }
]

#new trial (88.24% accuracy)
# benchmark_cases = [

#     # ==================================================
#     # TREND (10)
#     # ==================================================

#     {
#         "question": "Can you plot how our revenue has behaved month over month?",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Provide a timeline view of our total annual revenue",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Year": [2023, 2024],
#             "Revenue": [10000, 15000]
#         })
#     },

#     {
#         "question": "Show the sequential movement of sales across quarters",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Quarter": ["Q1", "Q2"],
#             "Sales": [1000, 1500]
#         })
#     },

#     {
#         "question": "Trace the day-by-day fluctuation in incoming orders",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Date": ["2024-01-01", "2024-01-02"],
#             "Orders": [50, 75]
#         })
#     },

#     {
#         "question": "Graph the monthly momentum of our customer acquisitions",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "CustomerCount": [100, 120]
#         })
#     },

#     {
#         "question": "What does the historical timeline of our net profit look like?",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Year": [2023, 2024],
#             "Profit": [10000, 12000]
#         })
#     },

#     {
#         "question": "Map out the progression of revenue from start to finish",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Visualize the month-by-month evolution of product-specific sales",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Sales": [200, 250]
#         })
#     },

#     {
#         "question": "Draw a trendline for the territory's financial performance over the years",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Year": [2023, 2024],
#             "Revenue": [5000, 7000]
#         })
#     },

#     {
#         "question": "Chart the volume changes in order quantities every quarter",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Quarter": ["Q1", "Q2"],
#             "Quantity": [100, 140]
#         })
#     },

#     # ==================================================
#     # RANKING (10)
#     # ==================================================

#     {
#         "question": "Give me a breakdown of our 10 highest-value purchasers",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Customer": ["A", "B"],
#             "Sales": [1000, 2000]
#         })
#     },

#     {
#         "question": "Which 20 individual items generated the most cash?",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Product": ["P1", "P2"],
#             "Revenue": [5000, 7000]
#         })
#     },

#     {
#         "question": "Identify the top-grossing groups of products",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Category": ["Bike", "Accessory"],
#             "Sales": [3000, 1000]
#         })
#     },

#     {
#         "question": "Rank our geographic operations from maximum to minimum return",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Revenue": [8000, 6000]
#         })
#     },

#     {
#         "question": "Which regional sectors are struggling the most with incoming revenue?",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Revenue": [2000, 6000]
#         })
#     },

#     {
#         "question": "Show a list of the 10 accounts with the lowest transaction volume",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Customer": ["A", "B"],
#             "Sales": [100, 200]
#         })
#     },

#     {
#         "question": "Sort our promotional offers based on total revenue generated",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Promotion": ["Promo1", "Promo2"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Which specific items yield the healthiest profit figures?",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Product": ["P1", "P2"],
#             "Profit": [1000, 1500]
#         })
#     },

#     {
#         "question": "Create a comparison chart of the most lucrative sales zones",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Region": ["North", "South"],
#             "Sales": [9000, 6000]
#         })
#     },

#     {
#         "question": "Rank our sales staff by total value of deals finalized",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Employee": ["John", "Mary"],
#             "Sales": [4000, 5000]
#         })
#     },

#     # ==================================================
#     # CONTRIBUTION (7)
#     # ==================================================

#     {
#         "question": "How is our absolute revenue distributed percentage-wise among categories?",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Category": ["A", "B"],
#             "Revenue": [60, 40]
#         })
#     },

#     {
#         "question": "Show the exact proportional weight of each territory in our total earnings",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Revenue": [70, 30]
#         })
#     },

#     {
#         "question": "What slice of overall sales does each promotion account for?",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Promotion": ["A", "B"],
#             "Sales": [80, 20]
#         })
#     },

#     {
#         "question": "Illustrate how individual products build up our total bottom line",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Product": ["P1", "P2"],
#             "Revenue": [50, 50]
#         })
#     },

#     {
#         "question": "Display the category-specific makeup of our company's earnings",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Category": ["A", "B"],
#             "Revenue": [30, 70]
#         })
#     },

#     {
#         "question": "Show the regional composition mix for inbound cash flow",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Region": ["North", "South"],
#             "Revenue": [45, 55]
#         })
#     },

#     {
#         "question": "What is the territorial composition of our aggregate sales metrics?",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Sales": [25, 75]
#         })
#     },

#     # ==================================================
#     # COMPARISON (8)
#     # ==================================================

#     {
#         "question": "Present a side-by-side comparison of annual territory yields",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Year": [2023, 2023],
#             "Territory": ["East", "West"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Contrast category sales figures within each distinct month",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Jan"],
#             "Category": ["A", "B"],
#             "Sales": [100, 200]
#         })
#     },

#     {
#         "question": "Compare regional intake grouped alongside specific discount structures",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Promotion": ["P1", "P2"],
#             "Revenue": [1000, 1200]
#         })
#     },

#     {
#         "question": "Show product segments paired with their respective calendar years",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Category": ["Bike", "Accessory"],
#             "Year": [2024, 2024],
#             "Sales": [1000, 500]
#         })
#     },

#     {
#         "question": "Juxtapose regional profit margins side-by-side across consecutive years",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Year": [2023, 2023],
#             "Territory": ["East", "West"],
#             "Profit": [1000, 1500]
#         })
#     },

#     {
#         "question": "Cross-examine quarterly sales numbers between competing product families",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Quarter": ["Q1", "Q1"],
#             "Category": ["A", "B"],
#             "Sales": [100, 120]
#         })
#     },

#     {
#         "question": "Plot territorial outcomes juxtaposed by operational year",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Year": [2024, 2024],
#             "Revenue": [5000, 4000]
#         })
#     },

#     {
#         "question": "Compare campaign revenues side by side across distinct operational hubs",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Promotion": ["P1", "P2"],
#             "Region": ["North", "South"],
#             "Revenue": [500, 700]
#         })
#     },

#     # ==================================================
#     # DISTRIBUTION (3)
#     # ==================================================

#     {
#         "question": "Graph the concentration and density frequency of our raw transactions",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "Sales": [10, 20, 30, 40, 50]
#         })
#     },

#     {
#         "question": "How do our invoice totals cluster across different numeric ranges?",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "OrderAmount": [100, 150, 200, 250]
#         })
#     },

#     {
#         "question": "Display a frequency count of our buyer base by age brackets",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "Age": [20, 25, 30, 35]
#         })
#     },

#     # ==================================================
#     # CORRELATION (3)
#     # ==================================================

#     {
#         "question": "Is a larger percentage discount linked to an uptick in overall volume?",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Discount": [0, 5, 10],
#             "Sales": [100, 90, 80]
#         })
#     },

#     {
#         "question": "Examine the linear relationship between unit pricing and order quantities",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Price": [10, 20, 30],
#             "Quantity": [100, 70, 40]
#         })
#     },

#     {
#         "question": "Does adjusting the promotional markdown directly impact our final gross revenue?",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Discount": [0, 5, 10],
#             "Revenue": [1000, 900, 800]
#         })
#     },

#     # ==================================================
#     # PHASE 4.1 NATURAL LANGUAGE STRESS TESTS
#     # ==================================================

#     # TREND

#     {
#         "question": "What is the over-time historical trajectory of our total earnings?",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Year": [2023, 2024],
#             "Revenue": [1000, 1500]
#         })
#     },

#     {
#         "question": "Plot the multi-year timeline shifts in our sales figures",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Year": [2023, 2024],
#             "Sales": [1000, 2000]
#         })
#     },

#     {
#         "question": "Display the continuous month-by-month path of our financial pipeline",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Are our macro earnings trending positively or negatively right now?",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "Revenue": [1000, 1500]
#         })
#     },

#     {
#         "question": "Graph the ongoing expansion rate of our client accounts over time",
#         "expected": "line",
#         "df": pd.DataFrame({
#             "Month": ["Jan", "Feb"],
#             "CustomerCount": [100, 120]
#         })
#     },

#     # RANKING

#     {
#         "question": "Show me our primary heavy-hitting accounts by total volume",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Customer": ["A", "B"],
#             "Revenue": [5000, 7000]
#         })
#     },

#     {
#         "question": "Which commercial accounts stand out at the absolute top of our billing reports?",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Customer": ["A", "B"],
#             "Revenue": [6000, 8000]
#         })
#     },

#     {
#         "question": "Identify the high-tier clients sorted explicitly by spending amounts",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Customer": ["A", "B"],
#             "Revenue": [1000, 2000]
#         })
#     },

#     {
#         "question": "Which specific zones represent our highest-producing territories?",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Revenue": [9000, 5000]
#         })
#     },

#     {
#         "question": "Present a ranked leaderboard of regions sorting by absolute total earnings",
#         "expected": "horizontal_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Revenue": [7000, 4000]
#         })
#     },

#     # CONTRIBUTION

#     {
#         "question": "Which stock sectors are currently generating the largest chunk of incoming funds?",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Category": ["Bikes", "Accessories"],
#             "Revenue": [80, 20]
#         })
#     },

#     {
#         "question": "What operational segment serves as the main component for total metrics?",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Category": ["A", "B"],
#             "Sales": [70, 30]
#         })
#     },

#     {
#         "question": "Show the categorical share breakdown for corporate incoming value",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Category": ["A", "B"],
#             "Revenue": [60, 40]
#         })
#     },

#     {
#         "question": "Graph the proportional internal breakdown of our aggregate cash profile",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Category": ["A", "B"],
#             "Revenue": [55, 45]
#         })
#     },

#     {
#         "question": "Illustrate territorial performance using percentage-based market presence",
#         "expected": "pie",
#         "df": pd.DataFrame({
#             "Region": ["North", "South"],
#             "Revenue": [65, 35]
#         })
#     },

#     # COMPARISON

#     {
#         "question": "How do our separate geographic zones stack up against one another?",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Territory": ["East", "West"],
#             "Year": [2024, 2024],
#             "Revenue": [1000, 1500]
#         })
#     },

#     {
#         "question": "Display paired bar charts of inventory cluster performance side-by-side",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Category": ["A", "B"],
#             "Revenue": [1000, 1200]
#         })
#     },

#     {
#         "question": "Contrast different regional variations relative to their multi-year metrics",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Year": [2023, 2023],
#             "Region": ["North", "South"],
#             "Revenue": [1000, 1500]
#         })
#     },

#     {
#         "question": "Present a side-by-side bar visualization contrasting regional cash takes",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Region": ["East", "West"],
#             "Revenue": [1000, 1200]
#         })
#     },

#     {
#         "question": "Evaluate paired performance bars across individual marketing promotions",
#         "expected": "grouped_bar",
#         "df": pd.DataFrame({
#             "Promotion": ["Promo1", "Promo2"],
#             "Revenue": [1000, 1200]
#         })
#     },

#     # DISTRIBUTION

#     {
#         "question": "What is the statistical pattern and variability of our overall sales columns?",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "Sales": [10, 20, 30, 40, 50]
#         })
#     },

#     {
#         "question": "Show a visual grouping of the frequency spread of our customer ages",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "Age": [20, 25, 30, 35, 40]
#         })
#     },

#     {
#         "question": "Plot a density chart mapping the commonality of distinct order sizes",
#         "expected": "histogram",
#         "df": pd.DataFrame({
#             "OrderAmount": [100, 150, 200, 250, 300]
#         })
#     },

#     # CORRELATION

#     {
#         "question": "Does applying markdown values directly trigger changes in incoming funds?",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Discount": [0, 5, 10],
#             "Revenue": [1000, 900, 800]
#         })
#     },

#     {
#         "question": "Is there a strong statistical link between price adjustments and inventory movement?",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Price": [10, 20, 30],
#             "Quantity": [100, 70, 40]
#         })
#     },

#     {
#         "question": "Plot list prices against gross sales metrics to see if they track together",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Price": [10, 20, 30],
#             "Sales": [1000, 800, 600]
#         })
#     },

#     {
#         "question": "Analyze the visual coordination between overall units sold and total incoming cash",
#         "expected": "scatter",
#         "df": pd.DataFrame({
#             "Quantity": [10, 20, 30],
#             "Revenue": [1000, 2000, 3000]
#         })
#     }
# ]

passed = 0
failed = 0

for i, test in enumerate(
    benchmark_cases,
    start=1
):

    actual = (
        VisualizationRecommender
        .recommend(
            test["question"],
            test["df"]
        )
    )

    expected = test["expected"]

    print("\n" + "=" * 50)

    print(
        f"TEST {i}"
    )

    print(
        f"Question: {test['question']}"
    )

    print(
        f"Expected: {expected}"
    )

    print(
        f"Actual: {actual}"
    )

    if actual == expected:

        passed += 1

        print("PASS")

    else:

        failed += 1

        print("FAIL")

    


    print("\n")
print("=" * 50)

print(
    "FINAL REPORT"
)

print("=" * 50)

print(
    f"Passed: {passed}"
)

print(
    f"Failed: {failed}"
)

accuracy = (
    passed
    /
    len(benchmark_cases)
) * 100

print(
    f"Accuracy: {accuracy:.2f}%"
)