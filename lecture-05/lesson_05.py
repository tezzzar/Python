# Завдання 1
print("Завдання 1")


def find_product_sales(filename, product):
    """Функція для пошуку товарів в файлі"""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        for index, line in enumerate(lines, start=1):
            if product in line:
                print(f"Line {index}: {line.strip()}")
                return
        print(f"Product '{product}' not found in the file.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")


find_product_sales("lecture-05/sales.txt", "laptop")

print()

# Завдання 2
print("Завдання 2")


def insert_sentence_after_second_line(input_filename, output_filename, new_sentence):
    """Функція відкриває файл, додає нове речення і записує в новий файл"""
    try:
        with open(input_filename, "r") as file:
            lines = file.read().splitlines()

        if len(lines) > 1:
            lines.insert(2, new_sentence)

        with open(output_filename, "w") as file:
            for line in lines:
                file.write(line + "\n")
        print("New sentence inserted successfully.")
    except FileNotFoundError:
        print(f"The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


new_sentence = "If Peter Piper picked a peck of pickled peppers."
insert_sentence_after_second_line(
    "lecture-05/input.txt", "lecture-05/output.txt", new_sentence
)

print()

# Завдання 3
print("Завдання 3")

from pathlib import Path


def file_stats():
    """Ця функція відкриває файл з заданим шляхом і підраховує кількість строк, слів та символів"""
    file_path = "lecture-05/input.txt"
    path = Path(file_path)

    try:
        text = path.read_text()
        num_lines = text.count("\n") + 1
        num_words = len(text.split())
        num_chars = len(text)

        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_stats()

print()

# Завдання 4
print("Завдання 4")

import argparse


def calculate_square(number):
    """Calculate the square of a number."""
    return number**2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="Number to square")

    args = parser.parse_args()

    result = calculate_square(args.number)
    print(f"The square of {args.number} is {result}")


if __name__ == "__main__":
    main()

print()
