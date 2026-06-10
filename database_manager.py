from sqlalchemy import create_engine


class DatabaseManager:

    def __init__(self, connection_string):

        self.engine = create_engine(
            connection_string
        )

    def get_engine(self):
        return self.engine