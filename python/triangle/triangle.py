def equilateral(sides):
    return isValid(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if (isValid(sides)):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]
    else:
        return False


def scalene(sides):
    return isValid(sides) and not equilateral(sides) and not isosceles(sides)

def isValid(sides):
    conda = (sides[0] != 0) and (sides[1] != 0) and (sides[2] != 0)
    condb = (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[2] + sides[0] >= sides[1])
    return conda and condb