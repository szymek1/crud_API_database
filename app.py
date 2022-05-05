import json
import argparse

from utils.usr import User
from utils.validator import Validator

"""
new_usr_data = {
    'id_contact': '123',
    'phone_numb': '600462504',
    'name': 'Szymon',
    'surname': 'Bogus'
}

user.add_contact(id_contact=new_usr_data['id_contact'], phone_numb=new_usr_data['phone_numb'],
                 name=new_usr_data['name'], surname=new_usr_data['surname'])

user.show_all_contacts()

user.update_contact(id_contact=new_usr_data['id_contact'])

user.remove_contact(id_contact=new_usr_data['id_contact'])
"""


def get_choice(number: int) -> str:
    switcher = {
        1: '',
        2: 'name',
        3: 'surname',
        4: 'close edition'
    }
    return switcher.get(number, 'nothing')


def main(arguments):

    user_id = arguments.user_id
    given_key = arguments.api_key

    user_path = '/home/szymon_kubuntu/Documents/myProjects/Be_crudAPI-copy/configs/' + user_id + '.json'

    if Validator.validate_usr(user_id):
        with open(user_path, 'r') as f:
            usr_data = json.load(f)

        true_key = usr_data['api_key']
        if Validator.validate_api_key(true_api_key=true_key, given_api_key=given_key):
            user = User(user_id=user_id)
            # add function(decorator would be cool) for deciding which class method to use
        else:
            print('Incorrect api_key')
            exit()
    else:
        print(f'User: {user_id} not found')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline for accessing database with contacts.\nTo proceed"
                                                 "user has to authenticate their permission with api key.",
                                     argument_default=argparse.SUPPRESS, allow_abbrev=False, add_help=False)
    parser.add_argument("--user_id", type=str, help="type user_id which will allow to identify user in database")
    parser.add_argument("--api_key", type=str, help="give api_key to authenticate")
    parser.add_argument("-h", "--help", action="help", help="Display this message.\nAlways check user_id and api_key.")

    args = parser.parse_args()
