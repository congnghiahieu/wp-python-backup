import logging


def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(filename)s:%(lineno)d:%(funcName)s %(levelname)s:%(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        # filename="mod-logging/run.log",
    )

    log = logging.getLogger("log")
    log.setLevel(logging.INFO)

    log.debug("This is a debug message")
    log.info("This is a info message")
    log.warning("This is a warning message")
    log.error("This is a error message")
    log.critical("This is a critical message")


if __name__ == "__main__":
    main()
