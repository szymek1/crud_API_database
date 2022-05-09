import json

import pandas as pd
import pymysql
from sqlalchemy import create_engine

from utils.data_utils import Items


class UsersDatabase:
    """Class responsible for users database initialization"""

    def make_pandas_dataframe(self, path_to_users_json: str) -> pd.DataFrame:
        """Read users jsonfile and return it as pandas dataframe"""
        with open(path_to_users_json, "r") as usrs_json:
            usrs = json.load(usrs_json)

        users_df = pd.DataFrame(usrs['users'])

        return users_df

    def create_server_connection(self) -> pymysql.connect:
        """Creating connection to database"""
        conn = pymysql.connect(
            host=Items.database_configs['host'],
            user=Items.database_configs['usr'],
            password=Items.database_configs['password'],
            db=Items.database_configs['db_name']
        )

        return conn

    def load_users(self) -> None:
        """Load users to Users table in the database"""
        user_dataframe = self.make_pandas_dataframe(Items.users_config_json)

        engine = create_engine(Items.db_usrs_data)
        connect = self.create_server_connection()

        # cur = connect.cursor()
        user_dataframe.to_sql(Items.usrs_db_name, con=engine, if_exists='append', index=False)

        # cur.execute("SELECT * FROM Users")
        # output = cur.fetchall()

        # for i in output:
        #     print(i)

        connect.close()


if __name__ == '__main__':
    u = UsersDatabase()
    u.load_users()
