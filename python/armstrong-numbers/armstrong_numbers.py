def is_armstrong_number(number):
    length = len(str(number))
    str = str (number)
    sum = 0
    for i in str:
        sum+= (int(str[i]) ** length)

    if sum == number:
         return true
    else:
         return false