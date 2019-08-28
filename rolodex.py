# #rolodex concept

import Contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4

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


save_contatrs(mycontacts)



