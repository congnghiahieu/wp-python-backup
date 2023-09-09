# Custom tham số dòng lệnh
# python .\cli\cli_argparse.py --color blue
# python .\cli\cli_argparse.py -h
# choices: Chỉ chấp nhận tham số đầu vào là 1 trong các giá trị nằm trong set
# help: Thông tin hiện lên khi ta sử dụng --help (-h)

import argparse

parser = argparse.ArgumentParser(
    description="This is a program prints the name of my dog"
)
parser.add_argument(
    "-c",
    "--color",
    metavar="color",
    choices=["red", "blue", "green"],
    required=True,
    help="The color to search for",
)
args = parser.parse_args()
print(args.color)


def greeting(name: str, lang: str):
    langs = {
        "Vietnam": "Xin chào",
        "English": "Hello",
        "China": "Ni hao",
        "French": "Bonjoure",
    }
    print(f"{langs[lang]} {name}")


parser = argparse.ArgumentParser(description="This is a command line tool for greeting")
parser.add_argument(
    "-n", "--name", metavar="name", required=True, help="Any name in string"
)
parser.add_argument(
    "-l",
    "--lang",
    metavar="lang",
    required=True,
    choices=["Vietnam", "English", "China", "French"],
    help="Nationality",
)
args = parser.parse_args()
greeting(name=args.name, lang=args.lang)
