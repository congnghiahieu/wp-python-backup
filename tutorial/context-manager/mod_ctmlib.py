""" Có thể tạo decorator context manager bằng hàm và generator """

from contextlib import contextmanager


@contextmanager
def file(filepath: str, open_mode: str):
    try:
        print("Enter")
        file = open(filepath, open_mode)
        yield file
    except FileNotFoundError as exce:
        print("Catch Exception")
        print(exce)
    finally:
        print("Exit")
        file.close()


with file("context-manager/text.txt", "w") as f:
    print("Center")
    f.write("Hello World")
    # raise FileNotFoundError("This is a handled exception")
    raise FileExistsError("This is a unhandled exception")
