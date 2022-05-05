import os
import json
from pathlib import Path

from .data_utils import Items


class Utilities:
    """Class supplying with utilities functionalities"""

    @staticmethod
    def is_usr_directory(user_id: str) -> bool:
        """Check if directory for a specific user exists"""
        return Path(Items.users_rootdir + user_id).exists()

    @staticmethod
    def is_contact_file(user_id: str, id_contact: str) -> bool:
        """Check if a given contact has its file"""
        return Path(Items.users_rootdir + user_id + f'/{id_contact}.json').exists()

    @staticmethod
    def is_contact_list(user_id: str) -> bool:
        """Check if a contact list of a given user has its file"""
        return Path(Items.users_rootdir + user_id + f'/{user_id}_contact_list.json').exists()

    @staticmethod
    def rmv_contact(user_id: str, id_contact: str) -> None:
        """Remove a given contact"""
        Path(Items.users_rootdir + user_id + f'/{id_contact}.json').unlink()

    @staticmethod
    def rmv_contact_from_contact_list(user_id: str, id_contact: str) -> None:
        """Remove contact_id from contact list of a given user"""
        if Utilities.is_contact_list(user_id):
            with open(Items.users_rootdir + user_id + f'/{user_id}_contact_list.json', 'r+') as c_list:
                contact_list = json.load(c_list)
                contact_list['current contacts'].remove(id_contact)
                c_list.seek(0)
                json.dump(contact_list, c_list)
                c_list.truncate()
        else:
            print(f'Contact list for user: {user_id} not found')

    @staticmethod
    def make_usr_dir(user_id: str) -> None:
        """Create a directory for a given user to store there contacts"""
        os.mkdir(Items.users_rootdir + user_id)
