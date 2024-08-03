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

# Додатково:

# 1. Використовуйте послідовні правила іменування для імен функцій і змінних (наприклад, snake_case):
# Усі імена функцій та змінних приведені до формату snake_case.

# 2. Переконайтеся, що імена та телефонні номери введені користувачем правильно, надішліть повідомлення користувачеві, якщо це не так:
# Додана функція validate_phone_number, яка перевіряє формат номеру телефону.
# Перевірка введення імен та телефонного номеру у функції add_contact з відповідними повідомленнями користувачу.

# 3. Покращте підказки та повідомлення зворотнього зв’язку, щоб зробити роботу користувача більш інформативною:
# Додані детальні повідомлення зворотного зв'язку у випадку помилок (наприклад, якщо номер телефону неправильний або контакт вже існує).
# Повідомлення про успішне додавання, оновлення та видалення контактів.

# 4. Переконайтеся, що код правильно обробляє сценарій, коли немає контактів:
# Функція contact_list перевіряє наявність контактів і виводить відповідне повідомлення, якщо список контактів порожній.

# 5. Додайте коментарі та рядки документів для кращої читабельності та обслуговування:
# Додані коментарі до функцій і важливих частин коду для покращення читабельності та обслуговування.

contacts = []

TITLE = "Your phone book"


def hello():
    """Вітання користувача"""
    print(f"Hi! It's me, {TITLE.upper()}")


def bye():
    """Прощання з користувачем"""
    print(f"Thanks for using {TITLE}")


def make_your_choice():
    """Запит вибору дії у користувача"""
    return (
        input("\nPlease make your choice (l, a, u, r, h, or q) here>>> ")
        .strip()
        .lower()
    )


def help_me():
    """Виведення довідки про доступні команди"""
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
    """Виведення списку контактів"""
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
    """Перевірка чи номер телефону відповідає формату 380XXXXXXXXX"""
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


def validate_name(name):
    """Перевірка чи ім'я або прізвище складаються лише з букв і в нижньому регістрі"""
    if not name.isalpha() or not name.islower():
        print("Names and surnames must contain only letters and be in lowercase.")
        return False
    return True


def add_contact():
    """Додавання нового контакту"""
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    phone_number = input("Enter phone number: ").strip()

    # Перевірка на заповненість полів і формат номеру телефону
    if not first_name or not last_name or not phone_number:
        print("All fields are required. Please try again.")
        return None

    # Перевірка імені та прізвища
    if not validate_name(first_name) or not validate_name(last_name):
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
    """Оновлення існуючого контакту"""
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

    # Перевірка імені та прізвища
    if not validate_name(first_name) or not validate_name(last_name):
        return contact

    return {
        "first_name": first_name.lower(),
        "last_name": last_name.lower(),
        "phone_number": phone_number,
    }


def remove_contact(contact):
    """Видалення контакту"""
    index = contacts.index(contact)
    # Підтвердження видалення контакту
    confirm = (
        input("Are you sure you want to delete this contact? (y/n): ").strip().lower()
    )
    if confirm in ("yes", "y"):
        contacts.pop(index)
        print("Contact removed successfully.")


def lookup_contact(name):
    """Пошук контакту за ім'ям"""
    words = name.split()
    if len(words) == 2:
        first_name, last_name = words
    elif len(words) == 1:
        first_name = words[0]
        last_name = ""
    else:
        return None

    for contact in contacts:
        if (
            contact["first_name"] == first_name.lower()
            and contact["last_name"] == last_name.lower()
        ):
            return contact
        elif contact["first_name"] == first_name.lower() and not last_name:
            return contact
    return None


def main():
    """Головна функція програми"""
    hello()
    help_me()  # Виведення меню після привітання

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
        elif choice == "h":
            help_me()
        else:
            print("Invalid choice. Please try again.")
        help_me()  # Виведення меню після кожної дії


main()
