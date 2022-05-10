import json

import pandas as pd
import pymysql
import sqlalchemy
from sqlalchemy import create_engine


class DatabaseHandler:
    """Class responsible for database handling"""

    def make_pandas_dataframe(self, path_to_users_json: str) -> pd.DataFrame:
        """Read users jsonfile and return it as pandas dataframe"""
        with open(path_to_users_json, "r") as usrs_json:
            usrs = json.load(usrs_json)

        users_df = pd.DataFrame(usrs['users'])

        return users_df

    def create_server_connection(self, host_name: str, user_name: str, passwd: str, db_name: str) -> pymysql.connect:
        """Creating connection to database"""
        conn = pymysql.connect(
            host=host_name,
            user=user_name,
            password=passwd,
            db=db_name
        )

        return conn

    def create_sql_engine(self, db_usrs_data: str) -> sqlalchemy.create_engine:
        """Create engine for accessing database"""
        return create_engine(db_usrs_data)
