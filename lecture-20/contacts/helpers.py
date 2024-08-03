
"""Contacts entry point script"""
def help_me():
    """Informapin"""

    print("""
    All that You can do:      
        l : List existing contacts
        a : Add new contact
        u : Update existing contact
        r : Remove existing contact
        h : Print this help
        q : Exit
    """)
def hello(TITLE):
    print(F"Hi! It's me, {TITLE.upper()}")


def bye(TITLE):
    print(F"Thanks for using {TITLE}")


def make_your_choice():
    return input(f"Please make Your choice (l,a,u,r,h or q ) here>>> ")

if __name__ == "__main__":
    print("hello helpers modile")
    help_me()
