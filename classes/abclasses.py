from collections import UserDict
from datetime import datetime


class Contact():
    def __init__(self, name, surname='', phone='', birthday=None, email=''):
        self.name = name
        self.surname = surname
        self.phones = []
        self.birthday = None
        self.email = email
        if phone:
            self.phones.append(phone)
        if birthday:
            try:
                self.birthday = datetime.strptime(birthday, "%d.%m.%Y").date()
            except ValueError:
                raise ValueError("Invalid birthday format (should be 'DD.MM.YYYY')")
        
        
        def read_surname(self):
            pass


        def update_surname(self, value: str):
            pass

    
        def read_birthday(self):
            pass


        def update_birthday(self, value: str):
            pass

    
        def read_email(self):
            pass


        def update_email(self, value: str):
            pass

    
        def add_phone(self, value: str):
            pass


        def read_phones(self):
            pass


        def update_phone(self, current_phone: str, new_phone: str):
            pass

    
        def delete_phone(self, value: str):
            pass
    


class AddressBook(UserDict):
    
    def add_contact(self, contact: Contact):
        self.data.update({contact.name:contact})
    

    def read_contact(self, name: str):
        pass


    def update_contact(self, contact: Contact):
        pass

    
    def delete_contact(self, name):
        if name in self.data:
            del self.data[name]
    
    
    def show_contacts(self):
        pass

    
    

            
      