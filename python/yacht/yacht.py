# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice.sort()

    if category == ONES:
        return f_Ones(dice)
    elif category == TWOS:
        return f_Twos(dice)
    elif category == THREES:
        return f_Threes(dice)
    elif category == FOURS:
        return f_Fours(dice)
    elif category == FIVES:
        return f_Fives(dice)
    elif category == SIXES:
        return f_Sixes(dice)
    elif category == YACHT:
        return f_Yacht(dice)
    elif category == FULL_HOUSE:
        return f_Full_House(dice)

def f_Ones(dice):
    count = 0
    for die in dice:
        if die == 1:
            count+=1

    return count * 1

def f_Twos(dice):
    count = 0
    for die in dice:
        if die == 2:
            count+=1

    return count * 2

def f_Threes(dice):
    count = 0
    for die in dice:
        if die == 3:
            count+=1

    return count * 3

def f_Fours(dice):
    count = 0
    for die in dice:
        if die == 4:
            count+=1

    return count * 4

def f_Fives(dice):
    count = 0
    for die in dice:
        if die == 5:
            count+=1

    return count * 5

def f_Sixes(dice):
    count = 0
    for die in dice:
        if die == 6:
            count+=1

    return count * 6

def f_Yacht(dice):
    if dice[0] == dice[4]:
        return 50
    else:
        return 0

def f_Full_House(dice):
    if dice[0] != dice[4]:
        if (dice[0] == dice[2] and dice[3] == dice[4]) or (dice[0] == dice[1] and dice[2] == dice[4]):
            return sum(dice)

    return 0
