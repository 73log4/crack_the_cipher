
class CipherTemplate:

    def __init__(self, level):
        self.level = level

        self.print_welcome_message()

    @staticmethod
    def print_message(mes):
        print(mes)

    @staticmethod
    def error(error_mes):
        exit("Cipher Error: " + error_mes)

    def print_welcome_message(self):
        print(f"---------- Welcome to level {self.level} ----------\n")

    def print_congratulations_message(self):
        print(f"\nCongratulations! you cracked level {self.level}!")

    def cracked(self):
        self.print_congratulations_message()
        exit()
