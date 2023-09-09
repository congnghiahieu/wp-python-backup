""" More: https://docs.python.org/3/library/itertools.html """

from itertools import product, combinations

ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
ranks = [str(rank) for rank in ranks]

suits = ["Hearts", "Clubs", "Diamonds", "Spades"]

deck = list(product(ranks, suits))
# deck = [(x,y) for x in ranks for y in suits]
hands = [hand for hand in combinations(deck, 5)]
print(len(hands))
