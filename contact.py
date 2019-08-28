

class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    #
    def set_name(self, name):
        self.__phone = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_emails(self, email):
        self.__email = email

    # getters
    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_emails(self):
        return self.__email


    def __str(self):
        return 'Name: ' + self.name + \
                '\nPhone: ' + self.__phone + \
                '\nEmail: ' + self.__email




