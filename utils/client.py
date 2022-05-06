from abc import ABC, abstractmethod


class Client(ABC):
    """Abstract class for defining methods for interacting with contact from user's contact list"""

    @abstractmethod
    def add_contact(self, id_contact: str, phone_numb: str, name: str, surname: str) -> None:
        """Add contact to the contact list of a user"""
        raise NotImplementedError

    @abstractmethod
    def remove_contact(self, id_contact: str) -> None:
        """Remove contact from user list"""
        raise NotImplementedError

    @abstractmethod
    def update_contact(self, id_contact: str) -> None:
        """Update contact from contact list; Only possible to update 1 or more fields"""
        raise NotImplementedError

    @abstractmethod
    def show_all_contacts(self) -> None:
        """Show all contacts of a given user"""
        raise NotImplementedError

    @abstractmethod
    def disconnect_user(self) -> bool:
        """End user's session"""
        raise NotImplementedError
