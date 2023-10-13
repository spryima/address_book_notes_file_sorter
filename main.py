from classes.uiclasses import ConsoleUserInterface    
from mainfunc import parser


def main():
    ui = ConsoleUserInterface()
    ui.show_start_message()


    while True:
        message = ui.ask_question_input("   >>> ")
        cmd, data = parser(message)
        cmd(ui, *data)


if __name__ == "__main__":
    main()