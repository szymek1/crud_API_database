from pathlib import Path

from .data_utils import Items


class Validator:
    """Class with validation utilities for a given user"""
    @staticmethod
    def validate_usr(usr_id: str) -> bool:
        """Check if a given user exist by looking for their config json file"""
        return Path(Items.users_configs + f'{usr_id}.json').exists()

    @staticmethod
    def validate_api_key(true_api_key: str, given_api_key: str) -> bool:
        """Examine if a given api_key is the same as true api_key"""
        if given_api_key == true_api_key:
            return True
        else:
            return False
