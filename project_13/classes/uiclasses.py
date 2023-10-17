import os


    

class ConsoleUserInterface():
    help_message = """
                        List of all commands:
'add', '+' - adding a new contact to the address book
'change' - changing an existing contact
'find' - searching for contacts by the entered text in a property value
'del', 'delete', 'remove' - delete a contact from the address book
'delete all', 'remove all', 'clean' - complete cleaning of the address book
'show all', 'show' - display of all contacts in the address book
'sort' - sorting files in directories
'exit', 'quit', 'goodbye',  '.'  - completion of work with the address book, automatic saving of changes made
'find tag' - searching for notes by the entered tag 

The Address Book contact has the following properties:
 - surname (str),
 - name (str),
 - phones (list of str),
 - email (str),
 - birthday (date),
 - address (str)

"""
    
    @staticmethod
    def show_green_message(text):
        print(f'\033[92m{text}\033[0m', end="\n")
    
    @staticmethod
    def show_red_message(text):
        print(f'\033[91m{text}\033[0m', end="\n")
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def user_input(self, message=''):
        answer = input(message)
        return answer
    
    def show_message(self, message):
        print(message)

    def show_help(self):
        print(self.help_message)

    def show_start_message(self):
        ConsoleUserInterface.clear_screen()
        hello_message = '''                 "PROGRAMMULINKA"
        What's up buddy!
        I will be your assistant!'''
        ConsoleUserInterface.show_green_message(hello_message)
        
