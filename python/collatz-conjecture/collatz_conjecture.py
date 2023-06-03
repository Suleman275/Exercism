def steps(number):
    if (number == 1):
        return 0;
    if (number < 1):
        raise ValueError("Only positive integers are allowed")
    else:
        if (number % 2 == 0):
            return steps (number/2) + 1
        else:
            return steps(number*3 +1) + 1
