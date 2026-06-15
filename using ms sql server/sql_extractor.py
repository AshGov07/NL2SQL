# import re


# class SQLExtractor:

#     @staticmethod
#     def extract(text):

#         # SQL inside markdown block

#         match = re.search(
#             r"```sql\s*(.*?)```",
#             text,
#             re.IGNORECASE | re.DOTALL
#         )

#         if match:

#             return match.group(1).strip()

#         # First SELECT statement

#         match = re.search(
#             r"(select[\s\S]*?;)",
#             text,
#             re.IGNORECASE
#         )

#         if match:

#             return match.group(1).strip()

#         # First WITH statement

#         match = re.search(
#             r"(with[\s\S]*?;)",
#             text,
#             re.IGNORECASE
#         )

#         if match:

#             return match.group(1).strip()

#         return text.strip()





import re

class SQLExtractor:

    @staticmethod
    def extract(text):

        # ----------------------------------
        # SQL inside markdown block
        # ----------------------------------

        match = re.search(
            r"```sql\s*(.*?)```",
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            return match.group(1).strip()

        # ----------------------------------
        # WITH statement fallback
        # ----------------------------------
        match = re.search(
            r"(with[\s\S]*?;)",
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

        # ----------------------------------
        # SELECT statement fallback
        # ----------------------------------

        match = re.search(
            r"(select[\s\S]*?;)",
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

        return text.strip()