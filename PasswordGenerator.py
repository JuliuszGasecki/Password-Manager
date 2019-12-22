import UserCommands as static
import random

class Password_generator:
    def __check_statement(self, info):
        input_value = input(info)
        if input_value.upper() == static.yes_long:
            return 1
        if input_value.upper() == static.yes_short:
            return 1
        if input_value.upper() == static.no_long:
            return 0
        if input_value.upper() == static.no_short:
            return 0
        print(static.get_wrong_value_set_chars)
        self.__check_statement(info)

    def __set_password_characetrs(self, statement, value):
        if(statement):
            return value
        return ''

    def __set_password_lenght(self):
        value =int(input(static.getPassLen))
        if value <= 0 or value > 255:
            print(static.get_wrong_value_set_chars)
            return self.__set_password_lenght()
        else:
            return value

    def __create_password(self, len, chars):
        value = "".join(random.sample(chars, len))
        print(value)
        statement = self.__check_statement(static.get_accept_text)
        if statement == 1:
            return value
        return self.__create_password(len, chars)
    def generate_password(self):
        lowercase_letters ="abcdefghijklmnopqrstuvwxyz"
        uppercase_letters ="ABCDEfFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        special_chars = "!@#$%^&*()?"

        is_lowercase_letters = bool("true")
        is_uppercase_letters = self.__check_statement(static.getUpperCase)
        is_numbers = self.__check_statement(static.getNumbers)
        is_special_chars = self.__check_statement(static.getSpecial)

        password_characters = self.__set_password_characetrs(is_lowercase_letters, lowercase_letters)
        password_characters += self.__set_password_characetrs(is_uppercase_letters, uppercase_letters)
        password_characters += self.__set_password_characetrs(is_numbers, numbers)
        password_characters += self.__set_password_characetrs(is_special_chars, special_chars)
        password_lengh = self.__set_password_lenght()

        generated_password = self.__create_password(password_lengh, password_characters)
        print(static.accepted_password + generated_password)
        return generated_password

