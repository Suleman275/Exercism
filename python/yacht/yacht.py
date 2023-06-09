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

    if category == ONES or category == TWOS or category == THREES or category == FOURS or category == FIVES or category == SIXES:
        return f_nums(dice, category)
    elif category == YACHT:
        return f_yacht(dice)
    elif category == FULL_HOUSE:
        return f_full_house(dice)
    elif category == FOUR_OF_A_KIND:
        return f_four_of_a_kind(dice)
    elif category == LITTLE_STRAIGHT:
        return f_little_straight(dice)
    elif category == BIG_STRAIGHT:
        return f_big_straight(dice)
    elif category == CHOICE:
        return f_choice(dice)

def f_nums(dice, category):
    count = 0
    for die in dice:
        if die == category:
            count += 1

    return count*category

def f_yacht(dice):
    if dice[0] == dice[4]:
        return 50
    else:
        return 0

def f_full_house(dice):
    if dice[0] != dice[4]:
        if (dice[0] == dice[2] and dice[3] == dice[4]) or (dice[0] == dice[1] and dice[2] == dice[4]):
            return sum(dice)

    return 0

def f_four_of_a_kind(dice):
    if dice[0] == dice[3]:
        return sum(dice[0:4])
    elif dice[1] == dice[4]:
        return sum(dice[1:5])
    
    return 0

def f_little_straight(dice):
    if dice[0] == 1 and dice[4] == 5 and sum(dice) == 15:
        return 30
    return 0

def f_big_straight(dice):
    if dice[0] == 2 and dice[4] == 6 and sum(dice) == 20:
        return 30
    return 0

def f_choice(dice):
    return sum(dice)