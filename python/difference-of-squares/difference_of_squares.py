def square_of_sum(number):
    sum = 0
    for i in range(number):
        sum += i
    return sum * sum

def sum_of_squares(number):
    sum = 0 
    for i in range(number):
        sum += i * i


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
