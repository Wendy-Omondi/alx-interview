#!/usr/bin/python3
""" Chamges come from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
       determine the fewest number of coins needed
       to meet a given amount total."""
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    fewest = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        fewest += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return fewest
