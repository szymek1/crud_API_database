from .utilities import Utilities


class Validator:
    """Class responsible for validation if certain user can access database"""
    @staticmethod
    def validate_usr(usr_id: str) -> bool:
        """Check if a given user exist by looking for their directory"""
        return Utilities.is_usr_directory(user_id=usr_id)

    @staticmethod
    def validate_api_key(true_api_key: str, given_api_key: str) -> bool:
        """Examine if a given api_key is the same as true api_key"""
        if given_api_key == true_api_key:
            return True
        else:
            return False
