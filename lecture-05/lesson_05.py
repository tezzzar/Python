# Завдання 1
print("Завдання 1")


def find_product_sales(filename: str, product: str) -> None:
    """Функція для пошуку товарів в файлі"""
    try:
        with open(filename, "r") as file:
            # читає файл по одному рядку за раз
            for index, line in enumerate(file, start=1):
                # перетворює рядок в нижній регістр, роблячи його нечутливим
                if product.lower() in line.lower():
                    print(f"Line {index}: {line.strip()}")
                    return
        print(f"Product '{product}' not found in the file.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")


find_product_sales("lecture-05/sales.txt", "laptop")


print()

# Завдання 2
print("Завдання 2")


def insert_sentence_after_second_line(
    input_filename: str, output_filename: str, new_sentence: str
) -> None:
    """Функція відкриває файл input, записує його значення в lines, потім відкриває файл output та записує туди змінений вміст"""
    try:
        with open(input_filename, "r") as file:
            lines = file.read().splitlines()
        # якщо кількість рядків менше двох,нове речення буде додаватись в кінець файлу
        if len(lines) > 1:
            lines.insert(2, new_sentence)
        else:
            lines.append(new_sentence)

        with open(output_filename, "w") as file:
            file.write("\n".join(lines) + "\n")

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

        # Якщо файл порожній, всі значення будуть встановлені як 0
        if not text:
            num_lines = 0
            num_words = 0
            num_chars = 0
        else:
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
import sys


def calculate_square(number: int) -> int:
    """Calculate the square of a number."""
    return number**2


# функція "parse_arguments" перейменована на "setup_parser"
def setup_parser() -> argparse.ArgumentParser:
    """Setup command line argument parser."""
    parser = argparse.ArgumentParser(description="Calculate the square of a number.")
    parser.add_argument("number", type=int, help="display the square of a given number")
    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()
    # Перевірка що число є цілим
    try:
        result = calculate_square(args.number)
        print(f"The square of {args.number} is {result}")
    except ValueError:
        print("Ensure the input is an integer.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()


print()
