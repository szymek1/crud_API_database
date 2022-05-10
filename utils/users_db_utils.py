from data_utils import Items
from database_utils.databse_handler import DatabaseHandler


class UsersDatabase:
    """Class responsible for users database initialization"""
    def __init__(self) -> None:
        self.host_name = Items.database_configs['host']
        self.user_name = Items.database_configs['usr']
        self.password = Items.database_configs['password']
        self.db_name = Items.database_configs['db_name']

    def load_users(self) -> None:
        """Load users to Users table in the database"""
        db_handler = DatabaseHandler()
        user_dataframe = db_handler.make_pandas_dataframe(Items.users_config_json)

        engine = db_handler.create_sql_engine(Items.db_usrs_data)
        connect = db_handler.create_server_connection(
            host_name=self.host_name,
            user_name=self.user_name,
            passwd=self.password,
            db_name=self.db_name
        )

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
