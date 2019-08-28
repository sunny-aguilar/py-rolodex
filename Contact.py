

class Contacts:
    def __init__(self, name, phone, email):
        self.__name = name

    def set_name(self, name):
        self.__phone = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_emails(self, email):
        self.__email = email

    # getters
    def get_name(self):
        return self.__name

