# test_aliases.py

from query_validator import QueryValidator

sql = """
SELECT c.customerName
FROM customers c
"""

aliases = QueryValidator.extract_aliases(
    sql.lower()
)

print(aliases)