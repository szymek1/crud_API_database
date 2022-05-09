from dataclasses import dataclass


@dataclass
class Items:
    """Class which stores importnt variables, paths etc.."""

    # ______paths_______________________
    users_rootdir: str = '/home/szymon_kubuntu/Documents/myProjects/Be_crudAPI-copy/users/'
    users_configs: str = '/home/szymon_kubuntu/Documents/myProjects/Be_crudAPI-copy/configs/'
    users_config_json: str = '/home/szymon_kubuntu/Documents/myProjects/Be_crudAPI-copy/users/users_config.json'

    # ______database management_________
    database_configs = {
        'host': 'localhost',
        'port': '3306',
        'usr': 'szymon',
        'password': '',
        'db_name': 'be_api'
    }
    db_usrs_data: str = 'mysql+pymysql://' + database_configs['usr'] + '@' + database_configs['host']\
                   + ':' + database_configs['port'] + '/' + database_configs['db_name']
    usrs_db_name: str = 'Users'
    clients_db_name: str = 'Clients'
