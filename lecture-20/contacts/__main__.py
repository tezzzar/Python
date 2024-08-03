"""Contacts entry point script"""
from contacts import helpers, TITLE, DATABASE
import argparse
# from helpers import help_me as h
def main():
    helpers.hello(TITLE)
    # save_contact(contacts)
    # contacts = load_contact()

    while True:
        match helpers.make_your_choice():
            case 'a':
                pass
                # new_contact = add_contact()
                # contacts.append(new_contact)
                # save_contact(contacts)

            case 'l':
                pass

                # contact_list(contacts)

            case 'u':
                pass
                # name = input("What name You looking for: ")
                # contact = lookup_contact(name)
                # # print(contact)
                # contact.update(update_contact(contact))

            case 'r':
                pass
                # name = input("What name You looking for: ")
                # contact = lookup_contact(contacts, name)
                # remove_contact(contacts, contact)

            case 'q':
                helpers.bye(TITLE)
                break
            case _:
                helpers.help_me()


if __name__ == "__main__":
    # print("hello Main modile")
    # helpers.help_me()
    # print(dir(helpers))
    # print(helpers.__file__)
    # print(dir(helpers.help_me))
    # print(helpers.__file__)
    # print(helpers.__name__)
    # print(helpers.__doc__)
    # help_me()

    # h()
    parser = argparse.ArgumentParser(
        prog="Phone book",
        description="List of my contacts",
        epilog="Thanks for using %(prog)s! :)"
    )
    parser.add_argument("path")
    args = parser.parse_args()

    general = parser.add_argument_group("General output")

    general.add_argument(
        "path",
        nargs="?",
        default="db.pkl",
        help="Take the path to the target database file (default: %(q)s)"
    )
    parser.parse_args()
    # print(args)



    main()