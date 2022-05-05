import json
from datetime import datetime
from collections import defaultdict

from .client import Client
from .utilities import Utilities
from .data_utils import Items


class User(Client):
    """Class for interacting with contacts"""
    def __init__(self, user_id: str):
        self.id = user_id

    def add_contact(self, id_contact: str, phone_numb: str, name: str, surname: str) -> None:
        """Add contact to the contact list of a user"""
        current_date = str(datetime.now())

        if not Utilities.is_usr_directory(self.id):
            Utilities.make_usr_dir(self.id)

        new_contact = {
            'id_contact': id_contact,
            'phone_numb': phone_numb,
            'name': name,
            'surname': surname,
            'created at': current_date
        }
        with open(Items.users_rootdir + self.id + f'/{id_contact}.json', 'w') as contact:
            json.dump(new_contact, contact)
            self.add_new_contact_to_list(id_contact)

    def add_new_contact_to_list(self, id_contact: str) -> None:
        """
        Check if contact list for a given user exists, if so then add new contact to it,
        else, create that file and then add contact
        """
        if Utilities.is_contact_list(self.id):
            with open(Items.users_rootdir + self.id + f'/{self.id}_contact_list.json', 'r+') as c_list:
                contact_list = json.load(c_list)
                contact_list['current contacts'].append(id_contact)
                json.dump(contact_list, c_list)
        else:
            with open(Items.users_rootdir + self.id + f'/{self.id}_contact_list.json', 'w') as c_list:
                contact_list = defaultdict(list)
                contact_list['current contacts'].append(id_contact)
                json.dump(contact_list, c_list)

    def remove_contact(self, id_contact: str) -> None:
        """Remove contact from user list"""
        if Utilities.is_contact_file(self.id, id_contact):
            Utilities.rmv_contact(self.id, id_contact)
            Utilities.rmv_contact_from_contact_list(self.id, id_contact)
            print(f'Contact: {id_contact} was successfully removed')
        else:
            print('No such contact')

    def update_contact(self, id_contact: str) -> None:
        """Update contact from contact list; Only possible to update 1 or more fields"""
        def get_choice(number: int) -> str:
            switcher = {
                1: 'phone_numb',
                2: 'name',
                3: 'surname',
                4: 'close edition'
            }
            return switcher.get(number, 'nothing')

        edition_on = True

        if Utilities.is_contact_file(self.id, id_contact):
            while edition_on:
                print('Select number related to contact data you would like to change:'
                      '\n1. phone_numb'
                      '\n2. name'
                      '\n3. surname'
                      '\n4. close edition')

                choice = input('Type here: ')
                choice = get_choice(number=int(choice))

                if choice != 'nothing':
                    if choice != 'close edition':
                        with open(Items.users_rootdir + self.id + f'/{id_contact}.json', 'r+') as contact:
                            contact_updated = json.load(contact)
                            new_content = input(f'Type here new value for {choice}: ')
                            contact_updated[choice] = new_content
                            contact.seek(0)
                            json.dump(contact_updated, contact, indent=4)
                            contact.truncate()
                    else:
                        edition_on = False
                        print('Edition closed')
                else:
                    print('No such position to edit')
        else:
            print('No such contact')

    def show_all_contacts(self) -> None:
        """Show all contacts of a given user"""
        if Utilities.is_contact_list(self.id):
            with open(Items.users_rootdir + self.id + f'/{self.id}_contact_list.json', 'r+') as c_list:
                all_contacts = json.load(c_list)
                all_contacts = all_contacts['current contacts']

                print(f'Current contacts of user: {self.id}\n')
                for contact in all_contacts:
                    print(contact)

    def disconnect_user(self) -> None:
        """End user's session"""
        print('Ending session')
