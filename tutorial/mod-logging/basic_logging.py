import logging


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")


if __name__ == "__main__":
    main()
