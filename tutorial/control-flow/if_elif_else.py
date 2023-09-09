import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


print("")
playerchoice = input("Enter...\n1. Rocks\n2. Paper\n3. Scissors\n\n")

# Mặc định input nhập vào của user là dạng string, nếu muốn nhập số phải cast sang int, dùng int()
# Để cast sang string, dùng str()
play = int(playerchoice)

# Để thoát chương trình ngay lập tức, dùng module sys và method sys.exit("...")
if play < 1 or play > 3:
    sys.exit("Invalid input. You must choose from 1 to 3")

# Để chọn random, dùng module random và method choice
computerchoice = random.choice("123")

computer = int(computerchoice)

print("Player chose:", str(RPS(play)).replace("RPS.", ""))
print("Python chose:", str(RPS(computer)).replace("RPS.", ""))

# if elif else
if play == 1 and computer == 3:
    print("🎉 Player wins")
elif play == 2 and computer == 1:
    print("🎉 Player wins")
elif play == 3 and computer == 2:
    print("🎉 Player wins")
elif play == computer:
    print("😮 Tie game")
else:
    print("🐍 Python wins")
