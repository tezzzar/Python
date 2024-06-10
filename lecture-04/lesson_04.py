# Форматування виводу контактів:
# Контакти відображаються у вигляді таблиці з заголовками колонок "First Name", "Last Name", "Phone Number" для покращення читабельності списку контактів.

# Валідація вводу користувача:
# 1. Додано функцію validate_phone_number, яка перевіряє, чи відповідає номер телефону формату "380XXXXXXXXX".
# 2. Перевірка на заповненість полів при додаванні нового контакту.

# Повідомлення користувачу:
# 1. Інформування користувача про успішне додавання, оновлення або видалення контактів.
# 2. Повідомлення про помилки (наприклад, якщо номер телефону неправильний або контакт вже існує).

# Покращення логіки пошуку:
# 1. Логіка пошуку дозволяє знайти контакт як за повним іменем, так і за лише першим ім'ям.
# 2. Додано перевірку на наявність контактів перед оновленням або видаленням, щоб уникнути помилок.

# Виведення меню:
# 1. Виведення меню команд після кожної дії, щоб користувачі не забували про доступні опції.


contacts = []

contact = {"first_name": "john", "last_name": "doe", "phone_number": "380111234567"}

contacts.append(contact)

TITLE = "Your phone book"


def hello():
    print(f"Hi! It's me, {TITLE.upper()}")


def bye():
    print(f"Thanks for using {TITLE}")


def make_your_choice():
    return (
        input(f"\nPlease make your choice (l, a, u, r, h, or q) here>>> ")
        .strip()
        .lower()
    )


def help_me():
    print(
        """
    All that you can do:
        l : List existing contacts
        a : Add new contact
        u : Update existing contact
        r : Remove existing contact
        h : Print this help
        q : Exit
    """
    )


def contact_list():
    if contacts:
        # Вивід контактів у вигляді таблиці
        print(f"{'First Name':<15} {'Last Name':<15} {'Phone Number':<15}")
        print("-" * 45)
        for contact in contacts:
            print(
                f"{contact['first_name']:<15} {contact['last_name']:<15} {contact['phone_number']:<15}"
            )
    else:
        print("Your contact list is empty. Go back to menu to add a new contact.")


def validate_phone_number(phone_number):
    # Перевірка чи номер телефону відповідає формату
    if (
        len(phone_number) != 12
        or not phone_number.isdigit()
        or not phone_number.startswith("380")
    ):
        print(
            "Invalid phone number format. Please enter a valid phone number (format: 380XXXXXXXXX)."
        )
        return False
    return True


def add_contact():
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    phone_number = input("Enter phone number: ").strip()

    # Перевірка на заповненість полів і формат номеру телефону
    if not first_name or not last_name or not phone_number:
        print("All fields are required. Please try again.")
        return None

    if not validate_phone_number(phone_number):
        return None

    # Перевірка на унікальність контакту
    for contact in contacts:
        if (
            contact["first_name"] == first_name and contact["last_name"] == last_name
        ) or contact["phone_number"] == phone_number:
            print("Contact with this name or phone number already exists.")
            return None

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
    }
    return contact


def update_contact(contact):
    old_phone_number = contact["phone_number"]
    old_first_name = contact["first_name"]
    old_last_name = contact["last_name"]

    # Перевірка нового номеру телефону на правильність формату
    phone_number = (
        input(f"Edit phone number: ({old_phone_number}) => ").strip()
        or old_phone_number
    )
    if phone_number != old_phone_number and not validate_phone_number(phone_number):
        return contact  # Залишаємо старий номер телефону, якщо новий не валідний

    first_name = (
        input(f"Edit first name: ({old_first_name}) => ").strip() or old_first_name
    )
    last_name = input(f"Edit last name: ({old_last_name}) => ").strip() or old_last_name

    return {
        "first_name": first_name.lower(),
        "last_name": last_name.lower(),
        "phone_number": phone_number,
    }


def remove_contact(contact):
    index = contacts.index(contact)
    # Підтвердження видалення контакту
    confirm = (
        input("Are you sure you want to delete this contact? (y/n): ").strip().lower()
    )
    if confirm in ("yes", "y"):
        contacts.pop(index)
        print("Contact removed successfully.")


def lookup_contact(name):
    words = name.split()
    if len(words) == 2:
        first_name, last_name = words
    elif len(words) == 1:
        first_name = words[0]
        last_name = ""
    else:
        return None

    for d in contacts:
        if (
            d["first_name"] == first_name.lower()
            and d["last_name"] == last_name.lower()
        ):
            return d
        elif d["first_name"] == first_name.lower() and not last_name:
            return d
    return None


def main():
    hello()
    help_me()  # Виводення меню після привітання

    while True:
        choice = make_your_choice()
        if choice == "a":
            new_contact = add_contact()
            if new_contact:
                contacts.append(new_contact)
                print("Contact added successfully.")
        elif choice == "l":
            contact_list()
        elif choice == "u":
            name = input("What name are you looking for: ").strip()
            contact = lookup_contact(name)
            if contact:
                updated_contact = update_contact(contact)
                contact.update(updated_contact)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
        elif choice == "r":
            name = input("What name are you looking for: ").strip()
            contact = lookup_contact(name)
            if contact:
                remove_contact(contact)
            else:
                print("Contact not found.")
        elif choice == "q":
            bye()
            break
        else:
            help_me()


main()
