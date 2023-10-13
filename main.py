from classes.uiclasses import ConsoleUserInterface    
from classes.abclasses import AddressBook
from mainfunc import parser


def main():
    ui = ConsoleUserInterface()
    
    ab = AddressBook()
    
    ui.show_start_message()
    
    while True:
        message = ui.user_input("   >>> ")
        cmd, data = parser(ui, message)
        cmd(ui, *data)


if __name__ == "__main__":
    main()