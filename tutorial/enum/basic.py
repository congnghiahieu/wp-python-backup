# import module enum
from enum import Enum
import asyncio as aio


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


print(RPS(2))
print(RPS.ROCK)
print(RPS["ROCK"])
print(RPS.ROCK.value)
