from collections import UserDict
from datetime import datetime as dt
import pickle as pckl
import re
import os

from classes.exceptionclasses import NoSuchPhone, InvalidFormat



class Contact():
    def __init__(self, surname):
        
        self.surname = surname
        self.name = ''
        self._phones = []
        self._birthday = ''
        self._email = ''
        self.address = ''

    def add_name(self, name):
        if name:
            self.name = name

    def add_phone(self, phones):
        if phones:
            print(phones)
            for phone in phones:
                self.phones = phone

    def add_email(self, email):
        if email:
            self.email = email

    def add_birthday(self, birthday):
        if birthday:
            self.birthday = birthday    

    def add_address(self, address):
        if address:
            self.address = address

    def update_surname(self, new_surname):
            self.surname = new_surname

    def update_name(self, new_name):
        if new_name:  
            self.name = new_name

    def update_phone(self, phones, *_):   
        if phones[0] in self._phones:
            self._phones.remove(phones[0])
            print(phones[1])
            self.phones = phones[1]
    
    def update_birthday(self, new_birthday):
        if new_birthday:
            self.birthday = new_birthday
    
    def update_email(self, new_email):
        if new_email:
            self.email = new_email

    def update_address(self, new_address):
        if new_address:
            self.address = new_address

    def __repr__(self) -> str:
        return '-' * 50 + f'\n\nSurname: {self.surname}\nName: {self.name}\nPhones: {", ".join(phone for phone in self.phones)}\nEmail: {self.email}\nBirthday: {self.birthday}\nAddress: {self.address}\n\n' + '-' * 50

    @property
    def phones(self):
        return self._phones

    @phones.setter
    def phones(self, phone: str):
        san_phone = re.sub(r'[-)( ]', '', phone)
        if re.match(r'^(\+?\d{1,2}[- ]?)?\d{10,15}$', san_phone) or san_phone == '':
            self._phones.append(san_phone)
        else:
            raise InvalidFormat(f"Invalid Phone format. Use 10 digits, please")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        if re.match(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email) or email == '':
            self._email = email 
        else:
            raise InvalidFormat(f"Invalid email format")

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, date):
        if re.match(r"[0-3][0-9][.|\\|/|-](([0][1-9])|([1][0-2]))[.|\\|/|-]\d{4}", date) or date == '': 
            self._birthday = date 
        else:
            raise InvalidFormat(f"Invalid Birthday format. Use -> dd.mm.yyyy")
    
    def __repr__(self) -> str:
        return '-' * 50 + f'\n\nSurname: {self.surname}\nName: {self.name}\nPhones: {", ".join(phone for phone in self.phones)}\nEmail: {self.email}\nBirthday: {self.birthday}\nAddress: {self.address}\n\n' + '-' * 50
    
def get_path(file_name):
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        return os.path.join(current_dir, f'../data/{file_name}')

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.notes = []

    def add_contact(self, ui , contact: Contact):
            self.data.update({contact.surname:contact})
            ui.show_green_message('This command will guide you through creating new contact:\n')
            ui.show_message(f'Surname: {contact.surname}')
            contact.add_name(ui.user_input('Name [Enter to skip]: '))
            contact.add_phone(ui.user_input('Phones space-separate [Enter to skip]: ').split())
            contact.add_birthday(ui.user_input('Birthday [Enter to skip]: '))
            contact.add_email(ui.user_input('Email [Enter to skip]: '))
            contact.add_address(ui.user_input('Address [Enter to skip]: '))
        

    def read_contact(self, name: str):
        pass


    def update_contact(self, ui, contact: Contact):
        ui.show_green_message('This command will guide you through updating contact:\n')
        new_surname = ui.user_input(f'Surname: {contact.surname} [Enter to skip]: ') 
        if new_surname in self.data:
            ui.show_red_message(f'{new_surname} already exists ')
            return
        elif new_surname:
            self.data[new_surname] = contact
            del self.data[contact.surname]
            contact.update_surname(new_surname)      
        contact.update_name(ui.user_input(f'Name: {contact.name} [Enter to skip]: '))
        contact.update_phone(ui.user_input(f'{contact.phones} type old number and new number to replace [Enter to skip]: ').split())
        contact.update_birthday(ui.user_input(f'Birthday: {contact.birthday} [Enter to skip]: '))
        contact.update_email(ui.user_input(f'Email: {contact.email} [Enter to skip]: '))
        contact.update_address(ui.user_input(f'Address: {contact.address} [Enter to skip]: '))


    def delete_contact(self, ui, contact: Contact):
        ui.show_red_message(f'Are you sure you want to delete the contact {contact.surname}?\n')
        if ui.user_input('Y/n:  ').lower() in ('y', 'yes'):
            del self.data[contact.surname]
            
    def nearby_birthday(self, ui, n):
        today = dt.now()
        nearby_contacts = []
        for contact in self.data.values():
            if contact.birthday:
                try:
                    birthdate = dt.strptime(contact.birthday, '%d.%m.%Y').replace(year=today.year)
                    days_until_birthday = (birthdate - today).days
                    if 0 <= days_until_birthday <= int(n):
                        nearby_contacts.append(contact)
                except ValueError:
                    pass
        if nearby_contacts:
            for contact in nearby_contacts:
                ui.show_message(contact)
        else:
            ui.show_red_message("No contact with birthday within your date.")

    def show_contacts(self):
        pass
    
    def delete_all(self, ui):
        ui.show_red_message('Are you sure you want to clear the address book?\n')
        if ui.user_input('Y/n:  ').lower() in ('y', 'yes'):
            self.data.clear()
            

    def log(self, action):
        time = dt.strftime(dt.now(), '%H:%M:%S')
        msg = f'[{time} {action}]'
        with open(get_path("logs.txt"), "a+") as file:
            file.write(f'{msg}\n')

    def save(self):
        with open(get_path("auto_save.bin"), "wb") as file:
            pckl.dump(self.data, file)
        self.log(f'AddressBook saved')
        with open(get_path("notes.bin"), "wb") as file:
            pckl.dump(self.notes, file)
        self.log(f'Notes saved')

    def load(self):
        try:
            with open(get_path("auto_save.bin"), "rb") as file:
                self.data = pckl.load(file)
        except FileNotFoundError:
            ...
        self.log(f'AddressBook loaded')
        try:
            with open(get_path("notes.bin"), "rb") as file:
                self.notes = pckl.load(file)
        except FileNotFoundError:
            ...
        self.log(f'Notes loaded')
        return self.data, self.notes

        
    


            
      