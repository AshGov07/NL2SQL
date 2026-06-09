# # from sql_repair import SQLRepair

# # tables = [
# #     "customer",
# #     "payment",
# #     "rental",
# #     "film",
# #     "inventory"
# # ]

# # print(
# #     SQLRepair.closest_match(
# #         "custmer",
# #         tables
# #     )
# # )



# from sql_repair import SQLRepair

# # tables = [
# #     "customer",
# #     "payment",
# #     "rental",
# #     "film",
# #     "inventory",
# #     "category"
# # ]

# # sql = """
# # SELECT *
# # FROM customers c
# # JOIN payments p
# # ON c.customer_id = p.customer_id
# # """

# # repaired = SQLRepair.repair_table_names(
# #     sql,
# #     tables
# # )

# # print(repaired)


# columns = [
#     "customer_id",
#     "first_name",
#     "last_name",
#     "email",
#     "address_id"
# ]

# print(
#     SQLRepair.repair_column_name(
#         "custmer_id",
#         columns
#     )
# )

# print(
#     SQLRepair.repair_column_name(
#         "frist_name",
#         columns
#     )
# )

# print(
#     SQLRepair.repair_column_name(
#         "emial",
#         columns
#     )
# )




# from sql_repair import SQLRepair

# columns = [
#     "customer_id",
#     "first_name",
#     "last_name",
#     "email",
#     "address_id"
# ]

# sql = """
# SELECT custmer_id,
#        frist_name,
#        emial
# FROM customer
# """

# print(
#     SQLRepair.repair_column_references(
#         sql,
#         columns
#     )
# )



from sql_repair import SQLRepair

tables = [
    "customer",
    "payment",
    "rental",
    "film"
]

columns = [
    "customer_id",
    "first_name",
    "last_name",
    "email"
]

sql = """
SELECT custmer_id,
       frist_name
FROM customers
WHERE emial IS NOT NULL
"""

repaired_sql = SQLRepair.repair_sql(
    sql,
    tables,
    columns
)

print(repaired_sql)