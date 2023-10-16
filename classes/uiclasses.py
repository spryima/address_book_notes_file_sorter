import os


    

class ConsoleUserInterface():
    help_message = """
                        List of all commands:
help   - show this list


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
        ConsoleUserInterface.show_green_message('                 "ADDRESS BOOK"')