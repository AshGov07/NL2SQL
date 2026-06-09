import re


class CTEHelper:

    @staticmethod
    def extract_cte_names(sql):

        cte_names = set()

        matches = re.findall(
            r'with\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+as',
            sql,
            re.IGNORECASE
        )

        for name in matches:
            cte_names.add(
                name.lower()
            )

        chained_matches = re.findall(
            r',\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+as',
            sql,
            re.IGNORECASE
        )

        for name in chained_matches:
            cte_names.add(
                name.lower()
            )

        return cte_names