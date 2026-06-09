# sql_guard.py

import re


class SQLGuard:

    ALLOWED = [
        "SELECT",
        "SHOW",
        "DESCRIBE",
        "EXPLAIN",
        "WITH"
    ]

    FORBIDDEN = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "TRUNCATE",
        "ALTER",
        "CREATE",
        "REPLACE",
        "GRANT",
        "REVOKE"
    ]

    @classmethod
    def validate(cls, sql: str):

        if not sql:
            raise ValueError("Empty SQL query")

        sql_upper = sql.upper()

        for keyword in cls.FORBIDDEN:

            pattern = rf"\b{keyword}\b"

            if re.search(pattern, sql_upper):

                raise ValueError(
                    f"Forbidden SQL detected: {keyword}"
                )

        first_word = sql_upper.strip().split()[0]

        if first_word not in cls.ALLOWED:

            raise ValueError(
                f"Only read-only queries are allowed. Found: {first_word}"
            )

        return True