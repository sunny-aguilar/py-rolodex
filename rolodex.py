# #rolodex concept

import Contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'

def main():
    mycontacts = load_contacts()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(mycontact)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)


save_contacts(mycontacts)


def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')
        contact_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        contact_dct = {}

    return contact_dct

def get_menu_choice():
    print()
    print('Menu')
    print('-----------------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')

    choice = int(input('Enter your choice: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice


def load_contacts():
    input_file = open(FILENAME, 'rb')

    contact_dct = pickle.load(input_file)

    input_file.close()

    except IOError:
        contact_dct = {}

    return contact_dct

