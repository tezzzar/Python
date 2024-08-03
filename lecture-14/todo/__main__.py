"""Todo entry point script"""

import logging
from todo import cli

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode="w",
    format="%(process)d - %(name)s - %(levelname)s - %(message)s - %(asctime)s",
)


def main() -> None:
    """Main function to run the CLI application and log various messages."""
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")
    cli.app()


if __name__ == "__main__":
    main()
