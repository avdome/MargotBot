import random


"""We do a little Rolling."""


# returns a number from 1 to n in a string message.
def roll(n: int) -> str:
    return 'You rolled a ' + str(random.randint(1, n)) + ' cutie. :wink:'


# returns a number if the roll syntax is correct, otherwise returns 0.
def rollcheck(s: str) -> int:

    if s == 'roll':
        return 6

    s = s.split(' ', 1)

    if s[0] == 'roll':
        return checknum(s[1])
    else:
        return 0


# if num is a single int that, then it will return it, otherwise return 0.
def checknum(num: str) -> int:

    try:
        final = int(num)
        return final
    except ValueError:
        return 0


def mhelp():
    return 'help yourself'
