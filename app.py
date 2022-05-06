import json
import argparse

from utils.usr import User
from utils.validator import Validator


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

            usr_session = True
            operations_list = [1, 2, 3, 4, 5]
            while usr_session:
                print('Select number regarding operation you would like to perform:'
                      '\n1. add new contact'
                      '\n2. update contact'
                      '\n3. show contact list'
                      '\n4. remove contact'
                      '\n5. close session')

                operation = int(input('Chose operation: '))

                if operation in operations_list:
                    if operation == 1:
                        id_contact, phone_numb, name, surname = input('Type: id_contact, phone number, name, surname: ').split(', ', 4)
                        user.add_contact(
                            id_contact=id_contact,
                            phone_numb=phone_numb,
                            name=name,
                            surname=surname
                        )
                    if operation == 2:
                        contact_to_update = input('Type contact_id of contact to update: ')
                        user.update_contact(id_contact=contact_to_update)
                    if operation == 3:
                        user.show_all_contacts()
                    if operation == 4:
                        contact_to_remove = input('Type contact_id of contact to remove: ')
                        user.remove_contact(id_contact=contact_to_remove)
                    if operation == 5:
                        usr_session = user.disconnect_user()
                else:
                    print('Operation not found')

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
    main(args)
