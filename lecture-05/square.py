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
