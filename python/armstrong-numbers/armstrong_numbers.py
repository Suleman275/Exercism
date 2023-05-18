def is_armstrong_number(number):
    x = str(number)
    sum=0
    for i in range(len(x)):
        sum+=(int(x[i]) ** len(x))

    if sum == number:
        return True
    else:
        return False